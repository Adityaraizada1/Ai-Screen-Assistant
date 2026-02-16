import os
import shlex

def speak(text):
    if not text:
        return

    # Escape text safely for shell
    safe_text = shlex.quote(text)

    print("🔊 Speaking response...")
    os.system(f"say {safe_text}")
