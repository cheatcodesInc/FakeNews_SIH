import streamlit as st
import streamlit.components.v1 as components
import requests
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from Dictionary import getDict # test purpose
from db import storeInDB
from cluster import preprocess, getClusterOfIds
from extraFunc import *
from pred import factcheck

stop_words=set(stopwords.words('english'))
lemma=WordNetLemmatizer()

def predTweet( text ):
    
    text = preprocess( text )
    text = tweet_dict.doc2bow( text )
    l = tweet_lda.get_document_topics( text )
    l.sort( key = lambda x: x[1], reverse = True )
    
    return l[0][0]

def theTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

verifiedTweetDict, _ = storeInDB()
#verifiedTweetDict, _ = getDict( 231033118 )
tweetTexts = list( verifiedTweetDict.values() )
tokenizedTweets = []

X = []

for i in tweetTexts:
    tokens = preprocess( i )
    X.append( tokens )

tweet_dict = corpora.Dictionary( X )
tweet_corpus = [ tweet_dict.doc2bow( token, allow_update = True) for token in X ]

tweet_lda = gensim.models.ldamodel.LdaModel( tweet_corpus, num_topics=10, id2word= tweet_dict, passes=50 )

tweetLabels = [ predTweet( i ) for i in tweetTexts ]
# print( tweetLabels )

dictOfIDs = getClusterOfIds( tweetLabels, verifiedTweetDict )


claim = st.text_input("Enter your claim")

claimLabel = predTweet( claim )
fact = factcheck( claim )
st.header( fact )


listOfRealtedIDs = dictOfIDs[ claimLabel ]
listOfURLs = []

for _ in listOfRealtedIDs:
    listOfURLs.append( getTweetURL( _ ))

for _ in listOfURLs:
    res = theTweet( _ )
    components.html( res, height = 700 )


# the correct label (from predTweet()) has to return a bunch of tweetIds
# the _tweetIds has to pass through getTweetURL()
# create a _listOfURL and then pass through embedtweets()


# input = st.text_input("Enter your claim")

# labelOfTweet = predTweet( tweet )
# st.header( labelOfTweet )

# tweetUrl = [ ]
# for i in tweetUrl:
#     res = theTweet(i)
#     components.html(res,height= 200)