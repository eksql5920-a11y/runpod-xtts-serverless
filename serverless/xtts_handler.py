import base64
import runpod
import os

# 절대 경로 import로 변경
from serverless.model_loader import load_model
from serverless.audio_utils import wav_to_base64

# 모델은 워커 시작 시 1번만 로드
model = load_model()

SPEAKER_MAP = {
    "ko": "serverless/speakers/ko.wav",
    "en": "serverless/speakers/en.wav",
    "ja": "serverless/speakers/ja.wav",
}

def handler(event):
    input_data = event.get("input", {})

    text = input_data.get("text", "")
    language = input_data.get("language", "ko")

    if not text:
        return {"error": "text is required"}

    speaker_wav = SPEAKER_MAP.get(language)

    wav = model.tts(
        text=text,
        language=language,
        speaker_wav=speaker_wav
    )

    audio_base64 = wav_to_base64(wav)

    return {
        "audio": audio_base64
    }

runpod.serverless.start({"handler": handler})
