import openai
from config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def ai_chatbot(prompt):
    """Generates a response using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "I'm having trouble responding right now."
