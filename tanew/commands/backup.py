# tanew/commands/backup.py

from .base import Base

import util

import tweepy

from time import sleep

DEFAULT_BACKUP_FILENAME = 'backup.txt'

class Backup(Base):
    def run(self, auth):
        try:
            
            file_arg = self.options['<file>']
            filename = file_arg if file_arg != None else DEFAULT_BACKUP_FILENAME

            user_id = self.options['--user-id']
            
            api = tweepy.API(auth)

            if user_id != None:
                friends_ids_cursor = tweepy.Cursor(api.friends_ids, id=user_id).items()
            else:
                friends_ids_cursor = tweepy.Cursor(api.friends_ids).items()

            friends_ids = []

            while True:
                try:
                    friends_ids.append(friends_ids_cursor.next())
                except tweepy.RateLimitError:
                    sleep(1)
                    continue
                except StopIteration:
                    break
            
            with open(filename, 'w+') as f:
                f.write("List of friend ids followed by {}".format(auth.get_username()))
                f.write('\n\n')
                for friend in friends_ids:
                    f.write(friend.__str__())
                    f.write('\n')

            print("All accounts being followed backed up in {}".format(filename))
                    
        except tweepy.TweepError as te:
            util.parse_te(te)
        except FileNotFoundError as fnfe:
            print("Something weird happened with opening the backup file")
