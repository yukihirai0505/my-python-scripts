import ccxt

exchanges = {
    "bitflyer": {
        "apiKey": "",
        "secret": ""
    },
    "quoinex": {
        "apiKey": "",
        "secret": ""
    },
    "zaif": {
        "apiKey": "",
        "secret": ""
    }
}

amount = 0.001
ask_exchange = ''
ask_price = 99999999
bid_exchange = ''
bid_price = 0

# 各取引所のaskとbidを取得
for exchange_id in exchanges:
    exchange = eval('ccxt.' + exchange_id + '()')

    orderbook = exchange.fetch_order_book('BTC/JPY')
    bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    if ask < ask_price:
        ask_exchange = exchange_id
        ask_price = ask
    if bid > bid_price:
        bid_exchange = exchange_id
        bid_price = bid

# 裁定取引を行う
# 買い
ask_price = int(ask_price / 5) * 5
exchange = eval('ccxt.' + ask_exchange + '()')
exchange.apiKey = exchanges[ask_exchange]["apiKey"]
exchange.secret = exchanges[ask_exchange]["secret"]
exchange.create_limit_buy_order('BTC/JPY', amount, ask_price)

# 売り
bid_price = int(bid_price * 5) / 5
exchange = eval('ccxt.' + bid_exchange + '()')
exchange.apiKey = exchanges[bid_exchange]["apiKey"]
exchange.secret = exchanges[bid_exchange]["secret"]
exchange.create_limit_sell_order('BTC/JPY', amount, bid_price)

print(ask_exchange, 'で', ask_price, '円で', amount, '買って')
print(bid_exchange, 'で', bid_price, '円で', amount, '売ったので')
print((bid_price - ask_price) * amount, '円の利益！')
