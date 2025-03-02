import wikipedia
import webbrowser

def search_google(query):
    """Perform a Google search."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for {query}"

def search_wikipedia(query):
    """Perform a Wikipedia search."""
    try:
        result = wikipedia.summary(query, sentences=3)
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "Multiple results found. Be more specific."
    except wikipedia.exceptions.PageError:
        return "No results found on Wikipedia."
