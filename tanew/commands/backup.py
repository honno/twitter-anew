# tanew/commands/backup.py

from .status import Status

from parse_te import *

import tweepy

from time import sleep

DEFAULT_BACKUP_FILENAME = 'backup.txt'

class Backup(Status):
    def run(self, auth):
        try:
            super().run(auth)
            
            file_arg = self.options['<file>']
            
            if file_arg != None:
                filename = file_arg
            else:
                filename = DEFAULT_BACKUP_FILENAME
            
            api = tweepy.API(auth)
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
            parse_te(te)
        except FileNotFoundError as fnfe:
            print("Something weird happened with opening the backup file")
