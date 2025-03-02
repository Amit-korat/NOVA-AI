from deep_translator import GoogleTranslator

def translate_text(text, dest_language):
    """Translates text into the specified language."""
    translator = GoogleTranslator(source="auto", target=dest_language)
    return translator.translate(text)

