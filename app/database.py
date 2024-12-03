import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = None
db = None


def initialize_db():
    global client, db
    if not os.getenv("TESTING"):
        client = MongoClient(os.getenv("MONGO_URI"), tls=True,
                             tlsAllowInvalidCertificates=True)
        db = client["adaptive_learning"]
    return db


def get_database():
    global db
    if db is None:
        initialize_db()
    return db


def save_progress(progress):
    database = get_database()
    if not database:
        return None
    return database.child_progress.insert_one(progress.model_dump())


def get_progress(child_id):
    database = get_database()
    if not database:
        return None
    return database.child_progress.find_one({"child_id": child_id})
