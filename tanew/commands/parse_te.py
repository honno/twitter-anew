from json import loads

def parse_te(te):
    json_reason = str(te)[1:-1].replace('\'', '"')
    reason = loads(json_reason)
    return reason['message'] + " (Code {})".format(reason['code'])
