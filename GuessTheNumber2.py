from random import*
randNum = randint(1,20)
won = False
numTurns = 0
while won == False:
    numTurns = numTurns + 1
    guess = input("Enter a random number 1 through 20 inclusive: ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        	guess = int(guess) # converts a string to an integer
    if guess == randNum:
        won == True
        print("You are correct")
    else:
        if guess > randNum:
            print("The number is lower!")
        else:
            print("The number is higher!")
    if numTurns == 3:
        break
if won == False:
    print("The number was ", randNum)
