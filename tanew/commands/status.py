# tanew/commands/status.py

from .base import Base

import json

import tweepy

from parse_te import *

class Status(Base):
    def run(self, auth):
        try:
            
            
            username = '@' +  auth.get_username()
            
            api = tweepy.API(auth)
            following_no = api.friends_ids().__len__()

            print("{} is linked".format(username))
            print("Number of accounts {} is following: {}".format(username, following_no))
            

        except tweepy.TweepError as te:
            print(parse_te(te))
