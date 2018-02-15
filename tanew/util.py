def parse_te(te):
    from json import loads

    from re import search as regex_search

    string = ""
    try:
        json_reason = regex_search('\[(\{.+\})\]', str(te)).group(1).replace('\'', '"')
        reason = loads(json_reason)
        string = "Twitter API: {} (Code {})".format(reason['message'], reason['code'])
    except AttributeError:
        string = te
    finally:
        return string


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