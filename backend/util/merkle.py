import hashlib
import json
from pprint import pprint

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()



trnsx_pool = [
    {
        "id": "755ff10e",
        "input": {
            "address": "6545496d",
            "amount": 1000,
            "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
            "signature": [
                73323053606282351662690118316090247736484694268906041314994969817597666618374,
                60027851077496506494167076454637985442685275402893710752759264337554208730670
            ],
            "timestamp": 1665032550.8641
        },
        "output": {
            "name_owner" : "aman",
            "land" : "land1"
        }
    },
    {
        "id": "7a9e62f4",
        "input": {
            "address": "6545496d",
            "amount": 1000,
            "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
            "signature": [
                95482100014478040611218385390755933095429261958825809328479790518683788359995,
                111001039000545476710811240226658807527004219171189061343770901960365508300456
            ],
            "timestamp": 1665033449.6759381
        },
        "output": {
            "name_owner" : "manas",
            "land" : "land2"
        }
    },
    {
        "id": "7a9e62f4",
        "input": {
            "address": "6545496d",
            "amount": 1000,
            "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
            "signature": [
                95482100014478040611218385390755933095429261958825809328479790518683788359995,
                111001039000545476710811240226658807527004219171189061343770901960365508300456
            ],
            "timestamp": 1665033449.6759381
        },
        "output": {
            "name_owner" : "manas",
            "land" : "land3"
        }
    }
]

#creating a list of transaction from the pool
list_trnx = list()
for trnsx in trnsx_pool : 
    list_trnx.append(json.dumps(trnsx))
# pprint(type(list_trnx[0]))

#list1 is updated set of transactions
list1 = list()
#list2 is calculated hash of list1 items in pair
list2 = list()

#taking pair from list1 hashing it and adding it to list2
    #if list1.size() == 1 then create pair with same txn
list_trnx = ['1','2','3','4','5']
list1 = list_trnx

while (len(list1) != 1):
    if(len(list1) % 2 !=0): #odd length
        list1.append(list1[-1])
    # pprint(list1)
    for i in range(int(len(list1)/2)):
        # print(i)
        pair = list1[0] +  list1[1]
        # print(f'st1 : {list1[0]} + str 2 : {list1[1]}')
        hash = crypto_hash(pair)
        list1.append(hash)
        del list1[0]
        del list1[0]
    # pprint(list1)
    # pprint("---------")
pprint(list1)    