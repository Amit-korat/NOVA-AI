import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

def speak(text):
    """Converts text to speech."""
    print(f"NOVA: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures user speech and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio)
        print(f"You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Speech Recognition service is unavailable.")
        return "Speech Recognition service is unavailable."
