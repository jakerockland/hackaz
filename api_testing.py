import tweepy

consumer_key = "SqwvX6h8i9TfrwMJfWK3PHv5L"
consumer_secret = "gsAxqf5RyQQOEKyl0gq9AOKfFo8dDEWMIvU1aNQJv2sfKo758o"
access_token = "2585352386-PiCcgwiYciO2mfPGxTaMLXsPD47EAlUZamucJ6z"
access_token_secret = "9082pHXLQyadkuFMzqdy8Hq3SMDPOtSGaoW7HWSoY1qgB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

save = ''

twitter_id = "jtimberlake" # can use us id number or screen name to call data

following_list = api.friends_ids(twitter_id)[0:5] # 5 people the user follows

final_tweets = []
for tweeter in following_list:
    tweets = api.user_timeline(tweeter,count=100)
    for tweet in tweets:
        first_cut = str(tweet).split("text=u")[1]
        # line above cuts information before tweet
        final_tweets.append(str(first_cut).split("in_reply_to_status_id=")[0])
        print str(first_cut).split("in_reply_to_status_id=")[0]


#save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link



with open('justin_timberlake.txt','w') as writeFile:
    for final_tweet in final_tweets:
        writeFile.write(final_tweet+'\n')
