import base64
import runpod
from model_loader import load_model
from audio_utils import wav_to_base64

# 모델은 워커 시작 시 1번만 로드됨
model = load_model()

def handler(event):
    """
    event["input"] expects:
    {
        "text": "안녕하세요",
        "language": "ko",
        "speaker_wav": null
    }
    """
    input_data = event.get("input", {})

    text = input_data.get("text", "")
    language = input_data.get("language", "ko")
    speaker_wav = input_data.get("speaker_wav", None)

    if not text:
        return {"error": "text is required"}

    wav_path = model.tts(
        text=text,
        language=language,
        speaker_wav=speaker_wav
    )

    audio_base64 = wav_to_base64(wav_path)

    return {
        "audio": audio_base64
    }

runpod.serverless.start({"handler": handler})
