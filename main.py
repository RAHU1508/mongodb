import pymongo
client = pymongo.MongoClient("mongodb+srv://RAHU1508:mongodb123@rahu1508.g93ki.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {'name':'rahul', 'surname':'kumar'}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)