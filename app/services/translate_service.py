import whisper

MODEL = whisper.load_model("large-v3")

def translate_english_text(english_text: str, target_language: str) -> str:
    """
    Translates canonical English into the target language.
    """
    result = MODEL.transcribe(
        english_text,
        task="translate",
        language=target_language,
        fp16=False
    )

    return result.get("text", "").strip()
