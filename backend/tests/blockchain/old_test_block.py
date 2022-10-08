#from backend.blockchain.block import Block,GENESIS_DATA
import json
from backend.blockchain.block import Block

class Test:
    def _init_(self):
        self.chain = [Block.genesis()]
        """#def test_block():

#    last_block = Block.genesis()
#    data = 'tets-data'
#    new_block = Block(last_block.hash,data)

#    assert isinstance(last_block, Block)
#    assert new_block.data == data
#    assert new_block.last_hash == last_block.hash

#def test_genesis():
#    genesis = Block.genesis()
#    assert isinstance(genesis, Block)
#   assert genesis.last_hash == GENESIS_DATA['last_hash']
#  assert genesis.data == GENESIS_DATA['data']

"""

        block = self.chain[-1]
        print(block)  

  



