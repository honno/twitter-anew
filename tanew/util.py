from json import loads

from re import search as regex_search


def parse_te(te):
    return te.reason

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
