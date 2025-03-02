import openai
from config import OPENAI_API_KEY
from modules.openai_chat import ai_chatbot

openai.api_key = OPENAI_API_KEY

def code_explainer(code_snippet):
    """Explains a given code snippet."""
    prompt = f"Explain the following code:\n{code_snippet}"
    return ai_chatbot(prompt)

def generate_code(prompt):
    """Generates code based on user input."""
    return ai_chatbot(f"Write code for: {prompt}")
