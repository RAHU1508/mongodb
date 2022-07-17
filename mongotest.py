import pymongo
client = pymongo.MongoClient("mongodb+srv://RAHU1508:Rahul@1999#@rahu1508.g93ki.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
