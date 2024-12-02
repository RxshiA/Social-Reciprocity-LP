from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["adaptive_learning"]

# Example: Save progress
def save_progress(progress):
    db.child_progress.insert_one(progress.dict())

# Example: Retrieve progress
def get_progress(child_id):
    return db.child_progress.find_one({"child_id": child_id})
