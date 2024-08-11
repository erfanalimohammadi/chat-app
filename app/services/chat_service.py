import socketio
from fastapi import FastAPI
from app.crud import create_message
from app.models import Message

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
