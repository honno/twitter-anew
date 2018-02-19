import logging

import tweepy

import tanew.util as util
from .base import Base


class UnfollowAll(Base):
    def run(self, auth):
        if self.options['--verbose']:
            logging.basicConfig(level=logging.INFO)
        log = logging.getLogger(__name__)

        try:
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

            friends_ids = tweepy.Cursor(api.friends_ids).items()

            for friend_id in friends_ids:
                log.error("Unfollowing user {}".format(friend_id))
                api.destroy_friendship(friend_id)

            print("Unfollowed everybody!")

        except tweepy.TweepError as te:
            log.error(util.parse_te(te))
