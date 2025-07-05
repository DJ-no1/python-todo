
# LLM wrapper for Gemini (Google Generative AI)
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Supported Gemini models
GEMINI_MODELS = {
    "gemini-1.5-flash": "gemini-1.5-flash",
    "gemini-1.5-pro": "gemini-1.5-pro",
    "gemini-2.5-flash": "gemini-2.5-flash",
    "gemini-2.0-flash": "gemini-2.0-flash",

}

def get_gemini_llm(model: str = "gemini-2.5-flash", temperature: float = 0.2):
    """
    Returns a Gemini LLM instance with API key loaded from env.
    Model must be one of the supported Gemini models.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY or GEMINI_API_KEY not found in environment.")
    os.environ["GOOGLE_API_KEY"] = api_key
    model_id = GEMINI_MODELS.get(model, model)
    return ChatGoogleGenerativeAI(model=model_id, temperature=temperature)

def list_gemini_models():
    """Returns a list of supported Gemini model names."""
    return list(GEMINI_MODELS.keys())

# Example usage:
# llm = get_gemini_llm()
#  response = llm.invoke("Say hello!")


# Use get_gemini_llm(model="gemini-1.5-pro") or any supported model name.
# Call list_gemini_models() to see all available Gemini models.
# Easily add more models to the GEMINI_MODELS dictionary in the future.