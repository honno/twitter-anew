# tanew/commands/linkaccount.py

from .base import Base

from json import dump

import webbrowser

import logging

from tweepy import TweepError

import util

class LinkAccount(Base):
    def run(self, auth):
        log = logging.getLogger(__name__)

        try:
            redirect_url = auth.get_authorization_url()
            
            print(redirect_url)
            #webbrowser.open(redirect_url)
            
            pin = input("Press enter pin given to continue: ")
            
            token, token_secret = auth.get_access_token(pin)

            tokens = {}
            tokens['token'] = token
            tokens['token_secret'] = token_secret

            
            auth.set_access_token(token, token_secret)

            print("Account authorized successfully!")
            
            with open('access_tokens.json', 'w+') as f:
                dump(tokens, f, indent=2, sort_keys=True)

            print("Access tokens stored at access_tokens.json")

                
        except TweepError as te:
            log.error(util.parse_te(te))
