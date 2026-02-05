from fastapi import APIRouter, UploadFile, File
from app.services.audio_service import process_uploaded_audio

router = APIRouter(prefix="/api/v1/audio", tags=["Audio"])


@router.post("/upload")
async def upload_audio(audio_file: UploadFile = File(...)):
    result = process_uploaded_audio(audio_file)

    return {
        "audio_id": result["audio_id"],
        "status": "processed",
        "hash": result["hash"]
    }

