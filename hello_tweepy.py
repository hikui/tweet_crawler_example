import sys
import tweepy
import codecs
import string
import json

auth = tweepy.OAuthHandler("3779qAQHaXeCoez6gbePLPgx8", "Smh4geVG3LusJBLRBJoI1Bucj5NUDvEJkYGG0d8Y9dvdsI521n")
auth.set_access_token("110147932-RQMjJCMxN26FrIh4lPBFM88HhDrrGLUWdD868RO7", "DLn6oxudmGHJoE1OV6WS9kj0pBVsSxqxX9xgQpyE8ysM3")

from pymongo import MongoClient


class MongoStreamListener(tweepy.StreamListener):

    def __init__(self):
        super(MongoStreamListener, self).__init__()
        client = MongoClient('115.146.88.96',27017)
        db = client.final_project
        collection = db.tweets
        self.collection = collection

    def on_status(self, status):
        json_str = json.dumps(status._json)
        obj = json.loads(json_str)
        inserted_id = self.collection.insert_one(obj).inserted_id
        print(inserted_id)
        



def main():
    twitter_stream_listener = MongoStreamListener()
    stream = tweepy.Stream(auth, twitter_stream_listener)
    stream.sample(languages=['en'])

if __name__ == '__main__':
    sys.exit(int(main() or 0))