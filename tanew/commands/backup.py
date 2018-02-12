# tanew/commands/backup.py

from .status import Status

from parse_te import *

import tweepy

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
            friends = tweepy.Cursor(api.friends_ids)
        
            with open(filename, 'w+') as f:
                for friend in friends.items():
                    f.write(friend.__str__())
                    f.write('\n')

            print("All accounts being followed backed up in {}".format(filename))
                    
        except tweepy.TweepError as te:
            parse_te(te)
        except FileNotFoundError as fnfe:
            print("Something weird happened with opening the backup file")
