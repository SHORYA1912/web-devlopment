import speech_recognition as sr
import pyttsx3
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine. say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("listening...")
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"user said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
    except sr.RequestError:
        print("SORRY, API ERROR")
        return ""

def respond_to_command(command):
    if 'time' in command:
        strTime = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'date' in command:
        strDate = datetime.now().strftime("%d-%m-%Y")
        speak(f"Today's date is {strDate}")
    elif 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'exit' in command or quit in command:
        speak("GOODBYE!")
        exit()
    else:
        speak("I am sorry, I don't understand that command.")
        return True
    
def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        
        command = get_audio()
        if not respond_to_command(command):
                break

if __name__ == "__main__":
    main()

