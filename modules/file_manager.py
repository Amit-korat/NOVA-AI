import os
import shutil
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Speak the given text"""
    engine.say(text)
    engine.runAndWait()

def find_files(extension, directory="."):
    """Find files with a specific extension"""
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    if files:
        speak(f"Found {len(files)} files.")
    else:
        speak("No files found.")
    return files

def move_file(source, destination):
    """Move a file"""
    try:
        shutil.move(source, destination)
        speak(f"Moved file {source} to {destination}")
    except Exception as e:
        speak(f"Failed to move file. Error: {e}")

def delete_file(filepath):
    """Delete a file"""
    try:
        os.remove(filepath)
        speak(f"Deleted file {filepath}")
    except Exception as e:
        speak(f"Failed to delete file. Error: {e}")
