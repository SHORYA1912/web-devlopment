
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)

translator = Translator()

languages = {
    "1": "hi",
    "2": "ta",
    "3": "te",
    "4": "bn",
    "5": "mr",
    "6": "gu",
    "7": "ml",
    "8": "pa"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone(device_index=2) as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("🗣 You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("❌ API error:", e)
        return ""

print("\nCHOOSE LANGUAGE TO TRANSLATE:")
print("1.Hindi  2.Tamil  3.Telugu  4.Bengali")
print("5.Marathi  6.Gujarati  7.Malayalam  8.Punjabi")

choice = input("Enter choice (1-8): ")
LANG = languages.get(choice)

if not LANG:
    print("❌ Invalid choice")
    exit()

text = listen()

if text:
    translated = translator.translate(text, dest=LANG)
    print("🌍 Translated Text:", translated.text)
    speak(translated.text)


