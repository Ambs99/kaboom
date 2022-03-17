import random, sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card(
                            ID INTEGER, 
                            NUMBER TEXT, 
                            PIN TEXT, 
                            BALANCE INTEGER DEFAULT 0);""")
conn.commit()

class Bank:
    def __init__(self, card=0, pin=0, balance=0):
        self.card = card
        self.pin = pin
        self.balance = balance

    def luhn(self, number):
        suma = 0
        for i in range(15):
            x = int(number[i])
            if i % 2 == 0:
                x *= 2
                if x > 9:
                    x -= 9
            suma += x
        limit = ((suma // 10) + 1) * 10
        check = (limit - suma) % 10
        return '{}{}'.format(number[:15], check)

    def generate(self):
        self.card = int(self.luhn('%d' % random.randint(4*10**15, 4000009999999999)))
        self.pin = int('%04d' % random.randint(0000, 9999))

transfer = ""
def transfer_check(account, transfer, menu):
    if account.luhn(transfer) == transfer:
        cur.execute('SELECT BALANCE FROM CARD WHERE number = ?', (transfer,))
        transfer_1 = cur.fetchone()
        if transfer_1 == None:
            print("Such a card does not exist.")
            print()
            return

        money = int(input("Enter how much money you want to transfer: "))
        cur.execute("SELECT BALANCE FROM CARD WHERE NUMBER = {}".format(account.card))
        if money > account.balance:
            print("Not enough money!")
            return menu
        else:
            account.balance -= money
            cur.execute("UPDATE CARD SET BALANCE = (balance - {}) where number = {}".format(money, account.card))
            conn.commit()
            cur.execute("UPDATE CARD SET BALANCE = (balance + {}) where number = {}".format(money, transfer))
            conn.commit()
            print("Success!")
            print()
            return menu
    else:
        print("Probably you made a mistake in the card number. Please try again!")
        return menu


def search_card(account, user_card, user_pin):
    cur.execute('SELECT * FROM card WHERE number = ? AND pin = ?', (user_card, user_pin))
    res_1 = cur.fetchone()
    if res_1 == None:
        return False
    account.card = res_1[1]
    account.pin = res_1[2]
    account.balance = res_1[3]
    return res_1 != None


def login_menu(menu,account):
    menu1 = ""
    while menu1 != "0":
        menu1 = input("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")
        if menu1 == "1":
            print(f"Balance: {account.balance}")
            cur.execute('SELECT BALANCE FROM card WHERE number = {}'.format(account.card))
            res = cur.fetchone()
        elif menu1 == "2":
            income = int(input("Enter income:\n"))
            account.balance += income
            cur.execute('UPDATE card SET BALANCE = (balance + {}) WHERE number = {}'.format(income, account.card))
            conn.commit()
            print("Income was added!")
        elif menu1 == "3":
            transfer = input("Transfer\nEnter card number:\n")
            transfer_check(account, transfer, menu)
        elif menu1 == "4":
            cur.execute(f'DELETE FROM card WHERE number = {account.card}')
            conn.commit()
            print("The account has been closed!\n")
            menu1 = "0"
            
        elif menu1 == "5":
            print("You have successfully logged out!\n")
            menu1 = "0"

        elif menu1 == "0":
            menu = "0"
    return menu

def login(account, menu):
    user_card = int(input("Enter you card number: "))
    user_pin = int(input("Enter your PIN: "))
    if search_card(account, user_card, user_pin):
        print("You have successfully logged in!")
        return login_menu(menu, account)
    else:
        print("Wrong card number or PIN!")
    return menu

def create_account(account):
    account.generate()
    print(f"""Your card has been created
Your card number:
{account.card}
Your card PIN:
{account.pin}""")
    cur.execute('INSERT INTO card (number, pin) values (?,?);', (account.card, account.pin))
    conn.commit()

def menu1():

    menu = ""
    account = Bank()
    while menu != "0":
        menu = input("""
1. Create an account
2. Log into account
0. Exit
""")

        if menu == "1":
            create_account(account)
        elif menu == "2":
            menu = login(account, menu)
    print("Bye!")
if __name__=='__main__':
    menu1()
