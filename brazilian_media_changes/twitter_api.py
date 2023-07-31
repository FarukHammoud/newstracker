import os
import tweepy

class TwitterApi:

    def __init__(self):
        # Remember to set Clients Ids and Secrets from 
        self.api_key = os.environ.get("API_KEY")
        self.api_key_secret = os.environ.get("API_KEY_SECRET")
        self.client_key = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.bearer_token = os.environ.get("BEARER_TOKEN")
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    def post_tweet(self):
        client = tweepy.Client(
                       consumer_key=self.api_key,
                       consumer_secret=self.api_key_secret,
                       bearer_token=self.bearer_token,
                       access_token=self.access_token,
                       access_token_secret=self.access_token_secret)

        response = client.create_tweet(text='hello world')
        print(response)

api = TwitterApi()
api.post_tweet()