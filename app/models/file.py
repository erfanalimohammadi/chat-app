from datetime import datetime
from pydantic import BaseModel, Field
from App.utils.object_id import PydanticObjectId

class File(BaseModel):
    user_id: PydanticObjectId
    room_id: PydanticObjectId
    room_type: str
    filename: str
    file_type: str
    file_url: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())

class FileInDB(File):
    id: PydanticObjectId = Field(alias="_id", serialization_alias="id")
