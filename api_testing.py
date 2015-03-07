import tweepy

consumer_key = "ZW9fy0Sz9dLS9LilRJK1fdMIO"
consumer_secret = "tRgKWz9jMSenWL3ZIwr0aIETkXwpLB64uCZcVdc6Q1mHKTBxDL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token("2585352386-6JtnsjTdCJZkJhKsaImfGHhPxZJLo1YsGDPJIS7", "utdjm1NM8br5yncH14KdgvefZEIpFfTV5Ch3L4Yo3JEpS")

api = tweepy.API(auth)

print api.friends_ids("nfl") # This is user NFL
