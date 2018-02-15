# tanew/commands/status.py

from.base import Base

import util

import meta

import json

from time import sleep

from datetime import date

import tweepy

LIST_MAX = 500

DEFAULT_LIST_NAME = "Old"
DEFAULT_LIST_DESCRIPTION = "List of members followed as of {}. Automatically generated by {} ({}).".format(date.today().__str__(), meta.NAME, meta.URL)
DEFAULT_LIST_MODE = "public"

class CreateLists(Base):
    def run(self, auth):

        list_name = self.options['--list-name'] if self.options['--list-name'] != None else DEFAULT_LIST_NAME
        list_desc = DEFAULT_LIST_DESCRIPTION
        list_mode = self.options['--list-mode'] if (self.options['--list-mode'] != None) & ((self.options['--list-mode'] == "public") | (self.options['--list-mode'] == "private")) else DEFAULT_LIST_MODE
        
        try:
            api = tweepy.API(auth)
            
            friends_ids = api.friends_ids()

            friends_no = friends_ids.__len__()
            if friends_no > 500:
                friends_ids_matrix = []
                index = -1
                while friends_ids.__len__() != 0:
                    index += 1
                    friends_ids_matrix.append([])
                    range_stop = friends_ids.__len__() if friends_ids.__len__() < LIST_MAX else LIST_MAX
                    for i in range(0, range_stop):
                        friends_ids_matrix[index].append(friends_ids.pop())

                for i in range(0, friends_ids_matrix.__len__()):
                    list_name_numbered = list_name + " {}".format(i + 1)
                    self.create_list(api, list_name_numbered, list_mode, list_desc, friends_ids_matrix[i])
                    
                    
                    
            elif friends_no > 0:
                self.create_list(api, list_name, list_mode, list_desc, friends_ids)
            else:
                pass
                
        except tweepy.TweepError as te:
            print(util.parse_te(te))

    def create_list(self, api, name, mode, desc, friends_ids):
        friends_ids_iter = iter(friends_ids)
        twitter_list = api.create_list(name, mode, desc)

        while True:
            try:
                api.add_list_member(list_id=twitter_list.id, id=friends_ids_iter.__next__())
            except tweepy.RateLimitError:
                sleep(1)
                continue
            except StopIteration:
                break
