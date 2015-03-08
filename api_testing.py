import tweepy

consumer_key = "SqwvX6h8i9TfrwMJfWK3PHv5L"
consumer_secret = "gsAxqf5RyQQOEKyl0gq9AOKfFo8dDEWMIvU1aNQJv2sfKo758o"
access_token = "2585352386-PiCcgwiYciO2mfPGxTaMLXsPD47EAlUZamucJ6z"
access_token_secret = "9082pHXLQyadkuFMzqdy8Hq3SMDPOtSGaoW7HWSoY1qgB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_id = "nfl" # can use us id number or screen name to call data
print api.friends_ids(twitter_id)[0:4] # 200 people the user follows

#calling_first_tweet = api.user_timeline(twitter_id,count=100)[0]

#first_cut = str(calling_first_tweet).split("text=u")[1]
# line above cuts information before tweet

#print str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link
