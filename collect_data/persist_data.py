from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Insert a single document
document = {"name": "Alice", "age": 30, "city": "New York"}
collection.insert_one(document)

# Insert multiple documents
documents = [
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 28, "city": "Miami"}
]
collection.insert_many(documents)

# Query and print the inserted documents
for doc in collection.find():
    print(doc)

# Close the connection
client.close()
