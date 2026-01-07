import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import pyttsx3
import datetime

# Load Vosk model
model = Model("model")
recogniser = KaldiRecognizer(model, 16000)

# Queue for audio data
audio_queue = queue.Queue()

# Text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Callback function (FIXED)
def callback(indata, frames, time, status):
    if status:
        print(status)
    # Convert float32 → int16 for Vosk
    audio_queue.put((indata * 32767).astype("int16").tobytes())

# Query processing
def process_query(query):
    query = query.lower()

    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}"

    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    else:
        return "I am sorry, I cannot understand that."

print("🎙️ Listening...")

with sd.InputStream(          # 🔥 InputStream (not RawInputStream)
    samplerate=16000,
    blocksize=8000,
    dtype="float32",
    channels=1,
    device=40,                # Bluetooth mic index
    callback=callback
):
    while True:
        data = audio_queue.get()

        if recogniser.AcceptWaveform(data):
            results = json.loads(recogniser.Result())
            text = results.get("text", "")

            if text:
                print(f"You said: {text}")
                response = process_query(text)
                print(f"Assistant: {response}")
                speak(response)
