import more_itertools

import twitter

screen_name = 'yabaiwebyasan'
followers_ids = twitter.get_follower_ids(screen_name)
ids_set = more_itertools.chunked(followers_ids, 100)
file = open(screen_name + '_followers.txt', 'w')
for friends_100_ids in ids_set:
    users = twitter.lookup_user(friends_100_ids)
    for user in users:
        file.write(user['screen_name'] + '\n')

file.close()
