# Simple Gemini chat in terminal for testing
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Make sure GOOGLE_API_KEY is set in .env
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

print("Gemini Terminal Chat. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        response = llm.invoke(user_input)
        print(f"Gemini: {response.content}")
    except Exception as e:
        print(f"Error: {e}")
