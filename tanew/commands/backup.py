# tanew/commands/backup.py

from .base import Base

import tweepy

def Backup(Base):
    def run(self, auth):
        #super().run(self, auth)
        print("hi")
        api = tweepy.API(auth)
        friends = tweepy.Cursor(api.friends_ids)
        
        with open('backup.json') as f:
            for friend in friends:
                print(friend)
