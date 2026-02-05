from fastapi import FastAPI
from app.api.routes_audio import router as audio_router
from app.api.routes_normalize import router as normalize_router
from app.api.routes_translation import router as translation_router
from app.db.models import init_db

app = FastAPI(
    title="Hospital Multilingual ASR",
    version="0.6.0"
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(audio_router)
app.include_router(normalize_router)
app.include_router(translation_router)





