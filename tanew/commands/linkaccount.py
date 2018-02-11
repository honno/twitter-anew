# tanew/commands/linkaccount.py

from .base import Base

from json import dump

import webbrowser

from time import sleep

from tweepy import TweepError

from parse_te import *

class LinkAccount(Base):
    def run(self, auth):
        try:
            redirect_url = auth.get_authorization_url()
            
            print(redirect_url)
            webbrowser.open(redirect_url)
            
            sleep(3)
            
            pin = input("Press enter pin given to continue:\n")
            
            access_token, access_token_secret = auth.get_access_token(pin)

            tokens = {}
            tokens['token'] = access_token
            tokens['token_secret'] = access_token_secret
            
            with open('access_tokens.json', 'w+') as f:
                dump(tokens, f)
        except TweepError as te:
            print(parse_te(te))
