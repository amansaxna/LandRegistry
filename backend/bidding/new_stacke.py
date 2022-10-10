from dis import code_info


chain = [
    {
        "data": [],
        "difficulty": 3,
        "hash": "genesis_hash",
        "last_hash": "genesis_last_hash",
        "nonce": "genesis_nonce",
        "timestamp": 1
    },
    {
        "data": [
            {
                "id": "8c1b2dc5",
                "input": {
                    "address": "f5c64684",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        64908214225374969192710322602601582652275490649051740563344382979349215771849,
                        104621515763430037014215446978504098483121885950967581067791276984493083297394
                    ],
                    "timestamp": 1665241955.4012885
                },
                "output": {
                    "land": "land2",
                    "name_owner": "aman"
                }
            },
            {
                "id": "4e8eb3df",
                "input": {
                    "address": "f5c64684",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        74992237443534912180898697141468105018675533376525451459909252517168592656291,
                        71608589171770965260149073145188290688805298059070121816517414706099259184470
                    ],
                    "timestamp": 1665241956.665174
                },
                "output": {
                    "land": "land1",
                    "name_owner": "chirag"
                }
            }
        ],
        "difficulty": 4,
        "hash": "006a2e5bb20406b1d0f14a3f48d24f8d62cade6a00076ad3b91ac00deb8f7ca4",
        "last_hash": "genesis_hash",
        "nonce": 13,
        "timestamp": 1665241963.7884092
    },
    {
        "data": [
            {
                "id": "3396b218",
                "input": {
                    "address": "f5c64684",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        38381506545266748337376811012884723821116608615645706842623647769814707774833,
                        37036649186661146667411229999190745488425855999443853674087352190695924393088
                    ],
                    "timestamp": 1665242013.6176212
                },
                "output": {
                    "land": "land3",
                    "name_owner": "chirag"
                }
            },
            {
                "id": "3396b218",
                "input": {
                    "address": "f5c64684",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE8d8oTKNQIN5/zvCQjPx+AyMs7Edc9vEG\njpAQ7hmB5jCIqCwrh4d+hc3P8oSGuScu1vfHV5mM4YQBvEc3DVGq1A==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        38381506545266748337376811012884723821116608615645706842623647769814707774833,
                        37036649186661146667411229999190745488425855999443853674087352190695924393088
                    ],
                    "timestamp": 1665242013.6176212
                },
                "output": {
                    "land": "land2",
                    "name_owner": "manas"
                }
            }
        ],
        "difficulty": 5,
        "hash": "03687719ed49af57e8660bc88dafa2e6e344242662558d5e09f185d3d7dadc49",
        "last_hash": "006a2e5bb20406b1d0f14a3f48d24f8d62cade6a00076ad3b91ac00deb8f7ca4",
        "nonce": 6,
        "timestamp": 1665242019.4576075
    }
]


winner = "Aman"  # person who gets to mine the block i.e.
        # who has the smallest timestamp
age = dict() # dictionary maps wallet address to timestamp

# if wallet address already present in age do nothing else 
# add timestamp of that particular transaction




"""
New algo : 
    minner : oldest and has majority stake in it
"""

# define coin age -> 
# coin_age -> list
    # iteretae through chain, 
    # if( address not in coin_age : add it
    # else do nothing

coin_age = list()
count = dict() 

for iter_block in chain :    # chain -> list[ Block objects ]
    # convert block objects into serialized dict 
    # block.to_json(iter_block) => converted into dict
    if len(iter_block["data"]) == 0 :   # genesis block / block with 0 tranxs
        continue
    # each block's data contains multiple tranxs
    for trnx in iter_block["data"] :
        name_owner = trnx["output"]["name_owner"]
        
        # if name_owner not in coin_age : # address not present
        #     coin_age.append( name_owner )

        if count.get( name_owner ) == None :
            count[ name_owner ] = 1
        else :
            count[ name_owner ] += 1



print(count)
print(coin_age)
def max_stacker(count):
    max_stacker = ""
    max_stake = 0
    for pair in count :
        if max_stake < count[pair] :
            max_stake = count[pair] 
            max_stacker = pair
    return max_stacker

# def pickWinner():
#     # find out the oldest in the max_stack address 
#     # if coin_age IS empty  ALLOW address_minig_req to mine
    
print(max_stacker(count))
