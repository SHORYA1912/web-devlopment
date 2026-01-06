import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
engine.setProperty('rate', 150)
Translator = Translator()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak in English...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,  phrase_time_limit=5)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Network error")
    return ""

print("PLEASE CHOOSE A LANGUAGE")
print("1.HINDI,2.TAMIL,3.TELEGU,4.BENGALI")
print("5.MARATHI,6.GUJARATI,7.KANNADA,8.PUNJABI")

lang = int(input("ENTER THE OPTION BETWEEN 1TO8: "))

text = listen()
if text:
    translated = Translator.translate(text, dest=lang).text
    print("Translated text:", translated)
    speak(translated)

