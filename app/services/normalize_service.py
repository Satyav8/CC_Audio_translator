import re

MEDICAL_SYMPTOMS = [
    "chest pain",
    "fever",
    "headache",
    "shortness of breath",
    "cough",
    "nausea",
    "vomiting",
    "dizziness",
    "fatigue",
    "abdominal pain"
]

def normalize_medical_text(text: str):
    canonical = text.strip().capitalize()

    entities = {
        "symptoms": [],
        "duration": [],
        "medications": [],
        "dosages": []
    }

    flags = []

    text_lower = canonical.lower()

    # ---- Symptom extraction ----
    for symptom in MEDICAL_SYMPTOMS:
        if symptom in text_lower:
            entities["symptoms"].append(symptom)

    # ---- Duration extraction ----
    durations = re.findall(
        r"\b\d+\s+(day|days|week|weeks|month|months)\b",
        text_lower
    )
    entities["duration"] = durations

    # ---- Safety flags ----
    if "pain" in text_lower and not entities["duration"]:
        flags.append("pain mentioned without duration")

    if not entities["symptoms"]:
        flags.append("no recognizable symptoms extracted")

    return {
        "canonical_english": canonical,
        "entities": entities,
        "flags": flags
    }
