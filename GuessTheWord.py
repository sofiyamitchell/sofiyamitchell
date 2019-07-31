word = input("Enter a word to be guessed ")
wordList = []
alreadyGuessed = []
display = []
won = False
numTurns = 0
for i in range(len(word)):
    wordList.extend(word[i])
for i in range(len(word)):
    display.extend("_")
for i in range(len(word)):
    if word[i] == "-" or word[i] == "," or word[i] == "!" or word[i] == "?":
        display[i] = word[i]
while won == False and numTurns < 7:
    isIn = False
    letter = input("enter a letter to guess; ")
    for i in range(len(wordList)):
        if letter == wordList[i]:
            display[i] = letter
            print(display)
            isIn = True
    if isIn == False:
        numTurns = numTurns + 1
    if wordList == display:
        won = True
        print("You guessed correct! The word was ", word)
