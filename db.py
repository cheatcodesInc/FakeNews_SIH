import pymongo
from pymongo import MongoClient
import tweepy
from cleantext import clean
import re
from Dictionary import verifiedTweet
from RandomTweets import unverifiedTweet

consumer_key = "PrClisT6ArX0u91a0Tr8FkLEd"
consumer_secret = "c6tRq3XKpi4U5jB1Tavqjb4C3HDmmJ1L7jG6Xskk3CRtqIuAE7"
access_token = "91092883-kaSrqgWvxQiSxSTsAHF7D34mTIBbmTA96W4sLYI9p"
token_secret = "EOcnRNqxpfYSzws7aTz0WWbDYVFepDXLWxnbbDWk4DTr8"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAA%2B0aAEAAAAA3gerSEr%2BsRtUjaXfYK9iiOE1ZWM%3D4v6OoHklVcQobE37ZeWtKT6U7R1rkXIEhR9p1q21SzOo7A3SLg"

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





