import tweepy

key = 'vPluelKSMjckqdcyEr3cst0QH'
key_secret = 'ZkeGf68XyJxOGQkvXft8THHDTdbUMMzy5hde3AzvH4qISyGTg8'

def getusertweets(access_token, access_token_secret, taglist):
    auth = tweepy.OAuthHandler(key, key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    matches = {}

    for tag in taglist:
        print('tag:'+str(tag))
        for user in tweepy.Cursor(api.search_users, q=tag, per_page=10).items():
            print('user:'+str(user))
            tweets = []
            for tweet in tweepy.Cursor(api.user_timeline, id=user.id, count=100).items():
                print('tweet:'+str(tweet))
                tweets.append(tweet)
            matches[user.screen_name] = tweets

    return matches

getusertweets('2585352386-0A1shtpRmPL68IwlrdC7SE10vnXqRXxUz4BgYHT','3DyLhHWlKwBdZhvxag0k3ncBJnaSsyFhUZRxkFOTxNISe', ['#hack','#hackathon','#arizona'])
