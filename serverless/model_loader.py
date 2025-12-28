from TTS.api import TTS

def load_model():
    # XTTS v2
    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        progress_bar=False,
        gpu=True
    )
    return tts
