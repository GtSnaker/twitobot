import tweepy
import time
import datetime

CONSUMER_KEY = '3T3HTjbkmWCMWHcQ32FBIlfos'
CONSUMER_SECRET = 'laBiAkeGHENLKH0lSH816zzjL7LmJrUjg2vZsauNVHobn7VrGI'
ACCESS_TOKEN = '1281603361-2u70EqoTWXIWRAKCA5Rshw1XI33o4snauf21i8w'
ACCESS_TOKEN_SECRET = 'zsxZ4t7bM3Z0fpWo2Mws5IcmJsyaPRHIuiPiDqYkO8mfo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


friendos = list()
friendosID = list()
retweeted_id = list()
tweets_id_left = list()
retweets_id_done = list()

friendos.append("theartbond_team")
# friendos.append("_kasscabel")

retweets_done = api.retweets_of_me(count=10000)

for rt in retweets_done:
    retweets_id_done.append(rt.id)


for friendo in friendos:
    friendosID.append(api.get_user(friendo).id)

for ID in friendosID:
    my_user_timeline = api.user_timeline(id=ID, count=10000)
    my_user_timeline.reverse()
    for my_tweet in my_user_timeline:
        if (my_tweet.id not in tweets_id_left) and (my_tweet.id not in retweeted_id):
            tweets_id_left.append(my_tweet.id)
            # print my_tweet.text

for ID in tweets_id_left:
    if ID in retweets_id_done:
        tweets_id_left.remove(ID)


while True:
    time.sleep(300)

    ahora = datetime.datetime.now()

    if ahora.hour < 23 and ahora.hour > 10:
        for ID in friendosID:
            my_user_timeline = api.user_timeline(id=ID, count=1)
            for my_tweet in my_user_timeline:
                if (my_tweet.id not in tweets_id_left) and (my_tweet.id not in retweeted_id):
                    tweets_id_left.append(my_tweet.id)
                    print my_tweet.id

        if len(tweets_id_left) > 0:
            try:
                actual_id = tweets_id_left.pop(0)
                if actual_id in tweets_id_left:
                    tweets_id_left.remove(actual_id)
                api.retweet(actual_id)
                retweeted_id.append(actual_id)
            except tweepy.error.TweepError:
                pass
