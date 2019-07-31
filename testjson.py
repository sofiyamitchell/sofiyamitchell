import json
data = json.load(allanswers)
numPeople = 0
for i in data['names']:
    numPeople = numPeople + 1
