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
            api = tweepy.API(auth)

            friends_ids = read(filename)
            friends_no = friends_ids.__len__()
            
            if friends_no != 0:

                friends_ids_iter = iter(friends_ids)
                while True:
                    try:

                        api.create_friendship(friends_ids_iter.__next__())
                    except tweepy.RateLimitError:
                        sleep(1)
                        continue
                    except StopIteration:
                        break

                print("Jobs done!")
            else:
                print("No friend ids in {}".format(filename))


                    
        except tweepy.TweepError as te:
            print(util.parse_te(te))

        except FileNotFoundError as fnfe:
            print(fnfe)
