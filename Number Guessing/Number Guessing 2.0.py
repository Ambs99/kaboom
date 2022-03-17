import random 

low = int(input("Enter a lower number: "))
high = int(input("Enter a higher number: "))

random_number = random.randint(low, high)

count = 100

#def lower_guess():
    #if guess < random_number and count != 0:
     #   if random_number // 2 == 0:
            

while count != 0:
    guess = int(input("Enter your guess: "))
    if guess != random_number:
        count -= 10
    elif count == 0:
        print("Uh oh! You don't have any more points. The number was {}".format(random_number))

    if guess < random_number and count != 0:
        print("Mmm... Your guess is too low")
        
        
    elif guess > random_number and count != 0:
        print("Mmm... Your guess is too high")
    elif guess == random_number: 
        print("Congrats! You guessed right!")
        break
    