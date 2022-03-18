import pymongo
from pymongo import MongoClient
import tweepy
from cleantext import clean
import re
from Dictionary import verifiedTweet
from RandomTweets import unverifiedTweet

# Connecting to Database
try:
    cluster = MongoClient("mongodb+srv://puru:puru@cluster0.gh8mp.mongodb.net/TweetData?retryWrites=true&w=majority")
    print("Database connected successfully")
except:
    print("Database connection failed")

tweetdb = cluster["TweetData"]
verifiedTweetCollection = tweetdb["VerifiedTweets"]
unverifiedTweetCollection = tweetdb["UnverifiedTweets"]



# Inserting PIB and MIB docs to mongodb 
for key , value in verifiedTweet.items():
    try:
        verifiedTweetCollection.insert_one({"_id" : key , "tweet": value})
    except pymongo.errors.DuplicateKeyError:
        continue

# Inserting Unverified docs to mongodb
for key , value in unverifiedTweet.items():
    try:
        unverifiedTweetCollection.insert_one({"_id" : key , "tweet": value})
    except pymongo.errors.DuplicateKeyError:
        continue


# Reading data from mongodb
# cursor = tweetcollection.find()
# for doc in cursor:
#     print(doc)





