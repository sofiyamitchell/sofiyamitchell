from random import*
randNum = randint(1,20)
won = False
for i in range(3):
    guess = input("Enter a random number 1 through 20 inclusive: ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        	guess = int(guess) # converts a string to an integer
    if guess == randNum:
        print("You are correct!")
        won = True
        break
    else:
        if guess > randNum:
            print("The number is lower!")
        else:
            print("The number is higher!")

if won == False :
    print("The number was ", randNum)
