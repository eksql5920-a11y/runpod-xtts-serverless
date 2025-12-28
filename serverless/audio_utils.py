import base64
import io
import soundfile as sf

def wav_to_base64(wav, sample_rate=24000):
    buffer = io.BytesIO()
    sf.write(buffer, wav, sample_rate, format="WAV")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")
