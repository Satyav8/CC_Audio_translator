from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.asr_service import audio_to_english
from app.services.normalize_service import normalize_medical_text
from app.db.database import get_connection

router = APIRouter(prefix="/api/v1/normalize", tags=["Normalization"])


@router.post("/{audio_id}")
async def normalize(audio_id: str):
    """
    Audio → English → Medical normalization
    """
    audio_path = Path(f"data/audio/{audio_id}.wav")

    if not audio_path.exists():
        raise HTTPException(status_code=404, detail="Audio not found")

    # Audio → English (canonical)
    english_text = audio_to_english(audio_path)

    # Medical normalization
    normalized = normalize_medical_text(english_text)

    # Persist canonical English
    conn = get_connection()
    conn.execute(
        "INSERT INTO canonical_texts (audio_id, text) VALUES (?, ?)",
        (audio_id, normalized["canonical_english"])
    )
    conn.execute(
        "INSERT INTO audit_logs (audio_id, action) VALUES (?, ?)",
        (audio_id, "normalized_to_english")
    )
    conn.commit()
    conn.close()

    return {
        "audio_id": audio_id,
        "canonical_output": normalized
    }


