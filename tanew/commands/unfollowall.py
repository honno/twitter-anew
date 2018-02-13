import tweepy

from .base import Base

from parse_te import *

from time import sleep

class UnfollowAll(Base):
    def run(self, auth):

        try:
            api = tweepy.API(auth)
            friends_ids = tweepy.Cursor(api.friends_ids).items()

            while True:
                try:
                    api.destroy_friendship(friends_ids.next())
                except tweepy.RateLimitError:
                    sleep(1)
                    continue
                except StopIteration:
                    break

            print("Unfollowed everybody!")
                
        except tweepy.TweepError as te:
            print(parse_te(te))

        
