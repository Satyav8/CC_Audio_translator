import os
import ffmpeg
from pathlib import Path

# ---- FORCE FFmpeg visibility (Windows-safe) ----
FFMPEG_BIN_PATH = r"C:\ffmpeg\ffmpeg-2026-02-04-git-627da1111c-full_build\bin"
os.environ["PATH"] += os.pathsep + FFMPEG_BIN_PATH


def normalize_audio(input_path: Path, output_path: Path):
    try:
        (
            ffmpeg
            .input(str(input_path))
            .output(
                str(output_path),
                ac=1,          # mono
                ar=16000,      # 16kHz
                format="wav"
            )
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        raise RuntimeError(
            f"FFmpeg failed:\n{e.stderr.decode()}"
        )


