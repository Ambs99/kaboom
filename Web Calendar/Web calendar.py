import datetime
from flask import Flask, abort
import sys
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_


app = Flask(__name__)
db = SQLAlchemy(app)
parser = reqparse.RequestParser()
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'

class User(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()


parser.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)
parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)

resource_fields = {
            'id': fields.Integer,
            'event': fields.String,
            'date': fields.DateTime(dt_format='iso8601')
        }

# write your code here
class Endpoint(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return User.query.filter(User.date == datetime.date.today()).all()



class Event(Resource):

    @marshal_with(resource_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_time', type=inputs.date)
        parser.add_argument('end_time', type=inputs.date)

        args = parser.parse_args()
        start = args['start_time']
        end = args['end_time']
        
        if start is None or end is None:
            return User.query.all()
        else:
            
            events = db.session.query(User).filter(and_(User.date <= end, User.date >= start)).all()
            return events




    def post(self):
        args = parser.parse_args()
        data = User(event=args['event'], date=args['date'])
        db.session.add(data)
        db.session.commit()
        result = {
            "message": "The event has been added!",
            "event": args['event'],
            "date": str(args['date'].date())
        }
        return result

class EventByID(Resource):

    @marshal_with(resource_fields)
    def get(self, event_id):
        event = db.session.query(User).filter(User.id == event_id).first()
        if event is None:
            error = "The event doesn't exist!"
            abort(404, error)
        return event

    def delete(self, event_id):
        event = db.session.query(User).filter(User.id == event_id).delete()
        db.session.commit()
        print(event)
        if event == 0:
            error = "The event doesn't exist!"
            abort(404, error)
        return {"message": "The event has been deleted!"}









api.add_resource(Event, '/event')
api.add_resource(Endpoint, '/event/today')
api.add_resource(EventByID, '/event/<int:event_id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
