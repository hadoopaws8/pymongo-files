from pymongo import MongoClient     # finding data
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll = mydb["dbtable"]


##x = mycoll.find_one()
##print(x)

# find many documents in given belllow
for x in mycoll.find():
    print(x)
