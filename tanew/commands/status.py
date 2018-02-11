# tanew/commands/status.py

from .base import Base

import json

import tweepy

from parse_te import *

class Status(Base):
    def run(self, auth):
        try:
            access_tokens_file = open('access_tokens.json')
            
            access_tokens = json.load(access_tokens_file)
            token = access_tokens['token']
            token_secret = access_tokens['token_secret']

            auth.set_access_token(token, token_secret)
            
            username = '@' +  auth.get_username()
            
            api = tweepy.API(auth)
            following_no = api.friends_ids().__len__()

            print("{} is linked".format(username))
            print("Number of accounts {} is following: {}".format(username, following_no))
            
        except FileNotFoundError as fnfe:
            print("No account linked (try 'tanew linkaccount')")
        except json.decoder.JSONDecodeError as jde:
            print("Account access tokens not found in access_tokens.json")
        except tweepy.TweepError as te:
            print(parse_te(te))
