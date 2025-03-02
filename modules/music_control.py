import pyautogui
import keyboard
import pywhatkit as kit

def play_music(song_name):
    """Plays a song on YouTube."""
    kit.playonyt(song_name)
    return f"Playing {song_name} on YouTube!"

def pause_music():
    """Pauses music (media key shortcut)."""
    pyautogui.press("playpause")
    return "Music paused."

def next_track():
    """Skips to the next track."""
    pyautogui.press("nexttrack")
    return "Skipped to next track."
