from modules.speech_engine import speak, listen
from modules.openai_chat import ai_chatbot
from modules.system_commands import open_application, close_application, lock_screen
from modules.time_info import get_time
from modules.web_search import search_google, search_wikipedia
from modules.email_messaging import send_email, send_whatsapp
from modules.reminders_notes import set_reminder, save_note
from modules.music_control import play_music, pause_music, next_track
from modules.personalization import save_preference
from modules.language_support import translate_text
from modules.coding_assistant import code_explainer, generate_code

def process_command(command):
    """Processes user commands and returns a response."""
    # Wakeup call completed.
    if "hello" in command or "nova" in command or "hello nova" in command:
        return "Mr. Korat! What can I do for you?"
    
    # time working.
    elif "time" in command:
        return get_time()
    
    # open working, close & lock screen not working.
    elif "open" in command:
        app_name = command.replace("open ", "")
        return open_application(app_name)
    elif "close" in command:
        app_name = command.replace("close ", "")
        return close_application(app_name)
    elif "lock screen" in command:
        return lock_screen()
    
    # serch google working.
    elif "search google for" in command:
        query = command.replace("search google for ", "")
        return search_google(query)
    
    # search wikipedia working.
    elif "search wikipedia for" in command:
        query = command.replace("search wikipedia for ", "")
        return search_wikipedia(query)
    
    # send email not working.
    elif "send email" in command:
        return send_email("receiver@example.com", "Test Subject", "Hello!")
    elif "send email to" in command:
        receiver_email = command.replace("send email to ", "")
        subject = command.replace("and subject is ", "")
        message = command.replace("and message is ", "")
        return send_email(receiver_email, subject, message)
    
    # Not working, big problem.
    elif "reminder" in command:
        return set_reminder("Meeting in 10 minutes", 600)
    
    # play music working, pause and next is not working.
    elif "play music" in command or "play song" in command:
        song_name = command.replace("play music ", "") or command.replace("play song ", "")
        return play_music(song_name)
    elif "pause music" in command or "pause song" in command:
        return pause_music()
    elif "next track" in command or "next music" in command:
        return next_track()
    
    # not working.
    elif "generate code for" in command:
        prompt = command.replace("generate code for ", "")
        return generate_code(prompt)
    
    # translate working.
    elif "translate" in command:
        text = command.replace("translate ", "")
        return translate_text(text, "english")
    
    # great working.
    elif "great" in command:
        return "Thank you, it's my pleasure."
    
    # Exit and goodbye working.
    elif "exit" in command:
        return "Okay sir! exit performing."
    elif "goodbye" in command:
        return "Goodbye! Have a great day."
    else:
        return ai_chatbot(command)

if __name__ == "__main__":
    speak("Hello, I am NOVA. AI powered Next-Gen Omni Voice Assistant. How can I assist you?")
    while True:
        command = listen()
        if command:
            response = process_command(command)
            speak(response)
            if "exit" in command or "goodbye" in command:
                break
