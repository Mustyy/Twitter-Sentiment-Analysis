import tweepy
from textblob import TextBlob
import config

# Place your OWN (Consumer Key, Consumer Secret, Access Token, Access Secret Token)
# inside auth & auth.set_access_token.

# You can obtain them from:
# https://apps.twitter.com/

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

try:
	print ('\n**** Twitter Sentiment Analysis ****\n')
	user_input = input('Enter the topic you would like to analyze: ')

	public_tweets = api.search(str(user_input))

	for tweet in public_tweets:
		print (tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment,'\n')

except Exception as e:
	print ('\nThe following error has occured:',str(e))