from fastapi import APIRouter, HTTPException
from .crud import add_user, retrieve_user, add_chat, retrieve_chat, verify_password, get_chats, add_message, retrieve_messages
from .models import User, Chat, Message
from pydantic import BaseModel
from .auth import create_access_token, authenticate_user
from typing import List
from datetime import timedelta

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ChatCreate(BaseModel):
    sender: str
    receiver: str
    message: str

class ChatCreate(BaseModel):
    name: str
    users: List[str]

class MessageCreate(BaseModel):
    chat_id: str
    user_id: str
    message: str

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    db_user = await retrieve_user(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await add_user(user.dict())
    return new_user

@router.post("/chats/", response_model=Chat)
async def create_chat(chat: ChatCreate):
    new_chat = await add_chat(chat.dict())
    return new_chat

@router.get("/chats/{chat_id}", response_model=Chat)
async def get_chat(chat_id: str):
    chat = await retrieve_chat(chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

@router.post("/register")
async def register(user: UserCreate):
    await add_user(user.dict())
    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin):
    db_user = authenticate_user(user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/messages/")
async def create_message(message: MessageCreate):
    new_message = await add_message(message.dict())
    return new_message

@router.get("/messages/{chat_id}")
async def get_messages(chat_id: str):
    messages = await retrieve_messages(chat_id)
    return messages
