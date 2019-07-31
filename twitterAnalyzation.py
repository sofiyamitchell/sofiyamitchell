import json
twitterFile = open("./twitter.json","r")
tweetData = json.load(twitterFile)
twitterFile.close()
print("Tweet id: ", tweetData[0]["id"])
# for i in range(len(tweetData)):
#     print("Tweet text: ", tweetData[i]["text"])
for tweet in tweetData:
    print(tweet["text"])
