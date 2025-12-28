from TTS.api import TTS
import torch

def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        progress_bar=False,
        gpu=device == "cuda"
    )

    return tts
