"""
to update the land information with in land attribute 
inside the blockchain class 
using chain

"""
land = {
     "land1" : "f5bc0386"
} 
 # dict  : map  : land - > wallet address
block = {
    "data": [
        {
            "id": "1b783113",
            "input": {
                "address": "5d853afc",
                "amount": 1000,
                "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEmLKr8GDEGiOOB9uNSHtTnovQuXEvxC7y\nQhZIjkgQssSBs0DeX8en24tjifkNpQZyISaUwnHjtK1xWm02r2Ullw==\n-----END PUBLIC KEY-----\n",
                "signature": [
                    75056617861011179515713774605111711153234082866727479373769021796619942151641,
                    46661478515215909313479786139297717999930432091597056788606434116445030887352
                ],
                "timestamp": 1665188914.6071258
            },
            "output": {
                "land": "land2",
                "name_owner": "5d853afc"
            }
        },
        {
            "id": "2b086b34",
            "input": {
                "address": "5d853afc",
                "amount": 1000,
                "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEmLKr8GDEGiOOB9uNSHtTnovQuXEvxC7y\nQhZIjkgQssSBs0DeX8en24tjifkNpQZyISaUwnHjtK1xWm02r2Ullw==\n-----END PUBLIC KEY-----\n",
                "signature": [
                    104342705125858068560143175689311921098668404103301905151411255930959601263273,
                    28464582692028894844217352818836186316537232803473648155365543761550678385226
                ],
                "timestamp": 1665189039.275466
            },
            "output": {
                "land": "land1",
                "name_owner": "5d853afc"
            }
        },
        {
            "id": "9a7976f3",
            "input": {
                "address": "5d853afc",
                "amount": 1000,
                "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEmLKr8GDEGiOOB9uNSHtTnovQuXEvxC7y\nQhZIjkgQssSBs0DeX8en24tjifkNpQZyISaUwnHjtK1xWm02r2Ullw==\n-----END PUBLIC KEY-----\n",
                "signature": [
                    91456015900299781953986750717715325616136168850591984878911540672189079153733,
                    72376059207270973314809171211548271551671818540859726669413474431030073732314
                ],
                "timestamp": 1665189044.6466753
            },
            "output": {
                "land": "land3",
                "name_owner": "5d853afc"
            }
        }
    ],
    "difficulty": 4,
    "hash": "074cf6dd63bf9fb4484eaefd8c759fb827912975ed8d7e02e16ad90970d961ab",
    "last_hash": "genesis_hash",
    "nonce": 41,
    "timestamp": 1665189057.95266
}

print(block)

