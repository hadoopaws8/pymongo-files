from pymongo import MongoClient
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll = mydb["dbtable"]

mylist = [
    {"id":1,"name":"john","address":"Highway 37"},
    {"id":2,"name":"Peter","address":"Lowstreet 27"},
    {"id":3,"name":"Amy","address":"Apple st 652"},
    {"id":4,"name":"jay","address":"Chittoor 425"},
    {"id":5,"name":"love","address":"Dubai 897"},
]

x = mycoll.insert_many(mylist)

dblist = myclient.list_database_names()
if input('Enter DB') in dblist:
    print("The database exists.")
else:
    print("Not present")

print(dblist)
