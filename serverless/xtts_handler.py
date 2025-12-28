import base64
import os
import runpod

# ✅ 절대 경로 import (serverless 패키지 기준)
from serverless.model_loader import load_model
from serverless.audio_utils import wav_to_base64

# =========================
# 모델은 워커 시작 시 1번만 로드
# =========================
model = load_model()

# =========================
# speaker wav 경로 (안전한 방식)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SPEAKER_MAP = {
    "ko": os.path.join(BASE_DIR, "speakers", "ko.wav"),
    "en": os.path.join(BASE_DIR, "speakers", "en.wav"),
    "ja": os.path.join(BASE_DIR, "speakers", "ja.wav"),
}

# =========================
# RunPod handler
# =========================
def handler(event):
    input_data = event.get("input", {})

    text = input_data.get("text", "")
    language = input_data.get("language", "ko")

    if not text:
        return {
            "error": "text is required"
        }

    speaker_wav = SPEAKER_MAP.get(language)
    if not speaker_wav or not os.path.exists(speaker_wav):
        return {
            "error": f"speaker wav not found for language: {language}"
        }

    # XTTS TTS 실행
    wav = model.tts(
        text=text,
        language=language,
        speaker_wav=speaker_wav
    )

    audio_base64 = wav_to_base64(wav)

    return {
        "audio": audio_base64
    }

# =========================
# RunPod Serverless start
# =========================
runpod.serverless.start({
    "handler": handler
})
