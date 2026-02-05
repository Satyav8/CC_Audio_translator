from app.db.database import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Audio records
    cur.execute("""
    CREATE TABLE IF NOT EXISTS audio_records (
        id TEXT PRIMARY KEY,
        file_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # English canonical text
    cur.execute("""
    CREATE TABLE IF NOT EXISTS canonical_texts (
        audio_id TEXT,
        text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Target language outputs
    cur.execute("""
    CREATE TABLE IF NOT EXISTS translations (
        audio_id TEXT,
        language TEXT,
        text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Audit logs
    cur.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_id TEXT,
        action TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
