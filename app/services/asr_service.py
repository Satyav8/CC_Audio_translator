import whisper
from pathlib import Path

MODEL = whisper.load_model("large-v3")


def audio_to_english(audio_path: Path) -> str:
    """
    Audio → English text (canonical)
    """
    result = MODEL.transcribe(
        str(audio_path),
        task="translate",   # ALWAYS English
        fp16=False
    )
    return result.get("text", "").strip()


def audio_to_target_language(audio_path: Path, target_language: str) -> str:
    """
    Audio → Target language text
    """
    result = MODEL.transcribe(
        str(audio_path),
        task="transcribe",  # <-- KEY FIX
        language=target_language,
        fp16=False
    )
    return result.get("text", "").strip()




