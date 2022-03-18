import tweepy
from cleantext import clean
import re
from dotenv import load_dotenv
import os
load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
token_secret = os.getenv("token_secret")
bearer_token = os.getenv("bearer_token")
#authentication

api = tweepy.Client(bearer_token=bearer_token)


def getDict(user_id):
    tweetDict = {}
    text = ''
    for tweet in tweepy.Paginator(api.get_users_tweets, user_id, exclude='retweets', max_results=100).flatten(limit=100):
        string = " ".join(str(tweet).split())
        string = clean(string, no_emoji=True)
        string = re.sub(r'http\S+', '', string)
        newlist = []
        for letter in string.split():
            if letter.endswith(":"):
                pass
            else:
                newlist.append(letter)
        string = ' '.join(newlist)
        newlist = []
        for letter in string:
            if letter == "@":
                letter = letter.replace("@", "")
                newlist.append(letter)
            else:
                newlist.append(letter)
        string = ''.join(newlist)
        newstring = string.split()
        res = list(map(lambda st: str.replace(st, "&amp;", "&"), newstring))
        tweetVal = ' '.join(res)
        tweetKey = tweet.id
        tweetDict[tweetKey] = tweetVal
        text += tweetVal
    return tweetDict, text


verifiedTweetPIB, text = getDict(231033118)  # PIB
verifiedTweetMIB, text2 = getDict(920488039)  # MIB

verifiedTweet = dict()
verifiedTweet.update(verifiedTweetMIB)
verifiedTweet.update(verifiedTweetPIB)

