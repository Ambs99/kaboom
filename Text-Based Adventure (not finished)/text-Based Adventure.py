def welcome_message():
    print("\nHello! Welcome to this new adventure! You have been trapped in this building.\n\
    Explore the rooms until you find the way out.\n\
    Be careful, in these rooms you could find enemies to defeat or in the best cases, diamonds to take home.\n\
    Only if you get out of here.\n")


global hearts
hearts = 3
global diamonds
diamonds = 0
global heartsA
global heartsA1


def main_room():
    option1 = input("\nSelect A or B to choose a room: ")

    if option1 == "A" or option1 == "a":
        global diamondsA
        diamondsA = diamonds + 5
        print("Oh look! You found 5 diamonds! Now you have",
              diamondsA, "diamonds in total")
        room_A()

    elif option1 == "B" or option1 == "b":
        global heartsB
        heartsB = hearts + 1
        print("Seems like your will need this extra heart. Now you have",
              heartsB, "hearts in total")

    else:
        print("\nMmm... I didn't get that, please choose A or B")
        main_room()


def room_A():
    option2 = input("\nSelect A or B to choose another room: ")
    if option2 == "A" or option2 == "a":
        print("\nOh no, this room has enemies! Luckily there are some things to protect yourself.")
        weapon1()
    elif option2 == "B" or option2 == "b":
        #print("\nLooks like this heart will come in handy")
        pass
    else:
        room_A


def weapon1():

    weapon = input("Select between a rock or a rusty sword as your weapon: ")
    if weapon == "rock" or weapon == "Rock":
        heartsA = hearts - 1
        print("\nWell... That didn't work out. But somehow you scape from that room and you lose 1 heart. Now you have", heartsA, "hearts.")
        print("\nIn front of you, there are two doors.")
        roomA1()

    elif weapon == "rusty sword":
        print("\nHooray! Somehow that rusty sword helped!")
        print("\nIn front of you, there are two doors.")
        roomA1()
    else:
        print("\nWell... You only have those two options to fight.")
        weapon1()


def roomA1():
    #global heartsA1
    #heartsA1 = heartsA + 1
    option = input("Choose between A or B: ")
    if option == "A" or option == "a":
        # heartsA1
        print("""\nAfter that fight. You deserve to get this heart. Now you have" "hearts in total.
                Now, let's get out of here. And there's only one door.
                Could that be the way out?""")
        # Change hearts number
        user = input("\nEnter 'Continue' to move on: ")
        if user == "continue" or user == "Continue":
            print("""\nOh no. There are some enemies...
            But they haven't seen you yet. What do you wanna do?""")
            roomA2()

    elif option == "B" or option == "b":
        print("\nOh no! More enemies to face!")
        roomA3()

    else:
        roomA1()


def roomA2():
    weapon = input("""\nEnter 'A' if you wanna distract them throwing a rock and running away to that door pass the room
    or enter 'B' if you wanna fight them: """)
    if weapon == "A" or weapon == "a":
        print("""That worked! And the door was your way out. 
                Way to go! You escaped with #hearts and #diamonds""")
        ending()

    elif weapon == "B" or weapon == "b":
        pass
    else:
        roomA2()


def roomA3():
    weapon = input(
        "\nChoose a way to fight. Enter 'A' to give them some cake or 'B' to cut a rope that's beside you: ")
    if weapon == "A" or weapon == "a":
        # hearts
        print("Ups! They don't like cakes. They prefer salty stuff. *You lose 1 heart* Total: #\n\
                All beaten up and confused you pass through a door.\n\
                ....\n\
                Seems like this isn't your day. You have to face more enemies. But they haven't seen you yet so choose wisely what to do.")
        roomA2()

    elif weapon == "B" or weapon == "b":
        print("That rope was linked to a big box that was above your enemies.\n\
                Don't worry, it didn't fall over them. But it was enough to scare them off for a bit.\n\
                On the other side of the room you see a door. And pass throught it.\n\
                ...\n\
                And yup, these enemies are everywhere. But they haven't seen you just yet. Choose wisely your next move.")
        roomA2()

    else:
        roomA3()


def ending():
    option = input("""Do you wanna play again? 
                    Enter Yes or No: """)
    if option == "yes" or option == "Yes":
        welcome_message()
        main_room()
    else:
        exit


welcome_message()
main_room()


# Have a total of 0 diamonds at first and 5 hearts
# Have 2 options for each room
# If found an enemy choose between 2 options to defeat him
# If couldn't defeat him, loses 1 heart and moves to another room
# If chest found, the player can chooses between 3 chests and get the amount of diamons (5,10,0,15)
# Have a tracker of how much has the player walked
#
