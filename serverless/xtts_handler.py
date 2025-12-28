import runpod
from model_loader import load_model
from audio_utils import wav_to_base64

# 워커 시작 시 1회 로드 (⭐ 1시간 송출 핵심)
model = load_model()

# 언어별 기본 화자 (없으면 None)
DEFAULT_SPEAKERS = {
    "ko": None,
    "en": None,
    "ja": None,
}

def handler(event):
    """
    event["input"] =
    {
        "text": "Hello world",
        "language": "en",   # ko | en | ja
        "speaker_wav": null
    }
    """

    inp = event.get("input", {})

    text = inp.get("text")
    language = inp.get("language", "ko")
    speaker_wav = inp.get("speaker_wav", DEFAULT_SPEAKERS.get(language))

    if not text:
        return {"error": "text is required"}

    # ⭐ 안정성 + 발음 품질 핵심 옵션
    wav = model.tts(
        text=text,
        language=language,
        speaker_wav=speaker_wav,
        temperature=0.7,          # 자연스러움
        length_penalty=1.0,
        repetition_penalty=5.0,   # 장시간 반복 방지
        top_k=50,
        top_p=0.85
    )

    audio_base64 = wav_to_base64(wav)

    return {
        "language": language,
        "audio": audio_base64
    }

# ⭐⭐⭐ RunPod 필수
runpod.serverless.start({"handler": handler})
