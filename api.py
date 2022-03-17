import tweepy
from cleantext import clean
import re
from pprint import pprint
import yake


consumer_key = "PrClisT6ArX0u91a0Tr8FkLEd"
consumer_secret = "c6tRq3XKpi4U5jB1Tavqjb4C3HDmmJ1L7jG6Xskk3CRtqIuAE7"
access_token = "91092883-kaSrqgWvxQiSxSTsAHF7D34mTIBbmTA96W4sLYI9p"
token_secret = "EOcnRNqxpfYSzws7aTz0WWbDYVFepDXLWxnbbDWk4DTr8"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAA%2B0aAEAAAAA3gerSEr%2BsRtUjaXfYK9iiOE1ZWM%3D4v6OoHklVcQobE37ZeWtKT6U7R1rkXIEhR9p1q21SzOo7A3SLg"

# authentication

api = tweepy.Client(bearer_token = bearer_token)

def getDict(user_id):
    tweetDict = {}
    text = ''
    for tweet in tweepy.Paginator(api.get_users_tweets, user_id , exclude = 'retweets' , max_results = 100).flatten(limit=1000):
        string  = " ".join(str(tweet).split())
        string = clean(string, no_emoji=True)
        string=re.sub(r'http\S+', '', string)
        newlist = []
        for letter in string.split():
            if letter.endswith(":"):
                pass
            else:
                newlist.append(letter)
        string = ' '.join(newlist)
        newlist=[]
        for letter in string:
            if letter == "@":
                letter = letter.replace("@", "")
                newlist.append(letter)
            else:
                newlist.append(letter)
        string = ''.join(newlist)
        newstring=string.split()
        res = list(map(lambda st: str.replace(st, "&amp;", "&"), newstring))
        tweetVal = ' '.join(res)
        tweetKey = tweet.id
        tweetDict[tweetKey] = tweetVal
        text += tweetVal
    return (tweetDict , text)

tweetDictionary , text = getDict(231033118)

#print(text)

def sortList(tup):
    tup.sort(key = lambda x: x[1] , reverse = True) 
    return tup

# For Yake
kw_extractor = yake.KeywordExtractor()
language = "en"
numOfKeywords = 100
max_ngram_size = 4
deduplication_threshold = 0.9
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

keywords = custom_kw_extractor.extract_keywords(text)

k=list()
for kw in keywords:
    l = list(kw[0].split())
    if len(l)>=2:
        k.append(kw)

newKeywords = sortList(k)

# Min of 2-gram and max of 4-gram
sortedKeywords = newKeywords[11:20]

query = "(-is:retweet -is:quote -is:reply -is:verified lang:en) ("

for i in sortedKeywords:
    query += "\""+i[0]+"\" OR "

query = query[:len(query)-4]

query += ')'

print(query)
print(len(query))

# This section is for searching the tweets
#tweetsSearched = api.search_recent_tweets(query , max_results = 100)

for tweet in tweepy.Paginator(api.search_recent_tweets , query , max_results = 100).flatten(limit=1000):
    string  = " ".join(str(tweet).split())
    string = clean(string, no_emoji=True)
    string=re.sub(r'http\S+', '', string)
    newlist = []
    for letter in string.split():
        if letter.endswith(":"):
            pass
        else:
            newlist.append(letter)
    string = ' '.join(newlist)
    newlist=[]
    for letter in string:
        if letter == "@":
            letter = letter.replace("@", "")
            newlist.append(letter)
        else:
            newlist.append(letter)
    string = ''.join(newlist)
    newstring=string.split()
    res = list(map(lambda st: str.replace(st, "&amp;", "&"), newstring))
    tweetVal = ' '.join(res)
    tweetId = tweet.id
    print(tweetId)
    print(tweetVal)
    print("\n")

#(-is:retweet -is:quote -is:reply) (Indian OR Government OR "Indian Government" OR Farmers Congress OR Farmers OR Congress OR Government Citizens OR Minister OR Media Government OR People Indian Government OR People Government OR People Indian)