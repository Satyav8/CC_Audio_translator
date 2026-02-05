from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.asr_service import audio_to_target_language
from app.db.database import get_connection

router = APIRouter(prefix="/api/v1/translate", tags=["Translation"])


@router.post("/{audio_id}")
async def translate_audio(audio_id: str, target_language: str):
    """
    Audio → Target-language text (no text-to-text translation)
    """
    audio_path = Path(f"data/audio/{audio_id}.wav")

    if not audio_path.exists():
        raise HTTPException(status_code=404, detail="Audio not found")

    # Audio → target language text
    translated_text = audio_to_target_language(audio_path, target_language)

    # Persist translation
    conn = get_connection()
    conn.execute(
        "INSERT INTO translations (audio_id, language, text) VALUES (?, ?, ?)",
        (audio_id, target_language, translated_text)
    )
    conn.execute(
        "INSERT INTO audit_logs (audio_id, action) VALUES (?, ?)",
        (audio_id, f"translated_to_{target_language}")
    )
    conn.commit()
    conn.close()

    return {
        "audio_id": audio_id,
        "target_language": target_language,
        "text": translated_text
    }

