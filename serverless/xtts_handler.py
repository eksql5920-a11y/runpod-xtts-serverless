import os
import runpod

from .model_loader import load_model
from .audio_utils import wav_to_base64

# 모델 1회 로드 (장시간 송출 안정)
model = load_model()

BASE_DIR = os.path.dirname(__file__)
SPEAKER_DIR = os.path.join(BASE_DIR, "speakers")

LANG_SPEAKERS = {
    "ko": os.path.join(SPEAKER_DIR, "ko.wav"),
    "en": os.path.join(SPEAKER_DIR, "en.wav"),
    "ja": os.path.join(SPEAKER_DIR, "ja.wav"),
}

def handler(event):
    inp = event.get("input", {})

    text = inp.get("text")
    language = inp.get("language", "ko")

    if not text:
        return {"error": "text is required"}

    speaker_wav = LANG_SPEAKERS.get(language)

    wav = model.tts(
        text=text,
        language=language,
        speaker_wav=speaker_wav,
        temperature=0.7,
        repetition_penalty=5.0,
        top_k=50,
        top_p=0.85,
        length_penalty=1.0
    )

    return {
        "language": language,
        "audio": wav_to_base64(wav)
    }

runpod.serverless.start({"handler": handler})
