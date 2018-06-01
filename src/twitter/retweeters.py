import more_itertools

import twitter

# https://twitter.com/cancan___can/status/1001677871566540801
tweet_id = 1001677871566540801
retweeters_ids = twitter.get_retweeters(tweet_id, 100)
retweeters_100_ids_set = more_itertools.chunked(retweeters_ids, 100)
retweeters_file = open(str(tweet_id) + '_retweeters.txt', 'w')
for friends_100_ids in retweeters_100_ids_set:
    users = twitter.lookup_user(friends_100_ids)
    for user in users:
        retweeters_file.write(user['screen_name'] + '\n')

retweeters_file.close()
