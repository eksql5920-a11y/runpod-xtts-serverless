import torch
from TTS.api import TTS

_model = None

def load_model():
    global _model
    if _model is None:
        _model = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2",
            progress_bar=False,
            gpu=torch.cuda.is_available()
        )
    return _model
