# from datetime import datetime
# import time
# from backend.blockchain import blockchain

# from backend.blockchain.blockchain import Blockchain

# chain = [
#     {
#         "data": [],
#         "difficulty": 3,
#         "hash": "genesis_hash",
#         "last_hash": "genesis_last_hash",
#         "nonce": "genesis_nonce",
#         "timestamp": 1
#     },
#     {
#         "data": [
#             {
#                 "id": "8c1b2dc5",
#                 "input": {
#                     "address": "f5c64684",
#                     "amount": 1000,
#                     "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
#                     "signature": [
#                         64908214225374969192710322602601582652275490649051740563344382979349215771849,
#                         104621515763430037014215446978504098483121885950967581067791276984493083297394
#                     ],
#                     "timestamp": 1665241955.4012885
#                 },
#                 "output": {
#                     "land": "land2",
#                     "name_owner": "aman"
#                 }
#             },
#             {
#                 "id": "4e8eb3df",
#                 "input": {
#                     "address": "f5c64684",
#                     "amount": 1000,
#                     "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
#                     "signature": [
#                         74992237443534912180898697141468105018675533376525451459909252517168592656291,
#                         71608589171770965260149073145188290688805298059070121816517414706099259184470
#                     ],
#                     "timestamp": 1665241956.665174
#                 },
#                 "output": {
#                     "land": "land1",
#                     "name_owner": "chirag"
#                 }
#             }
#         ],
#         "difficulty": 4,
#         "hash": "006a2e5bb20406b1d0f14a3f48d24f8d62cade6a00076ad3b91ac00deb8f7ca4",
#         "last_hash": "genesis_hash",
#         "nonce": 13,
#         "timestamp": 1665241963.7884092
#     },
#     {
#         "data": [
#             {
#                 "id": "3396b218",
#                 "input": {
#                     "address": "f5c64684",
#                     "amount": 1000,
#                     "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
#                     "signature": [
#                         38381506545266748337376811012884723821116608615645706842623647769814707774833,
#                         37036649186661146667411229999190745488425855999443853674087352190695924393088
#                     ],
#                     "timestamp": 1665242013.6176212
#                 },
#                 "output": {
#                     "land": "land3",
#                     "name_owner": "chirag"
#                 }
#             },
#             {
#                 "id": "3396b218",
#                 "input": {
#                     "address": "f5c64684",
#                     "amount": 1000,
#                     "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
#                     "signature": [
#                         38381506545266748337376811012884723821116608615645706842623647769814707774833,
#                         37036649186661146667411229999190745488425855999443853674087352190695924393088
#                     ],
#                     "timestamp": 1665242013.6176212
#                 },
#                 "output": {
#                     "land": "land2",
#                     "name_owner": "manas"
#                 }
#             }
#         ],
#         "difficulty": 5,
#         "hash": "03687719ed49af57e8660bc88dafa2e6e344242662558d5e09f185d3d7dadc49",
#         "last_hash": "006a2e5bb20406b1d0f14a3f48d24f8d62cade6a00076ad3b91ac00deb8f7ca4",
#         "nonce": 6,
#         "timestamp": 1665242019.4576075
#     }
# ]


# winner = "Aman"  # person who gets to mine the block i.e.
#         # who has the smallest timestamp
# age = dict() # dictionary maps wallet address to timestamp

# # if wallet address already present in age do nothing else 
# # add timestamp of that particular transaction

"""
    Python implementation of POS
    In this implementation we are following coinage variation of POS
    where mining right exist with the oldest stake owner until 
    there exist some stake with them
"""
from datetime import datetime
import time
from hashlib import sha256
import json, requests
from random import randint

DATE = datetime.now()
GENESIS_BLOCK = {
    "Index": 0,
    "Timestamp": str(DATE),
    "BPM": 0,  # instead of transactions
    "PrevHash": "",
    "Validator": "",  # address to receive the reward {validator, Land, age}
}
GENESIS_BLOCK2 = {
    "Index": 0,
    "Timestamp": str(DATE),
    "BPM": 0,  # instead of transactions
    "PrevHash": "",
    "Validator": "",  # address to receive the reward {validator, Land, age}
}
GENESIS_BLOCK3 = {
    "Index": 0,
    "Timestamp": str(DATE),
    "BPM": 0,  # instead of transactions
    "PrevHash": "",
    "Validator": "",  # address to receive the reward {validator, Land, age}
}
GENESIS_BLOCK4 = {
    "Index": 0,
    "Timestamp": str(DATE),
    "BPM": 0,  # instead of transactions
    "PrevHash": "",
    "Validator": "",  # address to receive the reward {validator, Land, age}
}


class Blockchain(object):
    def __init__(self, _genesisBlock, account):
        """
        If the genesis block is valid, create chain
        """
        self.blockChain = []
        self.tempBlocks = []
        # self.candidateBlocks = [] #constains block
        self.myCurrBlock = {}
        # self.announcements = []
        self.validators = set()  # stakers and balance
        # self.unconfirmed_txns = []
        self.nodes = set()
        #initialization with 0 Land(stake) and age
        self.myAccount = {"Address": "", "Land": 0, "Age": 0}
        self.myAccount["Address"] = account["Address"]
        self.myAccount["Land"] = account["Land"]
        try:
            genesisBlock = self.generate_genesis_block(_genesisBlock)
            if self.is_block_valid(genesisBlock):
                self.blockChain.append(genesisBlock)
            else:
                raise Exception("Unable to verify block")
        except Exception as e:
            print("Invalid genesis block.\nOR\n" + str(e))

    def is_block_valid(self, block, prevBlock={}):
        try:
            _hash = block.pop("Hash")
        except KeyError as e:
            return False
        try:
            hash2 = self.hasher(block)
            assert _hash == hash2
        except AssertionError as e:
            return False

        prevHash = prevBlock["Hash"] if prevBlock else ""
        block["Hash"] = _hash
        if self.blockChain:
            prevHash = self.blockChain[-1]["Hash"] if not prevHash else prevHash
            try:
                assert prevHash == block["PrevHash"]
            except AssertionError as e:
                if prevHash == self.blockChain[0]["Hash"]:
                    block["Hash"] = _hash
                    return True
                block["Hash"] = _hash
                return False
        block["Hash"] = _hash
        return True

    def generate_new_block(self, bpm=randint(53, 63), oldBlock="", address=""):
        if self.myCurrBlock:
            return self.myCurrBlock
        prevHash = self.blockChain[-1]["Hash"]
        index = len(self.blockChain) if not oldBlock else oldBlock["Index"] + 1
        address = self.get_validator(self.myAccount) if not address else address
        newBlock = {
            "Index": index,
            "Timestamp": str(datetime.now()),
            "BPM": bpm,  # instead of transactions
            "PrevHash": prevHash,
            "Validator": address,
        }
        newBlock["Hash"] = self.hasher(newBlock)
        assert self.is_block_valid(newBlock)
        self.myCurrBlock = newBlock
        return newBlock

    def get_blocks_from_nodes(self):
        if self.nodes:
            for node in self.nodes:
                # resp = requests.get('http://{}/newblock'.format(node))
                node.add_another_block(self.myCurrBlock)
                resp = node.generate_new_block()
                if self.is_block_valid(resp):  # resp.json()
                    # self.tempBlocks.append(resp.json())
                    if not resp["Validator"] in self.validators:
                        self.tempBlocks.append(resp)
                        self.validators.add(resp["Validator"])

    def add_another_block(self, another_block):
        if self.is_block_valid(another_block):
            if not another_block["Validator"] in self.validators:
                self.tempBlocks.append(another_block)
                self.validators.add(another_block["Validator"])

    def pick_winner(self):
        """Creates a lottery pool of validators and choose the validator
        who gets to forge the next block. Random selection Landed by amount of token staked
        Do this every 30 seconds
        """
        winner = []

        self.tempBlocks.append(self.myCurrBlock)
        self.validators.add(self.myCurrBlock["Validator"])
        for validator in self.validators:
            acct = validator.rsplit(sep=", ")
            acct.append(int(acct[1]) * int(acct[2]))
            if winner and acct[-1]:
                winner = acct if winner[-1] < acct[-1] else winner
            else:
                winner = acct if acct[-1] else winner
        if winner:
            return winner
        for validator in self.validators:
            acct = validator.rsplit(sep=", ")
            acct.append((int(acct[1]) + int(acct[2])) / len(acct[0]))
            if winner:
                winner = acct if winner[-1] < acct[-1] else winner
            else:
                winner = acct
        return winner

    def pos(self):
        """
        #get other's stakes
        #add owns claim
        #pick winner
        """

        print(str(self.myAccount) + " =======================> Getting Valid chain\n")
        self.resolve_conflict()
        time.sleep(1)
        self._pos()
        print("***Calling other nodes to announce theirs***" + "\n")
        time.sleep(1)
        for node in self.nodes:
            node._pos()
        time.sleep(1)
        for block in self.tempBlocks:
            validator = block["Validator"].rsplit(", ")
            if validator[0] == self.pick_winner()[0]:
                new_block = block
                break
            else:
                pass
        print("New Block ====> " + str(new_block) + "\n")
        time.sleep(1)
        self.add_new_block(new_block)
        for node in self.nodes:
            node.add_new_block(new_block)
        print("Process ends" + "\n")

    def announce_winner(self):
        self.blockChain.append(self.myCurrBlock)

    def add_new_block(self, block):
        if self.is_block_valid(block):
            # check index too
            self.blockChain.append(block)
            acct = block["Validator"].rsplit(", ")
            if self.myAccount["Address"] != acct[0]:
                self.myAccount["Age"] += 1
            else:
                self.myAccount["Land"] += randint(1, 10) * self.myAccount["Age"]
                self.myAccount["Age"] = 0
        self.tempBlocks = []
        self.myCurrBlock = {}
        self.validators = set()

    def _pos(self):
        print("Coming from ==========================> " + str(self.myAccount) + "\n")
        time.sleep(1)
        print("***Generating new stake block***" + "\n")
        time.sleep(1)
        self.generate_new_block()
        print("***Exchanging temporary blocks with other nodes***" + "\n")
        time.sleep(1)
        self.get_blocks_from_nodes()
        print("***Picking a winner***" + "\n")
        time.sleep(1)
        print("Winner is =======================> " + str(self.pick_winner()) + "\n")

    def resolve_conflict(self):
        for node in self.nodes:
            if len(node.blockChain) > len(self.blockChain):
                if self.is_chain_valid(node.blockChain):
                    print("***Replacing node***" + "\n")
                    self.blockChain = node.blockChain
                    return
        print("***My chain is authoritative***" + "\n")
        return

    def is_chain_valid(self, chain):
        _prevBlock = ""
        for block in chain:
            if self.is_block_valid(block, prevBlock=_prevBlock):
                _prevBlock = block
            else:
                return False
        return True

    def add_new_node(self, new_node):
        self.nodes.add(new_node)
        new_node.add_another_node(self)

    def add_another_node(self, another_node):
        self.nodes.add(another_node)

    @staticmethod
    def hasher(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @staticmethod
    def get_validator(address):
        return ", ".join(
            [address["Address"], str(address["Land"]), str(address["Age"])]
        )

    def generate_genesis_block(self, genesisblock):
        address = {"Address": "eltneg", "Land": 50, "Age": 0}
        address = self.get_validator(address)
        genesisblock["Index"] = (
            0 if not genesisblock["Index"] else genesisblock["Index"]
        )
        genesisblock["Timestamp"] = (
            str(datetime.now())
            if not genesisblock["Timestamp"]
            else genesisblock["Timestamp"]
        )
        genesisblock["BPM"] = 0 if not genesisblock["BPM"] else genesisblock["BPM"]
        genesisblock["PrevHash"] = "0000000000000000"
        genesisblock["Validator"] = (
            address if not genesisblock["Validator"] else genesisblock["Validator"]
        )
        genesisblock["Hash"] = self.hasher(genesisblock)
        return genesisblock


def main():
    """Run test"""
    account = {"Address": "Aman", "Land": 50}
    account2 = {"Address": "Chirag", "Land": 55}
    account3 = {"Address": "Manas", "Land": 43}
    account4 = {"Address": "Sahitya", "Land": 16}
    blockchain = Blockchain(GENESIS_BLOCK, account)
    blockchain.generate_new_block(52)

    blockchain2 = Blockchain(GENESIS_BLOCK2, account2)
    blockchain3 = Blockchain(GENESIS_BLOCK3, account3)

    clients = [blockchain, blockchain2, blockchain3]


    blockchain.add_new_node(blockchain2)
    blockchain.add_new_node(blockchain3)

    blockchain2.add_new_node(blockchain)
    blockchain2.add_new_node(blockchain3)

    blockchain.get_blocks_from_nodes()
    # blockchain2.get_blocks_from_nodes()

    blockchain.pick_winner() # check if temp blocks are same

    blockchain.pos() #caling POS consensus over blockchain

    # blockchain2.pos()
    # blockchain3.pos()

    # blockchain4 = Blockchain(GENESIS_BLOCK4, account4)
    # blockchain4.add_new_node(blockchain)
    # blockchain4.add_new_node(blockchain2)
    # blockchain4.add_new_node(blockchain3)
    # blockchain4.pos()
    # clients.append(blockchain4)

    #continuous process of mining
    while True:
        print("============================================ \n\n")
        client = clients[randint(0, 3)]
        client.pos()


if __name__ == "__main__":
    main()
