def getTweetURL(tweet_id):
    url = "https://twitter.com/abc/status/"
    url += str(tweet_id)
    return url

print(getTweetURL(1502282783581892610))