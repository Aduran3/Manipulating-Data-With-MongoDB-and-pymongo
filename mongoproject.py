import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://aduran3:2ZJM1QViWH1UqBeX@cluster0.pbk8d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["project"]
collection = db["project"]

post = {"_id": "0", "name": "aaron", "grade": "90"}
post1 = {"_id": "1", "name": "billy", "grade": "75"}
post2 = {"_id": "2", "name": "john", "grade": "85"}
post3 = {"_id": "3", "name": "bill", "grade": "67"}
post4 = {"_id": "4", "name": "ariel", "grade": "94"}
post5 = {"_id": "5", "name": "joe", "grade": "100"}

collection.insert([post])
collection.insert([post1, post2, post3, post4, post5])

results = collection.find({"name": "joe"})

for result in results:
	print(result)

action = collection.delete_one({"_id": "0"})

collection.update_one({"_id": "4"}, {"$set": {"grade": "90"}})
