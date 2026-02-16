import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os

# Load Whisper once (important for performance)
model = whisper.load_model("base")

def listen_to_user(duration=5):
    print(f"🎙 Listening for {duration} seconds...")

    samplerate = 16000
    channels = 1

    # Record audio for fixed duration
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=channels,
        dtype="int16"
    )
    sd.wait()  # wait until recording is finished

    # Save to temp wav file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        wav.write(tmp.name, samplerate, recording)
        audio_path = tmp.name

    print("🧠 Transcribing...")
    result = model.transcribe(audio_path)

    os.remove(audio_path)

    text = result["text"].strip()
    print(f"🗣 You said: {text}")

    return text if text else None
