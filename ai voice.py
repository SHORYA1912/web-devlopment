import pyaudio, numpy as np , speech_recognition as sr
import matplotlib.pyplot as plt

RATE = 16000
CHUNK = 1024

def record_sounds(seconds):
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16,channels = 1 ,rate = RATE , input = True, frames_per_buffer = CHUNK)
    frames = [stream.read(CHUNK) for _ in range(int(RATE / CHUNK * seconds))]
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    return b''.join(frames)

def analyze_audio(audio):
    samples = np.frombuffer(audio, dtype=np.int16)
    return{
        "duration": len(samples) / RATE,
        "average": np.mean(np.abs(samples)),
        "max": np.max(np.abs(samples)),
        "SAMPLES": samples
    }

def transcribe_audio(audio):
    r = sr.Recognizer()
    try:
        return r.recognize_google(sr.AudioData(audio, RATE, 2))
    except:
        return "Transcription failed."
    
def plot(a1, a2):
        plt.plot(a1["SAMPLES"], label="Audio 1")
        plt.plot(a2["SAMPLES"], label ="Audio 2")
        plt.legend()
        plt.show()

print("SPEAK NORMALLY AND CLEARLY FOR 3 SECONDS")
audio1 = record_sounds(3)
s1 = analyze_audio(audio1)

print("SPEAK LOUDER OR FASTER FOR 3 SECONDS")
audio2 = record_sounds(3)
s2 = analyze_audio(audio2)

print("/n------------------- RESULTS -------------------")
print("R1 DURATION:", s1["duration"], "AVG VOLUME:", s1["average"])
print("R2 DURATION:", s2["duration"], "AVG VOLUME:", s2["average"])
plot(s1, s2)
