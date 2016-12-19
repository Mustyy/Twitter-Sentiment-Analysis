import tweepy
from textblob import TextBlob

consumer_key = 'uNDuNX1PiLZAk7Fhr4vHMudbm'
consumer_secret = 'doBqCf7qtHGQ1TVkuA8QzsshyKRllBrx5PxuHtZsrzFgM0r3Yr'

access_token = '784783562402852864-VaqewzA8V6wBPavkmsfcJtdkM9FWSFK'
access_token_secret = 'BWP7wSN5RM5tl0c8NLRqimiZnnLndCuHQd1Abzgm2IY2p'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_input = input('Enter the topic you would like to analyze: ')

public_tweets = api.search(str(user_input))

for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment,'\n')