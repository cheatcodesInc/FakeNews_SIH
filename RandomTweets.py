import tweepy
from cleantext import clean
import re
from QueryGenerator import querylist
from dotenv import load_dotenv
import os
load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
token_secret = os.getenv("token_secret")
bearer_token = os.getenv("bearer_token")

api = tweepy.Client(bearer_token=bearer_token)

unverifiedTweetDictionary = list()

for query in querylist:
    for tweet in tweepy.Paginator(api.search_recent_tweets, query, max_results=10).flatten(limit=10):
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
        tweetId = tweet.id
        # print(tweetId)
        # print(tweetVal)
        unverifiedTweetDictionary.append((tweetId, tweetVal))
        # print("\n")
unverifiedTweet = dict(unverifiedTweetDictionary)

