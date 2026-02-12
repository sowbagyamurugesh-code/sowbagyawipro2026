from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["C1"]

collection.insert_one({"name":"John","dept":"ECE","salary":70000})
result = collection.find_one({"name":"John"})
print(result)