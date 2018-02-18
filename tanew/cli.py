"""
tanew

Usage:
  tanew status  
  tanew linkaccount  
  tanew createlist [<file>] [--list-name=<name>] [--list-mode=<mode>] [-v]
  tanew addtolist <slug> [<file>] [-v]
  tanew backup [<file>] [--user-id=<id>] [-v]
  tanew unfollowall [-v]
  tanew followall [<file>] [-v]
  tanew -h | --help  
  tanew --version  

Options:
  -v --verbose
  -h --help  
  --version  
"""

from inspect import getmembers, isclass

from docopt import docopt

import tweepy

import json

import logging

import tanew.util as util

from tanew.__init__ import __version__ as VERSION

def main():
    log = logging.getLogger(__name__)

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
            
        except FileNotFoundError:
            pass

        """CLI"""
        import tanew.commands as commands
        options = docopt(__doc__, version=VERSION)
    
        for k, v in options.items():
            if hasattr(commands, k) and v:
                module = getattr(commands, k)
                commands = getmembers(module, isclass)
                command = [command[1] for command in commands if command[0] != 'Base'][0]
                command = command(options)
                command.run(auth)

    except FileNotFoundError as fnfe:
        log.error("No application linked to program (app.json)")
    except json.decoder.JSONDecodeError as jde:
        log.error(jde)
    except KeyError as ke:
        log.error(ke)
    except tweepy.TweepError as te:
        log.error(util.parse_te(te))
        if te.api_code == 32:
            print("The application pointed to in app.json does not exist")
