# Simple Gemini chat in terminal for testing

from llm import get_gemini_llm

llm = get_gemini_llm(model="gemini-2.0-flash")  # Use the latest Gemini model

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
