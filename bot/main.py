import tweepy
import os
import time

auth = tweepy.OAuthHandler('YGbknqiAcUUhtX7gglJ6eQD5H','AFLAT2JO8j6CY2kDvoyyXwEGmnizVGXynNMXGGzJclQQoVLqF3')
auth.set_access_token('1480471014777647104-eYLFi38lSjbPMrUxLLVaDY1nBic2GY','B2z49NWRxOL9iEsXnMdcjCOFWbNVOA7wfgo2GVQELgxej')

api = tweepy.API(auth, wait_on_rate_limit=True)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print("Tweet Found!")
        print(f"TWEET: {tweet.author.screen_name} - {tweet.text}")
        if tweet.in_reply_to_status_id is None and not tweet.favorited:
            try:
                print("Attempting like...")
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                print("Tweet successfully liked :)")
            except Exception as err:
                print(err)

# Creating StreamListener
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["Python"], languages=["en"])
