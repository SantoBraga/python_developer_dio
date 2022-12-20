from pymongo import MongoClient
from src.secrets import MONGO_DB

client = MongoClient(MONGO_DB)

db = client.app_twitter

trends_collection = db.tweets
