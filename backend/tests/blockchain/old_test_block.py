#from backend.blockchain.block import Block,GENESIS_DATA
import json
#def test_block():
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

mine_data = {
    "data": [
        {
            "id": "53b67301",
            "input": {
                "address": "8d0fc811",
                "amount": 1000,
                "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEsjbgT2WyvxkpwbxT/Mr5otyvCitW//M+\nlg8DAM/A2sXPqEN0Qm9ujkj2Zcay6ASDNN6liTbIeWHfFE8gH7DtsQ==\n-----END PUBLIC KEY-----\n",
                "signature": [
                    54165874169992401299038840530400580266157154043395075056126550862577941035227,
                    35348516953911841539557563541885200942735298352486087119883954860560164009526
                ],
                "timestamp": 1665141573.887527
            },
            "output": {
                "land": "land1",
                "name_owner": "8d0fc811"
            }
        }
    ],
    "difficulty": 5,
    "hash": "05f8a77823f44937189f800924e769b9e2d7611a38501c7b11453509a012d3e0",
    "last_hash": "0a70f86e5c08712ab0a8e9b4c4d3c22041514173ed17228ef5cc40300855df30",
    "nonce": 17,
    "timestamp": 1665141591.058639
}
#final_data = dict()
print(mine_data)


