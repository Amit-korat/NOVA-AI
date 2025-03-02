import json
import time
from plyer import notification

NOTES_FILE = "notes.json"

def set_reminder(text, delay):
    """Sets a reminder after a delay (in seconds)."""
    time.sleep(delay)
    notification.notify(title="Reminder", message=text, timeout=10)
    return "Reminder set!"

def save_note(title, content):
    """Saves a note."""
    notes = load_notes()
    notes[title] = content
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file)
    return "Note saved!"

def load_notes():
    """Loads saved notes."""
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
