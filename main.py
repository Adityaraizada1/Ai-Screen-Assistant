from pynput import keyboard
from screen import take_screenshot
from vision import analyze_screen
from voice import listen_to_user
from state_manager import is_safe
from speaker import speak
from floating_window import FloatingWindow
import threading

# ==============================
# Initialize UI (MAIN THREAD)
# ==============================
ui = FloatingWindow()

print("""
====================================
AI Screen Assistant (FINAL)
------------------------------------
Press CTRL + OPTION + A → Speak & Analyze
Press ESC               → Quit
====================================
""")

current_keys = set()
busy = False


def analyze():
    global busy
    if busy:
        return

    busy = True

    try:
        ui.show_text("📸 Capturing screen...")
        image_path = take_screenshot()

        ui.show_text("🎙 Listening for 5 seconds...")
        user_instruction = listen_to_user()

        ui.show_text("🧠 Transcribing complete.\n\nThinking...")
        
        if not user_instruction:
            user_instruction = "Explain what this screen is showing."

        response = analyze_screen(image_path, user_instruction)

        # Show final response
        ui.show_text("🤖 AI RESPONSE:\n\n" + response)

        if not is_safe(response):
            print("🚫 Exam/graded content detected.")

    finally:
        busy = False


def analyze_async():
    threading.Thread(target=analyze, daemon=True).start()


def on_press(key):
    current_keys.add(key)

    if (
        (keyboard.Key.ctrl_l in current_keys or keyboard.Key.ctrl_r in current_keys)
        and (keyboard.Key.alt_l in current_keys or keyboard.Key.alt_r in current_keys)
        and hasattr(key, "char")
        and key.char == "a"
    ):
        analyze_async()

    if key == keyboard.Key.esc:
        print("👋 Exiting assistant")
        ui.root.quit()
        return False


def on_release(key):
    if key in current_keys:
        current_keys.remove(key)


# Keyboard listener runs in background
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# ==============================
# START TKINTER MAIN LOOP
# ==============================
ui.run()
