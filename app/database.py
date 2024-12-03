from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB with SSL certificate verification disabled
client = MongoClient(os.getenv("MONGO_URI"), tls=True, tlsAllowInvalidCertificates=True)
db = client["adaptive_learning"]
print("Connected to MongoDB:" + str(db))

# Example: Save progress
def save_progress(progress):
    db.child_progress.insert_one(progress.model_dump())

# Example: Retrieve progress
def get_progress(child_id):
    return db.child_progress.find_one({"child_id": child_id})

# Close MongoDB connection
def close_connection():
    client.close()