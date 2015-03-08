import tweepy
import flock.config

twitter_auth = flock.config.oauth.get('twitter', {})
key = twitter_auth["consumer_key"]
key_secret = twitter_auth["consumer_secret"]

def getusertweets(access_token, access_token_secret):
    auth = tweepy.OAuthHandler(key, key_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

    tweepy.Cursor(api.me)

    API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
    API.search_users(q[, per_page][, page])

    return
