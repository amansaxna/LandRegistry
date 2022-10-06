warning: LF will be replaced by CRLF in backend/app/__init__.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in backend/blockchain/blockchain.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in backend/pubsub.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in backend/wallet/wallet.py.
The file will have its original line endings in your working directory
[1mdiff --git a/README.md b/README.md[m
[1mindex e69de29..b011526 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -0,0 +1,5 @@[m
[32m+[m[32mset "PEER=True"[m
[32m+[m[32mset FLASK_DEBUG=1[m
[32m+[m[32mset FLASK_ENV=devlopment[m
[32m+[m[32mcd ./Ass1[m[41m   [m
[32m+[m[32mpython -m backend.app[m
\ No newline at end of file[m
[1mdiff --git a/backend/__pycache__/pubsub.cpython-310.pyc b/backend/__pycache__/pubsub.cpython-310.pyc[m
[1mindex 932863a..4ca40c3 100644[m
Binary files a/backend/__pycache__/pubsub.cpython-310.pyc and b/backend/__pycache__/pubsub.cpython-310.pyc differ
[1mdiff --git a/backend/app/__init__.py b/backend/app/__init__.py[m
[1mindex 87bdfa2..301bf29 100644[m
[1m--- a/backend/app/__init__.py[m
[1m+++ b/backend/app/__init__.py[m
[36m@@ -8,7 +8,7 @@[m [mfrom flask_cors import CORS[m
 [m
 from backend.blockchain.blockchain import Blockchain[m
 from backend.wallet.wallet import Wallet[m
[31m-from backend.wallet.transaction import Transaction[m
[32m+[m[32mfrom backend.wallet.transactionLand import Transaction[m
 from backend.wallet.transaction_pool import TransactionPool[m
 from backend.pubsub import PubSub[m
 [m
[36m@@ -34,6 +34,8 @@[m [mdef route_blockchain_mine():[m
     print(block)[m
     pubsub.broadcast_block(block)[m
     transaction_pool.clear_blockchain_transactions(blockchain)[m
[32m+[m[32m    # update blockchain and wallet[m[41m [m
[32m+[m[32m    wallet.update()[m
     return jsonify(block.to_json())[m
     [m
 @app.route('/wallet/transact',methods= ['post'])[m
[36m@@ -41,19 +43,32 @@[m [mdef route_wallet_transact():[m
     #   {'recipient' :'foo', 'amount' :15}[m
     #1. get the data from request[m
     transaction_data = request.get_json()[m
[31m-    transaction = transaction_pool.existing_transaction(wallet.address)[m
[31m-[m
[31m-    if transaction:[m
[31m-        transaction.update([m
[31m-        wallet,[m
[31m-        transaction_data['recipient'],[m
[31m-        transaction_data['amount'][m
[31m-        )[m
[31m-    else:[m
[31m-        transaction = Transaction([m
[32m+[m[32m    #transaction = transaction_pool.existing_transaction(wallet.address)[m
[32m+[m
[32m+[m[32m    #if transaction:[m
[32m+[m[32m    #    transaction.update([m
[32m+[m[32m    #    wallet,[m
[32m+[m[32m    #    transaction_data['recipient'],[m
[32m+[m[32m    #    #transaction_data['amount'][m
[32m+[m[32m    #    transaction_data['Land'][m
[32m+[m[32m    #    )[m
[32m+[m[32m    #else:[m
[32m+[m
[32m+[m[32m    # create a diffrent module for this[m
[32m+[m[32m    max_bid = 0[m
[32m+[m[32m    max_bidder = ""[m
[32m+[m[32m    for bid in blockchain.sales[transaction_data['Land']] :[m
[32m+[m[32m        if(bid[1] >  max_bid )  :[m[41m [m
[32m+[m[32m            max_bid = bid[1][m
[32m+[m[32m            max_bidder = bid[0][m
[32m+[m
[32m+[m[32m    print(max_bid, max_bidder)[m
[32m+[m
[32m+[m[32m    transaction = Transaction([m
             wallet,[m
[31m-            transaction_data['recipient'],[m
[31m-            transaction_data['amount'][m
[32m+[m[32m            max_bidder,[m
[32m+[m[32m            transaction_data['Land'][m
[32m+[m[32m            #transaction_data['amount'][m
         )[m
 [m
     pubsub.broadcast_transaction(transaction)[m
[36m@@ -70,11 +85,17 @@[m [mdef route_wallet_info():[m
 @app.route('/wallet/addLand',methods= ['post'])[m
 def wallet_Land_info():[m
     request_data = request.get_json()[m
[31m-    print("hello")[m
[32m+[m[32m    #add a transaction for adding a land initally[m[41m [m
     wallet.addLand(request_data['name'])[m
     addr = wallet.address[m
     blockchain.add_Land(  request_data['name'] ,addr   )[m
[31m-    return 'sucess'[m
[32m+[m[32m    """transaction = Transaction([m
[32m+[m[32m            wallet,[m
[32m+[m[32m            wallet.address, # adding to the self[m
[32m+[m[32m            request_data['Land'][m
[32m+[m[32m        )"""[m
[32m+[m[41m    [m
[32m+[m[32m    return 'added as a transaction, please wait for the mining to update wallet'[m
 [m
 @app.route('/blockchain/land')[m
 def blockchain_show_land():[m
[1mdiff --git a/backend/app/__pycache__/__init__.cpython-310.pyc b/backend/app/__pycache__/__init__.cpython-310.pyc[m
[1mindex 6ab8f55..5e31339 100644[m
Binary files a/backend/app/__pycache__/__init__.cpython-310.pyc and b/backend/app/__pycache__/__init__.cpython-310.pyc differ
[1mdiff --git a/backend/blockchain/__pycache__/blockchain.cpython-310.pyc b/backend/blockchain/__pycache__/blockchain.cpython-310.pyc[m
[1mindex 71ae515..c59a39b 100644[m
Binary files a/backend/blockchain/__pycache__/blockchain.cpython-310.pyc and b/backend/blockchain/__pycache__/blockchain.cpython-310.pyc differ
[1mdiff --git a/backend/blockchain/blockchain.py b/backend/blockchain/blockchain.py[m
[1mindex fbfc76d..5b1646b 100644[m
[1m--- a/backend/blockchain/blockchain.py[m
[1m+++ b/backend/blockchain/blockchain.py[m
[36m@@ -14,8 +14,8 @@[m [mclass Blockchain:[m
     def add_block(self, data):[m
         self.chain.append(Block.mine_block(self.chain[-1], data))[m
     [m
[31m-    def add_bidder(self, address, bid_price , land_name ):[m
[31m-        new_bid = (address,bid_price)[m
[32m+[m[32m    def add_bidder(self, bidder_address, bid_price , land_name ):[m
[32m+[m[32m        new_bid = (bidder_address,bid_price)[m
         self.sales[land_name].append(new_bid)[m
     [m
     def list_property(self, land_name ):[m
[36m@@ -24,6 +24,12 @@[m [mclass Blockchain:[m
     def add_Land(self, name, address):[m
         self.land['name'].append([name , address])[m
 [m
[32m+[m[32m    def update(self):[m
[32m+[m[32m        """[m
[32m+[m[32m        update the land infor in the blockchain[m
[32m+[m[32m        """[m
[32m+[m[32m        print("code not implemented")[m
[32m+[m
     def __repr__(self):[m
         return f'Blockchain: {self.chain}'[m
 [m
[1mdiff --git a/backend/pubsub.py b/backend/pubsub.py[m
[1mindex dc2e6bc..7747e48 100644[m
[1m--- a/backend/pubsub.py[m
[1m+++ b/backend/pubsub.py[m
[36m@@ -7,7 +7,6 @@[m [mfrom backend.blockchain.blockchain import Blockchain[m
 from backend.wallet.transaction import Transaction[m
 from backend.wallet.transaction_pool import TransactionPool[m
 [m
[31m-[m
 pnconfig = PNConfiguration()[m
 # subscribe_key from admin panel[m
 pnconfig.subscribe_key = "sub-c-a731cf42-c89c-4871-b5b3-6647ea52b28e"[m
[36m@@ -16,7 +15,7 @@[m [mpnconfig.publish_key =   "pub-c-318e16e1-6ca3-4623-9862-8f1d2fdd6e0f"[m
 pnconfig.user_id = "my_custom_user_id"[m
 pubnub = PubNub(pnconfig)[m
 [m
[31m-CHANNELS =  {   'TEST':'TEST',  'BLOCK':'BLOCK' , 'TRANSACTION' : 'TRANSACTION'}[m
[32m+[m[32mCHANNELS =  {   'TEST':'TEST',  'BLOCK':'BLOCK' , 'TRANSACTION' : 'TRANSACTION' }[m
 [m
 class Listener(SubscribeCallback):[m
     def __init__(self, blockchain, transaction_pool):[m
[36m@@ -38,6 +37,11 @@[m [mclass Listener(SubscribeCallback):[m
                 print(f'\n Succesfully replaced the locla chain ')[m
             except Exception as e:[m
                 print(f'\n Did not replace :{e}')[m
[32m+[m[32m            print("Updating land and wallet")[m
[32m+[m[41m            [m
[32m+[m[32m            # wallet.update()[m
[32m+[m[32m            self.blockchain.update()[m
[32m+[m
         elif message_object.channel == CHANNELS['TRANSACTION']:[m
             transaction = Transaction.from_json(message_object.message)[m
             self.transaction_pool.set_transaction(transaction)[m
[1mdiff --git a/backend/wallet/__pycache__/wallet.cpython-310.pyc b/backend/wallet/__pycache__/wallet.cpython-310.pyc[m
[1mindex a50e2fa..8a67be4 100644[m
Binary files a/backend/wallet/__pycache__/wallet.cpython-310.pyc and b/backend/wallet/__pycache__/wallet.cpython-310.pyc differ
[1mdiff --git a/backend/wallet/wallet.py b/backend/wallet/wallet.py[m
[1mindex 8b9dd2e..cb40b39 100644[m
[1m--- a/backend/wallet/wallet.py[m
[1m+++ b/backend/wallet/wallet.py[m
[36m@@ -27,6 +27,9 @@[m [mclass Wallet:[m
 [m
     def addLand(self, name):[m
         self.land.add(name)[m
[32m+[m[41m    [m
[32m+[m[32m    def update(self):[m
[32m+[m[32m        print("code not implemented")[m
 [m
     def sign(self,data):[m
         """[m
