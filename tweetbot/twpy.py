import os
import tweepy

# 各種キーをセット
CONSUMER_KEY = os.environ["VAR_TWEET_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ['VAR_TWEET_CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = os.environ['VAR_TWEET_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['VAR_TWEET_ACCESS_SECRET']
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')
