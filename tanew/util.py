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


def check_list_size(api, twitter_list, expected_size):
    list_members_cursor = tweepy.Cursor(api.list_members, api.me().screen_name, twitter_list.slug)
    list_member_count = sum(1 for x in list_members_cursor.items())

    return list_member_count < expected_size
