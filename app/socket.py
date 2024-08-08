import socketio
from fastapi import FastAPI
from aiohttp import web
from app.crud import update_user_status, add_message
from datetime import datetime
from app.routes import router

sio = socketio.AsyncServer()
app = FastAPI()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    print(f"User connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"User disconnected: {sid}")
    await update_user_status(sid, False)
    await sio.emit('user_status', {'user_id': sid, 'status': 'offline'})

@sio.event
async def message(sid, data):
    print(f"Message from {sid}: {data}")
    chat_id = data['chat_id']
    user_id = data['user_id']
    message_text = data['message']

    message_data = {
        "chat_id": chat_id,
        "user_id": user_id,
        "message": message_text,
        "timestamp": str(datetime.utcnow())
    }
    await add_message(message_data)
    
    await sio.emit('new_message', message_data, room=chat_id)

@sio.event
async def user_online(sid):
    print(f"User online: {sid}")
    await update_user_status(sid, True)
    await sio.emit('user_status', {'user_id': sid, 'status': 'online'})

@app.get('/')
async def index():
    return {"message": "Socket.IO Server Running"}

app.include_router(router)
app = socketio.ASGIApp(sio, other_asgi_app=app)
