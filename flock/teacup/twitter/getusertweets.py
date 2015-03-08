import tweepy
import flock.config

twitter_auth = flock.config.oauth.get('twitter', {})
key = twitter_auth["consumer_key"]
key_secret = twitter_auth["consumer_secret"]

def getusertweets(access_token, access_token_secret):
    auth = tweepy.OAuthHandler(key, key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    username = api.me().screen_name

    tweets = []

    for tweet in tweepy.Cursor(api.user_timeline, count=100).items():
        tweets.append(tweet)

    return username, tweets
