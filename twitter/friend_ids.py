import json, config, more_itertools
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)


def get_friend_ids(_screen_name):
    url = "https://api.twitter.com/1.1/friends/ids.json"
    params = {'screen_name': _screen_name}
    req = twitter.get(url, params=params)
    if req.status_code == 200:
        return json.loads(req.text)['ids']
    else:
        print("ERROR: %d" % req.status_code)
        return []


def lookup_user(ids):
    url = "https://api.twitter.com/1.1/users/lookup.json"
    params = {'user_id': ids}
    lookup_req = twitter.get(url, params=params)
    if lookup_req.status_code == 200:
        return json.loads(lookup_req.text)
    else:
        print("ERROR: %d" % lookup_req.status_code)


screen_name = 'yabaiwebyasan'
friends_ids = get_friend_ids(screen_name)
friend_100_ids_set = more_itertools.chunked(friends_ids, 100)
friends_file = open(screen_name + '_friends.txt', 'w')
for friends_100_ids in friend_100_ids_set:
    users = lookup_user(friends_100_ids)
    for user in users:
        friends_file.write(user['screen_name'] + '\n')

friends_file.close()
