import json

from requests_oauthlib import OAuth1Session
from pprint import pprint

import config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)


def get_twitter_response(url, params):
    req = twitter.get(url, params=params)
    if req.status_code == 200:
        return json.loads(req.text)
    else:
        print("ERROR: %d" % req.status_code)


def get_friend_ids(_screen_name, _next_cursor=-1, _ids=None):
    if _ids is None:
        _ids = []
    url = 'https://api.twitter.com/1.1/friends/ids.json'
    params = {
        'screen_name': _screen_name,
        'cursor': _next_cursor
    }
    response = get_twitter_response(url, params)
    next_cursor = response['next_cursor']
    _ids.extend(response['ids'])
    if next_cursor:
        return get_friend_ids(_screen_name, next_cursor, _ids)
    else:
        return _ids


def lookup_user(ids):
    url = 'https://api.twitter.com/1.1/users/lookup.json'
    params = {'user_id': ids}
    return get_twitter_response(url, params)


def timeline(count):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'count': count
    }
    return get_twitter_response(url, params)


def search_tweet(query, tweet_id, _max_id=-1, _screen_names=None):
    if _screen_names is None:
        _screen_names = []
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {
        'q': query,
        'since_id': tweet_id,
        'max_id': _max_id
    }
    response = get_twitter_response(url, params)
    screen_names = list(map(lambda x: x['user']['screen_name'], response['statuses']))
    max_id = response['search_metadata']['max_id']
    _screen_names.extend(screen_names)
    if max_id > 0:
        return search_tweet(query, tweet_id, max_id, _screen_names)
    else:
        return _screen_names


def get_tweet_info(tweet_id):
    url = 'https://api.twitter.com/1.1/statuses/show.json'
    params = {
        'id': tweet_id
    }
    return get_twitter_response(url, params)


def get_retweeters(tweet_id, count, _next_cursor=-1, _ids=None):
    if _ids is None:
        _ids = []
    url = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json'
    params = {
        'id': tweet_id,
        'count': count
    }
    response = get_twitter_response(url, params)
    next_cursor = response['next_cursor']
    _ids.extend(response['ids'])
    if next_cursor:
        return get_retweeters(tweet_id, count, next_cursor, _ids)
    else:
        return _ids


def get_friendships_show(source_screen_name, target_screen_name):
    url = 'https://api.twitter.com/1.1/friendships/show.json'
    params = {
        'source_screen_name': source_screen_name,
        'target_screen_name': target_screen_name
    }
    return get_twitter_response(url, params)
