import json

from re import search as regex_search
import tweepy

def parse_te(te):
    msg = te
    try:
        reason = te.response.json()['errors'][0]
        msg = "Twitter API: {} (Code {})".format(reason['message'], reason['code'])
    except Exception:
        pass
    finally:
        return msg

def read_friends_ids(file):
    friends_ids = []
    with open(file, 'r') as f:
        for line in f:
            try:
                id = int(line.rstrip('\n'))
                friends_ids.append(line.rstrip('\n'))
            except ValueError:
                pass
    return friends_ids