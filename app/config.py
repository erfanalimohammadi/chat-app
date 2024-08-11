import socketio
from fastapi import FastAPI
from app.crud import create_message
from app.models import UserInDB, MessageInDB, ChatRoomInDB
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
ALGORITHM = "HS256"
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "chat_app")


sio = socketio.Server()
app = FastAPI()

@sio.on("join")
def join(sid, data):
    sio.enter_room(sid, data["room"])

@sio.on("message")
async def handle_message(sid, data):
    message = Message(**data)
    await create_message(message)
    sio.send(data, room=message.room_id)

app = socketio.ASGIApp(sio)
