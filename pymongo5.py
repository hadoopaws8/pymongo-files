from pymongo import MongoClient     # finding data
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll = mydb["dbtable"]

mydoc = mycoll.find().sort('name',1) #ascending order sorting
#mydoc = mycoll.find().sort('name',-1)#descending order sorting
for x in mydoc:
    print(x)
