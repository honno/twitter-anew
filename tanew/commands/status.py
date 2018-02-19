# tanew/commands/status.py

import logging

import tweepy

import tanew.util as util
from .base import Base


class Status(Base):
    def run(self, auth):
        log = logging.getLogger(__name__)
        try:

            username = "@{}".format(auth.get_username())

            api = tweepy.API(auth)
            following_no = api.friends_ids().__len__()

            print("{} is linked".format(username))
            print("Number of accounts {} is following: {}".format(username, following_no))

        except tweepy.TweepError as te:
            log.error(util.parse_te(te))
