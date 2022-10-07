"""
way 1 : explicitly have a place where miners tell there interusted stake for a mining process
way 2 : go though the tranx_pool and knw who is the max_staker for that set of transaction

"""
#way 1 ->
stackers = {  
                "aman"  : 1 ,
                "manas" : 2 ,
                "chirag" : 0,
                "sahitya" : 5
           }


"""
during mining -> first check if the requester(mining) has the max stake or not
"""
address = "sahitya" # wallet.address

#find max_stackere
max_stacker = ""
max_stake = 0
for pair in stackers :
    print(f'{pair} : {stackers[pair]}')
    if max_stake < stackers[pair] :
        max_stake = stackers[pair] 
        max_stacker = pair

if max_stacker != address :
    print("can't do the mining")
else :
    print("mining done")

#way 2 ->

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

# if in the out of the transactin , 
# just findou twhich wa;let address appers the majority time

# if notr present in the count add 
# else add the count
count = dict() 
# { 
#     "aman" : 1,
#     "manas" : 1
# }

# populate the count
    # if notr present in the count add 
    # else add the count

# print(count["aman"])
# count["aman"] += 1 
# print(count["manas"])

# if count.get("sahitya") == None:
#     count["sahitya"] = 1 # adding 
#     print("successfully added sahitya")
#     print(count["sahitya"])

# print(count)

for trnsx in trnsx_pool :
    # address = count.get(trnsx["output"]["name_owner"])
    if count.get(trnsx["output"]["name_owner"]) == None:
        count[trnsx["output"]["name_owner"]] = 1
    else :
        count[trnsx["output"]["name_owner"]] += 1

print(count)

address = "aman" # wallet.address

#find max_stackere
max_stacker = ""
max_stake = 0
for pair in count :
    print(f'{pair} : {stackers[pair]}')
    if max_stake < stackers[pair] :
        max_stake = stackers[pair] 
        max_stacker = pair

if max_stacker != address :
    print("aman can't do the mining")
else :
    print("  mining done")