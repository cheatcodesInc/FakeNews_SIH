import tweepy
from cleantext import clean
import re

consumer_key = "PrClisT6ArX0u91a0Tr8FkLEd"
consumer_secret = "c6tRq3XKpi4U5jB1Tavqjb4C3HDmmJ1L7jG6Xskk3CRtqIuAE7"
access_token = "91092883-kaSrqgWvxQiSxSTsAHF7D34mTIBbmTA96W4sLYI9p"
token_secret = "EOcnRNqxpfYSzws7aTz0WWbDYVFepDXLWxnbbDWk4DTr8"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAA%2B0aAEAAAAA3gerSEr%2BsRtUjaXfYK9iiOE1ZWM%3D4v6OoHklVcQobE37ZeWtKT6U7R1rkXIEhR9p1q21SzOo7A3SLg"

# authentication

api = tweepy.Client(bearer_token=bearer_token)


def getDict(user_id):
    tweetDict = {}
    text = ''
    for tweet in tweepy.Paginator(api.get_users_tweets, user_id, exclude='retweets', max_results=100).flatten(
            limit=1000):
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


verifiedTweetDictionary, text = getDict(231033118)  # PIB
verifiedTweetDictionary2, text2 = getDict(920488039)  # MIB