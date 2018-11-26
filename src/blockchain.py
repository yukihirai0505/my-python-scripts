from time import time
import json
import hashlib


class Blockchain:
    def __init__(self):
        # ここに初期値を定義してください
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        # トランザクションにコインベースを追加します
        # create_transactionに関しては次のチャプターで紹介します
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash="00000")

    # マイニングにより新しいブロックを作成する
    def create_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        # ブロックの追加をします
        self.chain.append(block)
        return block

    # トランザクション(取引情報)をブロックに追加する
    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index': self.transaction_index,
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        self.transaction_index += 1
        return self.transaction_index - 1, len(self.chain)

    # 現在のチェーンを確認する
    def create_node(self, node):
        pass

    # チェーンが正しいかどうか検証する
    def valid_chain(self, chain):
        pass

    # コンセンサスアルゴリズムによりブロックを承認する
    def resolve_conflicts(self, block_list):
        pass


blockchain = Blockchain()
print(blockchain.chain)


def calculate_hash(block):
    data = json.dumps(block).encode()
    return hashlib.sha256(data).hexdigest()


def proof_of_work(blockchain, previous_hash):
    nonce = 0
    while True:
        block = blockchain.create_block(nonce, previous_hash)
        # ブロックのハッシュ値を計算してください
        guess_hash = calculate_hash(block)
        # ハッシュ値のdifficult targetを設定してください
        if guess_hash[:4] == '0000':
            break

        # pop()でリストの最も後ろにある要素を削除しています（先ほど作成したブロックを無効化）
        blockchain.chain.pop()
        nonce += 1
    return block


def mine(blockchain):
    # calculate関数を用いて、直前のブロックのハッシュ値を計算してください
    last_block = blockchain.chain[-1]
    previous_hash = calculate_hash(last_block)
    # proof_of_work関数を用いて、新しくブロックをマイニングしてください
    proof_of_work(blockchain, previous_hash)

    # current_transactionsとtransaction_indexを初期化してください
    blockchain.current_transactions = []
    blockchain.transaction_index = 0
    # current_transactionsにコインベースを追加しています
    blockchain.create_transaction(sender='0', recipient="my_address", amount=1)
    block = blockchain.chain[-1]

    # 新しいブロックの情報をresponseに代入しています
    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return response


def create_transactions(blockchain, values):
    required = ["sender", "recipient", "amount"]
    # allモジュールの中身を作成してsender, recipient, amountの全てが含まれているか確認してください
    if not all([element in values for element in required]):
        return "valueの形式が正しくありません"

    # それぞれ渡して、新しいトランザクション追加してください
    transaction_index, block_index = blockchain.create_transaction(values['sender'], values['recipient'], values['amount'])

    response = {"message": f"トランザクションはブロック {block_index}の {transaction_index}番目 に追加されました"}
    return response


values = {
    "sender": "ishikawa",
    "recipient": "kawai",
    "amount": 5
}
create_transactions(blockchain, values)