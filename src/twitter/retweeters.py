import twitter

from pprint import pprint

# まとめるとこうなります。since_id も使って絞り込みます。
# q: 「元ツイートのテキスト」+「filter:retweets」+「@user（元ツイートのユーザー）」
# since_id: 元ツイートの ID（リツイートは、必ず元ツイートの後なので、ID により絞り込み）
# max_id を指定して、繰り返し検索します。

# https://twitter.com/cancan___can/status/1001677871566540801
tweet_id = 1001677871566540801
tweet_info = twitter.get_tweet_info(tweet_id)
# query = f'{tweet_info["text"]} filter:retweets @cancan___can'
query = f'3BTC!!!!!!!! filter:retweets @cancan___can'
screen_names = twitter.search_tweet(query, tweet_id)

search_result_file = open(str(tweet_id) + '_search_result.txt', 'w')
for screen_name in screen_names:
    search_result_file.write(screen_name + '\n')
search_result_file.close()
