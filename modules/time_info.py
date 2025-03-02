from datetime import datetime

def get_time():
    """Returns the current time."""
    return f"The current time is {datetime.now().strftime('%I:%M %p')}"
