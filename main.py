import streamlit as st
import streamlit.components.v1 as components
import requests

def theTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

tweetUrl = [ ]
for i in tweetUrl:
    res = theTweet(i)
    components.html(res,height= 700)%