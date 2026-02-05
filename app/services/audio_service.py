import uuid
from pathlib import Path
from app.utils.audio_utils import normalize_audio
from app.utils.hashing import sha256_file
from app.db.database import get_connection

AUDIO_DIR = Path("data/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


def process_uploaded_audio(upload_file):
    """
    Handles audio upload, normalization, hashing, and persistence.
    """
    audio_id = str(uuid.uuid4())

    raw_path = AUDIO_DIR / f"{audio_id}_raw"
    normalized_path = AUDIO_DIR / f"{audio_id}.wav"

    # Save raw upload
    with open(raw_path, "wb") as f:
        f.write(upload_file.file.read())

    # Normalize audio (mono, 16kHz, wav)
    normalize_audio(raw_path, normalized_path)

    # Hash normalized audio (audit integrity)
    file_hash = sha256_file(normalized_path)

    # Cleanup raw file
    raw_path.unlink(missing_ok=True)

    # Persist to DB
    conn = get_connection()
    conn.execute(
        "INSERT INTO audio_records (id, file_path) VALUES (?, ?)",
        (audio_id, str(normalized_path))
    )
    conn.execute(
        "INSERT INTO audit_logs (audio_id, action) VALUES (?, ?)",
        (audio_id, "audio_uploaded")
    )
    conn.commit()
    conn.close()

    return {
        "audio_id": audio_id,
        "file_path": str(normalized_path),
        "hash": file_hash
    }


