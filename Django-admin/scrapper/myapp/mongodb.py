from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['indeed']  # Replace with your actual database name

# Access the MongoDB collection
collection = db['jobs']  # Replace with your collection name

def get_job_data():
    # Query data from the collection
    return collection.find({})

def get_job_search(query):
    return collection.find({"job_title": {"$regex": query}})
