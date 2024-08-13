from typing import List, Optional
from bson import ObjectId
from bson.json_util import dumps, loads
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorCollection
from passlib.context import CryptContext
from app.models import UserInDB, MessageInDB, ChatRoomInDB
from app.schemas import UserCreateSchema, MessageCreateSchema, ChatRoomCreateSchema, UserResponseSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def document_to_dict(doc) -> dict:
    """Converts MongoDB document to dictionary."""
    return loads(dumps(doc))

def user_from_doc(doc) -> UserInDB:
    """Converts MongoDB user document to Pydantic UserInDB model."""
    return UserInDB(**document_to_dict(doc))

def message_from_doc(doc) -> MessageInDB:
    """Converts MongoDB message document to Pydantic MessageInDB model."""
    return MessageInDB(**document_to_dict(doc))

def chat_room_from_doc(doc) -> ChatRoomInDB:
    """Converts MongoDB chat room document to Pydantic ChatRoomInDB model."""
    return ChatRoomInDB(**document_to_dict(doc))


async def create_user(db: AsyncIOMotorCollection, user: UserCreateSchema) -> UserResponseSchema:
    """Create a new user in the database."""
    user_dict = jsonable_encoder(user)
    user_dict['hashed_password'] = hash_password(user.password)  # Hash the password
    result = await db.insert_one(user_dict)
    return UserResponseSchema(**document_to_dict(await db.find_one({"_id": result.inserted_id})))

async def get_user_by_email(db: AsyncIOMotorCollection, email: str) -> Optional[UserResponseSchema]:
    """Get a user by email."""
    user = await db.find_one({"email": email})
    if user:
        return UserResponseSchema(**document_to_dict(user))
    return None

async def verify_user_password(db: AsyncIOMotorCollection, email: str, password: str) -> bool:
    """Verify a user's password."""
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return True
    return False


async def create_message(db: AsyncIOMotorCollection, room_id: str, message: MessageCreateSchema) -> MessageInDB:
    """Create a new message in a specific chat room."""
    message_dict = jsonable_encoder(message)
    await db.update_one(
        {"_id": ObjectId(room_id)},
        {"$push": {"messages": message_dict}}
    )
    room = await db.find_one({"_id": ObjectId(room_id)})
    message = next((msg for msg in room["messages"] if msg["_id"] == message_dict["_id"]), None)
    return message_from_doc(message) if message else None

async def get_messages(db: AsyncIOMotorCollection, room_id: str) -> List[MessageInDB]:
    """Get all messages in a specific chat room."""
    room = await db.find_one({"_id": ObjectId(room_id)})
    if room and "messages" in room:
        return [message_from_doc(msg) for msg in room["messages"]]
    return []


async def create_chat_room(db: AsyncIOMotorCollection, chat_room: ChatRoomCreateSchema) -> ChatRoomInDB:
    """Create a new chat room."""
    chat_room_dict = jsonable_encoder(chat_room)
    result = await db.insert_one(chat_room_dict)
    return chat_room_from_doc(await db.find_one({"_id": result.inserted_id}))

async def get_chat_room_by_id(db: AsyncIOMotorCollection, room_id: str) -> Optional[ChatRoomInDB]:
    """Get a chat room by its ID."""
    room = await db.find_one({"_id": ObjectId(room_id)})
    if room:
        return chat_room_from_doc(room)
    return None
