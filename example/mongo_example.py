from pymongo import MongoClient

# mongodb offline config
mongoConnection = 'mongodb://127.0.0.1:27017'
mongoDbName = 'testdb'

mgclient = MongoClient(mongoConnection)
mgdb = mgclient[mongoDbName]

records = mgdb.testcoll.find({}, {'field1': 1, 'field2': 1})
for r in records:
    print(r)

# add one
new_record = {"name": 'zhang0', 'age': 21}
mgdb.table2.insert(new_record)

# batch add
new_records = []
new_records.append({"name": 'zhang1', 'age': 22})
new_records.append({"name": 'zhang2', 'age': 23})
new_records.append({"name": 'zhang3', 'age': 24})
mgdb.table2.insert_many(new_records)

# find_one({"_id": ObjectId(id)})
record = mgdb.table2.find_one({"userId": 111})

# update one
ret = mgdb.table2.update_one(
    {"_id": record['_id']},
    {'$set': {
        'update_field': "new_val"
    }})

print ret

# update many
r = mgdb.table2.update({'field1': 'cond1'},
                       {
                           '$inc': {
                               'balance': 100,
                           },
                           '$set': {
                               'age': 333
                           }
                       }, upsert=False, multi=True)
print(r)

# remove
r = mgdb.table2.remove({'field1': 'cond1', 'field2': 'cond2'})
