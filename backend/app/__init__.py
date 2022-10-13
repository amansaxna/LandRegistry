import os
import random
import requests
from flask import Flask, jsonify, request
import json
from flask_cors import CORS 
 #impleemst a CORS middleware

from backend.blockchain.blockchain import Blockchain
from backend.wallet.wallet import Wallet
from backend.wallet.transactionLand import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.pubsub import PubSub

app = Flask(__name__)
CORS(app , resources={ r'/*': { 'origins' :'http://localhost:3000'} })
blockchain = Blockchain()
wallet = Wallet()
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

@app.route('/')
def route_default():
    return 'Welcome to the Blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    blockchain.add_block_pos(transaction_pool.transaction_data())
    block = blockchain.chain[-1]
    print(block)
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)
    # update blockchain and wallet 
    wallet.update()
    return jsonify(block.to_json())
    
@app.route('/blockchain/land')
def get_land():
    return f'Updated Land : { blockchain.land } '

@app.route('/wallet/transact',methods= ['post'])
def route_wallet_transact():
    #   {"land" : "land1"} only care s about which land to transact
    transaction_data = request.get_json()
    #transaction = transaction_pool.existing_transaction(wallet.address)

    #if transaction:
    #    transaction.update(
    #    wallet,
    #    transaction_data['recipient'],
    #    #transaction_data['amount']
    #    transaction_data['Land']
    #    )
    #else:

    # create a diffrent function for finding the max_bidder
    max_bid = 0
    max_bidder = ""
    for bid in blockchain.sales[transaction_data['land']] :
        if(bid[1] >  max_bid )  : 
            max_bid = bid[1]
            max_bidder = bid[0]

    print(max_bid, max_bidder)

    transaction = Transaction(
            wallet,
            max_bidder,
            transaction_data['land']
            #transaction_data['amount']
        )
    
    #empty the bidding 
    del blockchain.sales[transaction_data['land']]

    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())

@app.route('/wallet/info')
def route_wallet_info():
    lands_strings  = ""
    for val in wallet.land:
        lands_strings += val  + " , "  
    return jsonify({ 'address': wallet.address, 'balance': wallet.balance , 'landOwned' : lands_strings })

@app.route('/wallet/addLand',methods= ['post'])
def wallet_Land_add():
    request_data = request.get_json()
    #add a transaction for adding a land initally 
    wallet.addLand(request_data['land'])
    addr = wallet.address
    # blockchain.add_Land(  request_data['name'] ,addr   )
    transaction = Transaction(
            wallet,
            wallet.address, # adding to the self
            request_data['land']
        )
    
    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())

@app.route('/blockchain/land')
def blockchain_show_land():
    """
    list all the land registerd in the blockchain
    """
    return jsonify(blockchain.land)

@app.route('/list' , methods= ['post'])
def blockchain_list_land():
    """
        list a land for sales
    """
    transaction_data = request.get_json()
    blockchain.list_property( transaction_data['land_name'] )
    return f'Sales on for : { blockchain.sales}'

@app.route('/bid', methods= ['post'])
def list_add2auction():
    """
        bid for a land for sales
    """
    transaction_data = request.get_json()
    blockchain.add_bidder( wallet.address, transaction_data['bid_price'] 
                            , transaction_data['land_name'] )
    land_name = transaction_data['land_name']
    return f'Bid successfully for {land_name } : { blockchain.sales[ land_name ] }'

@app.route('/showList')
def show_list():
    """
        show active lists
    """
    return jsonify(blockchain.sales)

@app.route('/TransactionPool')
def show_TP():
    """
        show active lists
    """
    return jsonify(transaction_pool.transaction_data())

@app.route('/blockchain/history', methods= ['post'])
def history():
    """
        list the history of a land
    """
    transaction_data = request.get_json()
    history = blockchain.get_history(transaction_data["land"])
    return history


ROOT_PORT = 5000
PORT = ROOT_PORT

## Custom code for the peer instance
if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001,6000)
    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    result_blockchian = Blockchain.from_json(result.json())
    try:
        blockchain.replace_chain(result_blockchian.chain)
        print('\n Succesfully synchronized the chain')
    except Exception as e:
        print(f'\n Error synchronizing{e}')


app.run(port=PORT)
