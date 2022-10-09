from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]
        self.land = {}  # dict  : map  : land - > wallet address  
        self.wallets = {}    # dict : map : address -> name 
        self.sales = {}     # dict : property -> list of bidding  
        self.stackers = {}

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
    
    def add_bidder(self, bidder_address, bid_price , land_name ):
        new_bid = (bidder_address,bid_price)
        self.sales[land_name].append(new_bid)
    
    def list_property(self, land_name ):
        self.sales[land_name] = []
    
    def add_Land(self, name, address):
        """
        add land to the blockchain 
        """
        self.land['name'].append([name , address])

    def update(self):
        """
        update the land infor in the blockchain
        """
        block = self.chain[-1].to_json()
        print(f'block - > {type(block)} => \n \n {block}')
        data =  block.get("data")
        for trnx in data:
            landName = trnx["output"]["land"]
            landOwner = trnx["output"]["name_owner"] 
            if self.land.get(landName)==None :
                self.land[landName] = landOwner
            else: #if land already present update ownership
                self.land.update({landName : landOwner})
        
        

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming one if the following applies:
          - The incoming chain is longer than the local one.
          - The incoming chain is formatted properly.
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace. The incoming chain must be longer.')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e} ')

        self.chain = chain

    def to_json(self):
        """ 
        Serialize the blockchiain into a list of blocks.
        """
        serialized_chain = []

        for block in self.chain:
            serialized_chain.append(block.to_json())

        return serialized_chain

    @staticmethod
    def from_json(chain_json):
        """
        Deserialize a list of serialozed blocks into blockchain 
        the result will contain a chainlist of block instances.
        """
        blockchain = Blockchain()
        blockchain.chain = list(
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )
        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the blockchain:
          - the chain must start with the genesis block
          - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py ___name__: {__name__}')

if __name__ == '__main__':
    main()
