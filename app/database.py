# MongoDB connection setup for script-based usage
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URL)
db = client["todo_db"]
