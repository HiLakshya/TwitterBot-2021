import tweepy
from time import sleep

consumer_key = 'x4VpQHEGY6xe0yCxDZhxC9hKv'
consumer_secret = 'CHbVXYRQPOEj95XsD5fr36BcnTlMNTq9DfEwLXf4HiUdj6N0kz'
access_token = '1382744294931447811-qhi4YAgcV1oJ4McfFzY0wWVSXCd7ol'
access_token_secret = '7xe1NPxNRyThe6RK0wEErAdhruW83aJQlS0LU9AyjzDYO'

QUERY = "doge"
LIKE = True
FOLLOW = False
SLEEP_TIME = 0
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)
  
for tweet in tweepy.Cursor(api.search, q = QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
  
        tweet.retweet()
        print('Retweeted the tweet')
  
        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')
  
        # Follow the user who tweeted
        # check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')
  
        sleep(SLEEP_TIME)
  
    except tweepy.TweepError as e:
        print(e.reason)
  
    except StopIteration:
        break
