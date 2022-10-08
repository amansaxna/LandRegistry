import hashlib
import pprint
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def merkle_root(data):
    """
    Return a sha-256 Merkel hash of input in the form of json serialized.
    """

    #taking pair from list1 hashing it and adding it to list2
        #if list1.size() == 1 then create pair with same txn
    list1 = data 

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
    print(list1)   
    return list1 #hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")

if __name__ == '__main__':
    main()
