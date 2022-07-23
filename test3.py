import pymongo
client = pymongo.MongoClient("mongodb+srv://RAHU1508:mongodb123@rahu1508.g93ki.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
db1 = client['mongotest']
coll = db1['test2']
data1 = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
coll.insert_many(data1)
#record = coll.find({'companyName':'iNeuron'})
record = coll.find({'courseOffered':{'$gt':'E'}})
for i in record:
    print(i)