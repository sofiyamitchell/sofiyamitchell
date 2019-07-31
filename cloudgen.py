import json
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
twitterFile = open("./twitter.json","r")
tweetData = json.load(twitterFile)
twitterFile.close()
tweetString=""
for tweet in tweetData:
    tweetString = tweetString + tweet["text"]
tb = TextBlob(tweetString)
wordList = tb.words
print(tb.word_counts)
