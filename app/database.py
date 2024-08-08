from pymongo import MongoClient
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.chat_db

user_collection = database.get_collection("users_collection")
chat_collection = database.get_collection("chats_collection")
message_collection = database.get_collection("messages_collection")