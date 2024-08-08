from typing import Optional, Dict, List
from bson import ObjectId
from passlib.context import CryptContext
from pymongo import MongoClient
from .database import user_collection, chat_collection, message_collection
from .models import Message
from datetime import datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

client = MongoClient("mongodb://localhost:27017/")
db = client["chat_app"]
user_collection = db["users"]
MONGO_DETAILS = "mongodb://localhost:27017"


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"]
    }

async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def retrieve_user(email: str) -> Optional[dict]:
    user = await user_collection.find_one({"email": email})
    if user:
        return user_helper(user)
    return None

async def add_chat(chat_data: dict) -> dict:
    chat = await chat_collection.insert_one(chat_data)
    new_chat = await chat_collection.find_one({"_id": chat.inserted_id})
    return new_chat

async def retrieve_chat(chat_id: str) -> Optional[dict]:
    chat = await chat_collection.find_one({"_id": ObjectId(chat_id)})
    if chat:
        return chat
    return None

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def add_message(message_data: dict) -> dict:
    message = await message_collection.insert_one(message_data)
    new_message = await message_collection.find_one({"_id": message.inserted_id})
    return new_message

async def retrieve_messages(chat_id: str) -> List[dict]:
    messages = await message_collection.find({"chat_id": chat_id}).to_list(length=100)
    return messages

async def update_user_status(user_id: str, is_online: bool) -> None:
    await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"is_online": is_online}}
    )
def get_chats(user1: str, user2: str):
    chats = chat_collection.find({
        "$or": [
            {"$and": [{"sender": user1}, {"receiver": user2}]},
            {"$and": [{"sender": user2}, {"receiver": user1}]}
        ]
    }).sort("timestamp")
    return list(chats)
