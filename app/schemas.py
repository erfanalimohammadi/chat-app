from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserBaseSchema(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreateSchema(UserBaseSchema):
    password: str

class UserResponseSchema(UserBaseSchema):
    id: str

class MessageBaseSchema(BaseModel):
    sender: str
    content: str
    timestamp: datetime

class MessageCreateSchema(MessageBaseSchema):
    pass

class MessageResponseSchema(MessageBaseSchema):
    id: str

class ChatRoomBaseSchema(BaseModel):
    name: str
    members: List[str]

class ChatRoomCreateSchema(ChatRoomBaseSchema):
    pass

class ChatRoomResponseSchema(ChatRoomBaseSchema):
    id: str
    messages: List[MessageResponseSchema]

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    email: str
