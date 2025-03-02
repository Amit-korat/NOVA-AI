import json

USER_DATA_FILE = "user_data.json"

def save_preference(category, value):
    """Saves user preferences."""
    data = load_preferences()
    data[category] = value
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)
    return "Preference saved!"

def load_preferences():
    """Loads user preferences."""
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
