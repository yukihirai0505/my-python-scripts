import more_itertools

import twitter

screen_name = 'yabaiwebyasan'
friends_ids = twitter.get_friend_ids(screen_name)
friend_100_ids_set = more_itertools.chunked(friends_ids, 100)
friends_file = open(screen_name + '_friends.txt', 'w')
for friends_100_ids in friend_100_ids_set:
    users = twitter.lookup_user(friends_100_ids)
    for user in users:
        friends_file.write(user['screen_name'] + '\n')

friends_file.close()
