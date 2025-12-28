import os
import runpod
from model_loader import load_model
from audio_utils import wav_to_base64

model = load_model()

SPEAKER_DIR = "/runpod-volume/speakers"  # 또는 ./speakers

LANG_SPEAKERS = {
    "ko": f"{SPEAKER_DIR}/ko.wav",
    "en": f"{SPEAKER_DIR}/en.wav",
    "ja": f"{SPEAKER_DIR}/ja.wav",
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
        top_p=0.85
    )

    return {
        "language": language,
        "audio": wav_to_base64(wav)
    }

runpod.serverless.start({"handler": handler})
