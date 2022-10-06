"""
handels bidding processes 

"""

sales = { 
            "p1" :   [ ('bidder1' , 10 ), ('bidder2' , 15 ) ] ,
            "p2" :   [ ('bidder1' , 10 ) ] 
        }

print(sales)

# add a bidder
new_bid = ('bidder3',30)
sales['p1'].append(new_bid)
print(sales)

# add a property for listring
sales["p3"] = []

print(sales)

# during transaction 
# 1. find out the max bidder

max_bid = 0
max_bidder = ""
for bid in sales["p1"] :
    if(bid[1] >  max_bid )  : 
        max_bid = bid[1]
        max_bidder = bid[0]

print(max_bid, max_bidder)

