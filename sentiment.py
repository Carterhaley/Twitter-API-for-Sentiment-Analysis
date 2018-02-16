import tweepy
import textblob
consumer_key = 'insert consumer key here'
consumer_secret = 'insert consumer secret here'
access_token = 'insert access token here'
access_secret = 'insert access secret here'
auth = tweepy.OAuthHandler(consumer_key, 
                          consumer_secret)
auth.set_access_token(access_token,
                     access_secret)

api = tweepy.API(auth)

public_tweets = api.search('insert term/phrase to search here')

for tweet in public_tweets:
    print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    print(analysis.sentiment)
