import tweepy
from tweepy import OAuthHandler
import flock.config

twitter_auth = flock.config.oauth.get('twitter', {})
key = twitter_auth["consumer_key"]
key_secret = twitter_auth["consumer_secret"]

def getpotentialmatches(access_token, access_token_secret, taglist):
    auth = tweepy.OAuthHandler(key, key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    matches = {}

    for tag in taglist:
        for user in tweepy.Cursor(api.search_users, q=tag, per_page=10).items():
            tweets = []
            for tweet in tweepy.Cursor(api.user_timeline, id=user.id, count=100).items():
                tweets.append(tweet)
            matches[user.screen_name] = tweets

    return matches
