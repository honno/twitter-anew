import tweepy

from .base import Base

from .backup import DEFAULT_BACKUP_FILENAME

from time import sleep


import util

class FollowAll(Base):
    def run(self, auth):
        try:
            file_param = self.options['<file>']
            filename = file_param if file_param != None else DEFAULT_BACKUP_FILENAME
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

            friends_ids = util.read_friends_ids(filename)
            friends_no = friends_ids.__len__()
            
            if friends_no != 0:

                for friends_id in friends_ids:
                    api.create_friendship(friends_id)

                print("Jobs done!")
            else:
                print("No friend ids in {}".format(filename))


                    
        except tweepy.TweepError as te:
            print(util.parse_te(te))

        except FileNotFoundError as fnfe:
            print(fnfe)
