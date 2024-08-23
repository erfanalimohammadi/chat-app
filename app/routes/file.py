from fastapi import APIRouter, File, UploadFile, HTTPException
from App.models.file import File, FileInDB
from App.config.database import get_files_collection
from App.utils.object_id import PydanticObjectId
import aiofiles

router = APIRouter()

@router.post("/upload")
async def upload_file(room_id: str, room_type: str, user_id: str, file: UploadFile = File(...)):
    files_collection = get_files_collection()
    
    try:
        # Save file to disk or cloud storage
        file_location = f"files/{file.filename}"
        async with aiofiles.open(file_location, 'wb') as f:
            content = await file.read()
            await f.write(content)

        # Create file metadata
        file_metadata = File(
            user_id=PydanticObjectId(user_id),
            room_id=PydanticObjectId(room_id),
            room_type=room_type,
            filename=file.filename,
            file_type=file.content_type,
            file_url=file_location
        )
        file_dict = file_metadata.model_dump(by_alias=True)

        # Save file metadata to database
        result = await files_collection.insert_one(file_dict)
        file_dict["_id"] = result.inserted_id
        
        return FileInDB(**file_dict)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{file_id}")
async def download_file(file_id: str):
    files_collection = get_files_collection()
    file_metadata = await files_collection.find_one({"_id": PydanticObjectId(file_id)})

    if file_metadata:
        file_path = file_metadata['file_url']
        return FileResponse(file_path, media_type=file_metadata['file_type'], filename=file_metadata['filename'])
    
    raise HTTPException(status_code=404, detail="File not found")
