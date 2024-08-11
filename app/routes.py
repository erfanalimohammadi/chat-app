from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreateSchema, UserResponseSchema, MessageCreateSchema, MessageInDB
from app.crud import create_user, get_user_by_email, create_message, get_messages
from app.database import get_db

router = APIRouter()

@router.post("/users/", response_model=UserResponseSchema)
async def register_user(user: UserCreateSchema, db=Depends(get_db)):
    existing_user = await get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db, user)

@router.post("/messages/", response_model=MessageInDB)
async def post_message(room_id: str, message: MessageCreateSchema, db=Depends(get_db)):
    return await create_message(db, room_id, message)

@router.get("/messages/{room_id}", response_model=List[MessageInDB])
async def fetch_messages(room_id: str, db=Depends(get_db)):
    return await get_messages(db, room_id)
