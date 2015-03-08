import tweepy

consumer_key = "SqwvX6h8i9TfrwMJfWK3PHv5L"
consumer_secret = "gsAxqf5RyQQOEKyl0gq9AOKfFo8dDEWMIvU1aNQJv2sfKo758o"
access_token = "2585352386-PiCcgwiYciO2mfPGxTaMLXsPD47EAlUZamucJ6z"
access_token_secret = "9082pHXLQyadkuFMzqdy8Hq3SMDPOtSGaoW7HWSoY1qgB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

save = ''

twitter_id = "nfl" # can use us id number or screen name to call data
api.friends_ids(twitter_id)[0:2] # 3 people the user follows

calling_first_tweet = api.user_timeline(twitter_id,count=5)[0]

first_cut = str(calling_first_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_second_tweet = api.user_timeline(twitter_id,count=5)[1]

first_cut = str(calling_second_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_third_tweet = api.user_timeline(twitter_id,count=5)[2]

first_cut = str(calling_third_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_fourth_tweet = api.user_timeline(twitter_id,count=5)[3]

first_cut = str(calling_fourth_tweet).split("text=u")[1]
# line above cuts information before tweet
save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_fifth_tweet = api.user_timeline(twitter_id,count=5)[4]

first_cut = str(calling_fifth_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_sixth_tweet = api.user_timeline(twitter_id,count=6)[5]

first_cut = str(calling_sixth_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_seventh_tweet = api.user_timeline(twitter_id,count=7)[6]

first_cut = str(calling_seventh_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_eigth_tweet = api.user_timeline(twitter_id,count=8)[7]

first_cut = str(calling_eigth_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_ninth_tweet = api.user_timeline(twitter_id,count=9)[8]

first_cut = str(calling_ninth_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

calling_tenth_tweet = api.user_timeline(twitter_id,count=10)[9]

first_cut = str(calling_tenth_tweet).split("text=u")[1]
# line above cuts information before tweet

save += str(first_cut).split("in_reply_to_status_id=")[0]
# line above cuts after tweet and corresponding link

with open('data.txt','w') as writeFile:
    writeFile.write(str(save))
