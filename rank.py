import httplib
import json, urllib

def rank(cards):
    data = 'cards=' + json.dumps(cards)
    body = urllib.urlencode({'cards' : json.dumps(cards)})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    conn = httplib.HTTPConnection("rainman.leanpoker.org")
    conn.request("GET", "/rank", data, headers)
    r1 = conn.getresponse()
    res = r1.read()
    ranking = json.loads(res)
    conn.close()

    return ranking['rank']
