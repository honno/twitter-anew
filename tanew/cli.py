"""
tanew

Usage:
  tanew status  
  tanew linkaccount  
  tanew createlists [-n]  
  tanew backup <file> [-n]  
  tanew unfollowall [-n]  
  tanew -h | --help  
  tanew --version  

Options:
  -n --no-act  
  -h --help  
  --version  

Examples:
  skele status

Help:
  Hmmmm
"""

from inspect import getmembers, isclass

from docopt import docopt

import tweepy

import json

from parse_te import *

from __init__ import __version__ as VERSION

def main():
    try:
        app_file = open('app.json')

        app = json.load(app_file)
        key = app['key']
        secret = app['secret']
        auth = tweepy.OAuthHandler(key, secret)

        try:
            access_tokens_file = open('access_tokens.json')
            access_tokens = json.load(access_tokens_file)
            
            token = access_tokens['token']
            token_secret = access_tokens['token_secret']

            auth.set_access_token(token, token_secret)
            
        except Exception:
            pass

        """CLI"""
        import commands
        options = docopt(__doc__, version=VERSION)
    
        for k, v in options.items():
            if hasattr(commands, k) and v:
                module = getattr(commands, k)
                commands = getmembers(module, isclass)
                command = [command[1] for command in commands if command[0] != 'Base'][0]
                command = command(options)
                command.run(auth)

    except FileNotFoundError as fnfe:
        if(fnfe.filename == 'app.json'):
                print('No application linked to program (app.json)')
                
    except json.decoder.JSONDecodeError as jde:
        print(jde.msg + " in app.json file")
    except tweepy.TweepError as te:
        print(parse_te(te))
        print("Possibly the application pointed to in app.json does not exist?")
