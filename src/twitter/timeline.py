import twitter

timeline = twitter.timeline(5)
for tweet in timeline:
    print(tweet['user']['name'] + '::' + tweet['text'])
    print(tweet['created_at'])
    print('----------------------------------------------------')
