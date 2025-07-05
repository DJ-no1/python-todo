# AI/NLP logic for parsing and handling natural language todo commands
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

def analyze_todo_command(user_input: str, api_key: str = None):
    from dotenv import load_dotenv
    load_dotenv()
    # Gemini expects GOOGLE_API_KEY in env, do not pass as param
    from ai.prompts import CHAIN_OF_THOUGHTS_PROMPT, FEW_SHOT_EXAMPLES
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template=CHAIN_OF_THOUGHTS_PROMPT.format(
            few_shot_examples=FEW_SHOT_EXAMPLES,
            user_input="{user_input}"
        )
    )
    chain = prompt | llm
    ai_response = chain.invoke({"user_input": user_input})
    import json, re
    # Extract content if ai_response is a message object
    content = getattr(ai_response, "content", None)
    if content is None:
        content = str(ai_response)
    if not content or not content.strip():
        raise ValueError("AI did not return any response.")
    # Print/log each step to console
    steps = re.findall(r'Step \d+:.*?(?=Step \d+:|$)', content, re.DOTALL)
    for step in steps:
        print(step.strip())
    # Extract the final JSON object from Step 4
    match = re.search(r'Step 4:.*?(\{.*\})', content, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            return json.loads(json_str)
        except Exception as e:
            raise ValueError(f"AI response could not be parsed as JSON: {json_str}\nError: {e}")
    else:
        # fallback: try to extract any JSON object
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            json_str = match.group(0)
            try:
                return json.loads(json_str)
            except Exception as e:
                raise ValueError(f"AI response could not be parsed as JSON: {json_str}\nError: {e}")
        else:
            raise ValueError(f"AI response did not contain a JSON object. Raw response: {content}")

def summarize_todos(todos, api_key: str = None):
    from dotenv import load_dotenv
    load_dotenv()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    todo_titles = [t.get("title", "") for t in todos]
    summary_prompt = PromptTemplate(
        input_variables=["todos"],
        template="Summarize the following todo list: {todos}"
    )
    chain = summary_prompt | llm
    summary = chain.invoke({"todos": ", ".join(todo_titles)})
    return summary
