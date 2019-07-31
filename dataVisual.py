import json
from textblob import TextBlob
import matplotlib.pyplot as plt
twitterFile = open("./twitter.json","r")
tweetData = json.load(twitterFile)
twitterFile.close()
polarity = []
subjectivity = []
for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)
totalPolarity = 0
totalSubjectivity = 0
number = len(tweetData)
for i in range(len(polarity)):
    totalPolarity = totalPolarity + polarity[i]
for i in range(len(subjectivity)):
    totalSubjectivity = totalSubjectivity + subjectivity[i]
averagePolarity = totalPolarity / number
averageSubjectivity = totalSubjectivity / number
print("The average polarity is ", averagePolarity)
print("The average subjectivity is ", averageSubjectivity)
plt.hist(polarity,5)
plt.hist(subjectivity,5)
plt.show()
