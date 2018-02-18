import tweepy

from .createlist import CreateList

import meta
import util

import logging


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
                list = api.get_list(api.me().screen_name, owner, slug_arg)
                list_id = list.id
                if size <= meta.LIST_MAX:
                    for friends_id in friends_ids:
                        log.info("Adding {} to list".format(friends_id))
                        api.add_list_member(list_id=list_id, id=friends_id)
                else:
                    log.critical("Adding to list for a total member size of over 5000 is not possible")
            else:
                print("No users to add")

        except tweepy.TweepError as te:
            log.error(util.parse_te(te))
            if te.api_code == 104:
                print("Adding members to list locked. Please try again later.")
        except FileNotFoundError as fnfe:
            log.error(fnfe)


