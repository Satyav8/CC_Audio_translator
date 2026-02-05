

# 🏥 Multilingual Clinical Audio-to-Text Engine

> **A hospital-grade backend that converts spoken clinical audio in *any language* into accurate, auditable medical text — fully offline, privacy-first, and production-ready.**

---

## ✨ What This Is

This project is a **multilingual clinical ASR (Automatic Speech Recognition) system** designed for hospitals and healthcare providers.

It allows doctors, nurses, and patients to **speak naturally in any language**, while the system reliably produces:

* **Canonical English medical text** for clinical records
* **Native-language text output** for patient communication
* **Full audit trails** for medico-legal trust

All without cloud dependencies or external APIs.

---

## 🧠 Core Capabilities

### 🎙️ Audio → Medical Text (Any Language)

* Accepts real-world hospital audio (noise, accents, interruptions)
* Supports multilingual speech automatically
* No manual language selection required

### 🇬🇧 Canonical English (Clinical-Safe)

* Produces clean, professional English
* Removes filler speech
* Normalizes terminology
* Designed for EHR / documentation workflows

### 🌍 Native-Language Output (From Audio)

* Same audio → text in Hindi, Telugu, Tamil, etc.
* No text-to-text translation (prevents semantic drift)
* Output is always traceable to the original audio

### 🧾 Audit-First Architecture

* Every audio upload is logged
* Every transcription is persisted
* Every translation is traceable
* Built for compliance, not demos

---

## 🏗️ Architecture (High-Level)

```
Audio (any language)
   ↓
FFmpeg normalization (mono / 16kHz)
   ↓
Whisper ASR
   ├── English (canonical)
   └── Target language (direct from audio)
   ↓
Medical normalization
   ↓
SQLite persistence + audit logs
```

**Key principle:**

> English is the *single source of clinical truth*.
> Other languages are derived, not re-interpreted.

---

## 🔒 Privacy by Design

* Fully **offline**
* No external APIs
* No cloud dependency
* All data stored locally (SQLite)
* Suitable for on-prem hospital deployment

---

## 🧱 Tech Stack

* **Python 3.11+**
* **FastAPI** – clean, async REST APIs
* **Whisper (large-v3)** – multilingual speech recognition
* **FFmpeg** – audio normalization
* **SQLite** – lightweight, auditable persistence

---

## 🚀 API Overview

### Upload Audio

```
POST /api/v1/audio/upload
```

### Canonical English (Medical)

```
POST /api/v1/normalize/{audio_id}
```

### Native-Language Output (Audio → Text)

```
POST /api/v1/translate/{audio_id}?target_language=hi
```

No request bodies.
No ambiguity.
No hidden behavior.

---

## 🧪 Why Hospitals Trust This

* Deterministic outputs
* Human-in-the-loop friendly
* Clear failure modes
* Transparent audit logs
* No hallucination from text translation
* Designed for pilots, not pitch decks

---

## ⚠️ What This Is *Not*

* ❌ Not a chatbot
* ❌ Not a demo toy
* ❌ Not a cloud-only AI service
* ❌ Not real-time conversational translation (yet)

This is a **clinical backend foundation**.

---

## 🛣️ Roadmap (Post-Pilot)

* Authentication & role-based access
* Confidence scoring UI
* Streaming ASR
* HL7 / FHIR integration
* PostgreSQL upgrade
* On-prem Docker deployment

---

## 🏁 Status

✅ Feature-complete for pilot
✅ Hospital-grade architecture
✅ Internship + enterprise credible

---

## 👨‍⚕️ Final Word

This system doesn’t try to *replace doctors*.
It removes friction, paperwork, and language barriers — **safely**.

That’s how clinical AI earns trust.

---

