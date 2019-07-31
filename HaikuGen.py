from random import *

#Create the list of words you want to choose from.
fiveSyllables= ["I like butterflies","Don't be so stupid","I like to eat cheese","Get back here right now","I have lost my keys","Do it for the vine","How many pigeons are there","freeshavocado", "Abominable","Abracadabra","Illuminati"]
sevenSyllables= ["I like to cook spaghetti","Petting dogs is good for health","Oxygen is poisonous","The birds are government drones","Why am I writing a haiku","Conceptualization.","Superficiality."]

#Generates a random integer.
fiveOneIndex = randint(0, len(fiveSyllables)-1)
fiveTwoIndex = randint(0, len(fiveSyllables)-1)
sevenIndex = randint(0, len(sevenSyllables)-1)
print(fiveSyllables[fiveOneIndex])
print(sevenSyllables[sevenIndex])
print(fiveSyllables[fiveTwoIndex])
