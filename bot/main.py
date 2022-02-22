import tweepy
import time

auth = tweepy.OAuthHandler('kcaGq8On6b2w1lo2nmN9p50dE','Wdxu0bpqhbprTgV0oQyqssrCJ33MfLhsKIeex53z7cSHaSVj8N')
auth.set_access_token('1467133434615058432-bpkSFTIJqVFAmIUyTb7YMXuyjdddXP','IgBKjvW38QGxANaLrwYa1SzkWGFoeCZf3otANsUe8edWk')

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
stream.filter(track=["NFTcollector"], languages=["en"])
