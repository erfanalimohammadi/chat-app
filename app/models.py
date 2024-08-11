from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class MessageBase(BaseModel):
    sender: str
    content: str
    timestamp: datetime

class MessageInDB(MessageBase):
    id: str

class ChatRoomBase(BaseModel):
    name: str
    members: List[str]

class ChatRoomInDB(ChatRoomBase):
    id: str
    messages: List[MessageInDB]

class UserInDB(BaseModel):
    email: str
    hashed_password: str
    full_name: Optional[str] = None

class MessageInDB(BaseModel):
    _id: str
    content: str
    sender: str
    timestamp: str

class ChatRoomInDB(BaseModel):
    _id: str
    name: str
    messages: List[MessageInDB]
