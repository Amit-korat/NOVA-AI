import requests
import pyttsx3
from config import NEWS_API_KEY

engine = pyttsx3.init()

def speak(text):
    """Speak the given text"""
    engine.say(text)
    engine.runAndWait()

def get_news():
    """Fetch latest news"""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    
    if "articles" in response:
        headlines = [article["title"] for article in response["articles"][:5]]
        for headline in headlines:
            speak(headline)
    else:
        speak("No news found.")
