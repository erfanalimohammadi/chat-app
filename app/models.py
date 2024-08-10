from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: EmailStr
    password: str
    is_online: bool = False 

class Chat(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    participants: list[str]
    messages: list[dict]

class Message(BaseModel):
    chat_id: str
    user_id: str
    message: str
    timestamp: Optional[str] = None
