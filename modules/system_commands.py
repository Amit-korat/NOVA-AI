import os
import platform

def open_application(app_name):
    """Open system applications based on OS."""
    try:
        if platform.system() == "Windows":
            os.system(f"start {app_name}")
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open -a '{app_name}'")
        elif platform.system() == "Linux":
            os.system(f"xdg-open {app_name}")
        return f"Opening {app_name}"
    except Exception as e:
        return f"Failed to open {app_name}. Error: {e}"
    
    # close app and lock screen not wworking.
def close_application(app_name):
    """Close system applications based on OS."""
    try:
        if platform.system() == "Windows":
            os.system(f"taskkill /F /IM {app_name}.exe")  # Force close the app
        elif platform.system() == "Darwin":  # macOS
            os.system(f"pkill -f '{app_name}'")  # Close by process name
        elif platform.system() == "Linux":
            os.system(f"pkill -f '{app_name}'")  # Kill the process
        return f"Closed {app_name}"
    except Exception as e:
        return f"Failed to close {app_name}. Error: {e}"

def lock_screen():
    """Lock the screen."""
    if platform.system() == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif platform.system() == "Darwin":  # macOS
        os.system("/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession -suspend")
    elif platform.system() == "Linux":
        os.system("gnome-screensaver-command -l")
    return "Screen locked"
