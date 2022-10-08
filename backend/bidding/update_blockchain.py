"""
to update the land information with in land attribute 
inside the blockchain class 
using chain

"""
land = {'name' : [] }  # dict  : map  : land - > wallet address
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
                "id": "dbdf1a3d",
                "input": {
                    "address": "6545496d",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        114864003191439788311665499359893570336855215874922046882684998988415914750468,
                        77398801526828584707890912332243997625291502377432139494188339378892777684880
                    ],
                    "timestamp": 1665024613.768578
                },
                "output": {
                    "amansdsaxena": "land2"
                }
            },
            {
                "id": "94d04e12",
                "input": {
                    "address": "6545496d",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        53012783970614763388224069478103833104910280327665529485556180317800323971959,
                        82705319049675579555615803259353111713125991665274134726606276077985902015500
                    ],
                    "timestamp": 1665024630.5904686
                },
                "output": {
                    "amansdsaxena": "land1"
                }
            }
        ],
        "difficulty": 4,
        "hash": "02ca2f510e73688712d323171592a89b94d3a7b3c109b108ae763e1551dcce43",
        "last_hash": "genesis_hash",
        "nonce": 0,
        "timestamp": 1665024650.832157
    },
    {
        "data": [
            {
                "id": "eaf3ff85",
                "input": {
                    "address": "6545496d",
                    "amount": 1000,
                    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEse11YkhAtuxWof07DbuOzEdVAmwXhk9h\nS8doJonhYKa86dH+DdwfPvUwAtfc9pHJbgc6ExhljjQcCy12hyudyw==\n-----END PUBLIC KEY-----\n",
                    "signature": [
                        61811000501018983520234131876363830401011737395476025301834656897228061902398,
                        20827783997069955309229581425658805813162713766080027846233703922646931106725
                    ],
                    "timestamp": 1665029348.7631187
                },
                "output": {
                    "amansdsaxena": "land1"
                }
            }
        ],
        "difficulty": 5,
        "hash": "01d66b8f4dac5b204b1323fea9cc25686b79142092c7333e5e646da93c800d7c",
        "last_hash": "02ca2f510e73688712d323171592a89b94d3a7b3c109b108ae763e1551dcce43",
        "nonce": 0,
        "timestamp": 1665029380.872428
    }
]

print(chain)

