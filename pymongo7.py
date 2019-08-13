from pymongo import MongoClient     # finding data
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll = mydb["dbtable"]

#mycoll.drop() #drop collection
#democlient.drop_database("demo")  #for droping the db
#print(myclient.list_database_names())

#myquery = {"name":"john"}
#newvalues = {"$set":{"name":"andrew"}}

myquery = {"address":{"$regex":"^D"}}
newvalues = {"$set": {"address":"Mansion Street 105"}}

#mycoll.update_one(myquery,newvalues)
#mycoll.update_many(myquery,newvalues)
for y in mycoll.find():
    print(y)
