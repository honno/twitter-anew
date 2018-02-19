import logging

import tweepy

import tanew.meta as meta
import tanew.util as util
from .createlist import CreateList


class AddToList(CreateList):
    def run(self, auth):
        if self.options['--verbose']:
            logging.basicConfig(level=logging.INFO)
        log = logging.getLogger(__name__)

        try:
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

            file_arg = self.options['<file>']
            friends_ids = util.read_friends_ids(file_arg) if file_arg is not None else api.friends_ids()

            owner = api.me().screen_name

            slug_arg = self.options['<slug>']

            friends_ids_known = []
            list_members_cursor = tweepy.Cursor(api.list_members, owner, slug_arg)
            for user in list_members_cursor.items():
                friends_ids_known.append(user.id)

            friend_ids = [id for id in friends_ids if id not in friends_ids_known]

            size = len(friends_ids) + len(friends_ids_known)

            if size > 0:
                if size <= meta.LIST_MAX:
                    twitter_list = api.get_list(api.me().screen_name, owner, slug_arg)
                    list_id = twitter_list.id

                    friends_ids_slices = [friends_ids[i:i + meta.CREATE_ALL_MAX] for i in
                                          range(0, len(friends_ids), meta.CREATE_ALL_MAX)]

                    for friends_ids_slice in friends_ids_slices:
                        log.info("Adding users {} to list".format(friends_ids_slice))
                        api.add_list_members(list_id=list_id, user_id=friends_ids_slice)

                    if util.check_list_size(api, twitter_list, size):
                        log.critical(meta.LIST_SIZE_UNDER_LOG)
                        print(meta.LIST_SIZE_UNDER_PRINT)
                else:
                    log.critical("Adding to list for a total member size of over {} is not possible".format(meta.LIST_MAX))
            else:
                print("No users to add")

        except tweepy.TweepError as te:
            log.error(util.parse_te(te))
        except FileNotFoundError as fnfe:
            log.error(fnfe)
