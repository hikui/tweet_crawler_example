import sys
import tweepy
import codecs
import string

auth = tweepy.OAuthHandler("3779qAQHaXeCoez6gbePLPgx8", "Smh4geVG3LusJBLRBJoI1Bucj5NUDvEJkYGG0d8Y9dvdsI521n")
auth.set_access_token("110147932-RQMjJCMxN26FrIh4lPBFM88HhDrrGLUWdD868RO7", "DLn6oxudmGHJoE1OV6WS9kj0pBVsSxqxX9xgQpyE8ysM3")

api = tweepy.API(auth)

filepath = './tweet.txt'

def search_tweets(query, count=200):
    search_results = api.search(q=query, count=count, lang="en")
    for tweet in search_results:
        write_tweets(filepath, tweet)

def write_tweets(filename, tweet):
    with codecs.open(filename, 'a', 'utf-8') as f:
        f.write(string.replace(tweet.text, '\n', ''))
        f.write('\n')

def main():
    search_tweets('iphone7')

if __name__ == '__main__':
    sys.exit(int(main() or 0))