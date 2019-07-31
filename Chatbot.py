from random import *
from sys import *
def main():
    while True:
        isValid = True
        validAnswers = ["hi","tell me a joke","whats your name","play rock paper scissors","draw me a picture","exit"]
        answer = input("(What will you say?)")
        isValid = valid(answer, validAnswers)
        if isValid == True:
            process_input(answer)
        else:
            print("thats not a valid input :(  , try tell me a joke, or play rock paper scissors, draw me a picture, or exit")
def introduction():
    print("Hi im chatbot, type to talk to me!")
def valid(answer, validAnswers):
    if answer in validAnswers:
        return True
    else:
        return False
def process_input(answer):
    if answer == "hi" or answer == "hello":
        greeting()
    elif answer == "tell me a joke":
        joke()
    elif answer == "whats your name":
        name()
    elif answer == "play rock paper scissors":
        rps()
    elif answer == "draw me a picture":
        draw()
    elif answer == "exit":
        exit()
def greeting():
    print("hello!")
def default():
    print("thats cool!")
def draw():
    print("  O  ")
    print(" /|\\ ")
    print(" / \\ ")
def joke():
    jokes = ["There are only 10 kinds of people in this world: those who know binary and those who dont." , "Why do Java programmers wear glasses? They can't C#", "What do you call 8 Hobbits? A Hobbyte."]
    jokenum = randint(0,len(jokes)-1)
    joke = jokes[jokenum]
    print(joke)
def rps():
    moves = ["rock", "paper", "scissors"]
    playerMove = input("enter your move: ")
    myMoveInt = randint(0, len(moves)-1)
    myMove = moves[myMoveInt]
    print("My move is ", myMove)
    if myMove == "rock" and playerMove == "paper":
        print("you won")
    elif myMove == "paper"  and playerMove == "scissors":
        print("you won")
    elif myMove == "scissors" and playerMove == "rock":
        print("you won")
    elif myMove == playerMove:
        print("we tied")
    else:
        print("i won!")
def name():
    print("My name is chatbot!")
if __name__ == "__main__" :
    introduction()
    main()
