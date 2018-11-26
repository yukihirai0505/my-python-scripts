# -*- coding: utf-8 -*-
from urllib.parse import parse_qsl
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import get as GET
from time import sleep
import random

# 検索キーワードを変えたい場合は `query = "{キーワード}"` 部分を変更
query = "世界一のプログラマー"
rank = 1


def search_google(start):
    html = GET("https://www.google.co.jp/search?q=%s&start=%d" % (query, start)).text
    bs = BeautifulSoup(html, 'lxml')

    for el in bs.select("h3.r a"):
        global rank
        title = el.get_text()
        url = dict(parse_qsl(urlparse(el.get("href")).query))["q"]
        print('%d. %s: %s' % (rank, title, url))
        rank += 1


# 100件以上取得したい場合は `range(10)` の中の数字を変更 range(11) とすれば1ページ目から11ページ目まで取得できる
for i in range(10):
    # 一気に呼び込むとGoogleに怒られそうなので1リクエスト毎に4-6秒時間あけてリクエスト
    search_google(i * 10)
    sleep(random.randint(4, 6))
