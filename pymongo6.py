from pymongo import MongoClient     # finding data
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll = mydb["dbtable"]

myquery = {"name":{"$regex":"^A"}}
#myquery = {"name":"jay"}

mydoc = mycoll.delete_many(myquery)
#mydoc = mycoll.delete_one(myquery)
for y in mycoll.find():
    print(y)
