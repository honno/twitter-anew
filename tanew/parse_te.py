from json import loads

from re import search as regex_search

def parse_te(te):
    string = ""
    try:
        json_reason = regex_search('\[(\{.+\})\]', str(te)).group(1).replace('\'', '"')
        reason = loads(json_reason)
        string = "Twitter API: {} (Code {})".format(reason['message'], reason['code'])
    except AttributeError:
        string = te
    finally:
        return string
