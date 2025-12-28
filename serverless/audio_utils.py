import base64
import io
import soundfile as sf

def wav_to_base64(wav, sample_rate=24000):
    buf = io.BytesIO()
    sf.write(buf, wav, sample_rate, format="WAV")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
