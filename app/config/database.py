from typing import AsyncIterator
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from fastapi import Depends
from pymongo import MongoClient

DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "chat_app"

client = AsyncIOMotorClient(DATABASE_URL)
database = client[DATABASE_NAME]

def get_db() -> AsyncIterator[AsyncIOMotorDatabase]:
    try:
        yield database
    finally:
        client.close()
