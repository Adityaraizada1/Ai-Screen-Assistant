# 🤖 AI Screen Assistant: Vision & Voice Powered Intelligence

An advanced, real-time AI assistant that "sees" your screen and "hears" your voice to provide intelligent context-aware support. Built with the powerful **Qwen2-VL** vision model and **OpenAI Whisper**, this tool bridges the gap between your desktop and state-of-the-art AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Transformers](https://img.shields.io/badge/Powered%20By-Transformers-orange?style=for-the-badge)
![Vision](https://img.shields.io/badge/Vision-Qwen2--VL-red?style=for-the-badge)
![Voice](https://img.shields.io/badge/Voice-Whisper-green?style=for-the-badge)

---

## ✨ Features

- 🎹 **Global Hotkey:** Trigger the assistant from anywhere with `Ctrl + Option + A`.
- 📸 **Instant Vision:** Captures your active screen and processes it with high-precision vision-language models.
- 🎙️ **Voice Interaction:** Speak your instructions naturally; powered by OpenAI's Whisper for robust transcription.
- 🧠 **Contextual Intelligence:** Uses Qwen2-VL to understand complex UI, text, and visual elements.
- 🗂️ **Floating Dashboard:** A premium, non-intrusive UI built with CustomTkinter for real-time feedback.
- 🔊 **Voice Feedback:** Seamlessly speaks back the AI response (optimised for macOS).
- 🛡️ **Safety Guard:** Built-in filters to prevent misuse in academic or sensitive contexts.

---

## 🚀 How It Works

1. **Trigger:** Press `Ctrl + Option + A`.
2. **Vision:** The system takes a high-quality screenshot via `mss`.
3. **Voice:** The assistant listens for 5 seconds to capture your request.
4. **Processing:**
   - **Speech-to-Text:** Whisper transcribes your audio into text.
   - **Vision-Language Model:** Qwen2-VL analyzes the image based on your text prompt.
5. **Response:** The AI's insight is displayed in a floating window and read aloud.

---

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- macOS (for `say` command support and specific keyboard bindings)
- A reasonably capable CPU/GPU (runs on CPU by default)

### Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd llm-model
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Required System Libraries (macOS):**
   ```bash
   brew install portaudio
   ```

---

## 📖 Usage

1. **Start the application:**
   ```bash
   python main.py
   ```
2. **Invoke the Assistant:**
   - Press `Ctrl + Option + A`.
   - Wait for the "Listening" prompt in the floating window.
   - Speak your question (e.g., *"Explain this code snippet"* or *"What is happening in this graph?"*).
   - View the AI's response in the dashboard and hear it via your speakers.
3. **Exit:**
   - Press `Esc` or close the window.

---

## 🏗️ Project Structure

- `main.py`: The entry point and application orchestrator.
- `vision.py`: Vision-Language Model (Qwen2-VL) integration.
- `voice.py`: Audio recording and Whisper transcription.
- `floating_window.py`: CustomTkinter-based UI implementation.
- `speaker.py`: Text-to-Speech (TTS) engine.
- `screen.py`: Screen capture utility.
- `state_manager.py`: Safety filters and state handling.

---

## 🛠️ Tech Stack

- **AI Models:** Qwen2-VL-2B-Instruct, OpenAI Whisper (Base)
- **UI Framework:** CustomTkinter
- **Core Libraries:** PyTorch, Transformers, Pynput, SoundDevice
- **Automation/Vision:** mss, PIL (Pillow)

---

> [!NOTE]
> The first run may take some time as the models (Qwen2-VL and Whisper) are downloaded to your local cache.

---

## 📄 License
MIT License - Created for innovative vision-voice interactions.
