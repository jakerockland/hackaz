import tweepy

consumer_key = "ZW9fy0Sz9dLS9LilRJK1fdMIO"
consumer_secret = "tRgKWz9jMSenWL3ZIwr0aIETkXwpLB64uCZcVdc6Q1mHKTBxDL"
access_token = "2585352386-6JtnsjTdCJZkJhKsaImfGHhPxZJLo1YsGDPJIS7"
access_token_secret = "utdjm1NM8br5yncH14KdgvefZEIpFfTV5Ch3L4Yo3JEpS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_id = "nfl" # can use us id number or screen name to call data
#api.friends_ids(twitter_id)[1:200]

calling_first_tweet = api.user_timeline(twitter_id,count=100)[0]

first_cut = str(calling_first_tweet).split("text=u")[1]
# line above cuts information before tweet

print str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link 
