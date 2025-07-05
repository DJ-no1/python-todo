# Prompt templates for LLMs

# --- FEW-SHOT EXAMPLES FOR CHAIN-OF-THOUGHTS ---
FEW_SHOT_EXAMPLES = '''
Example 1:
User input: Add a todo to call mom tomorrow
Step 1: The user wants to add a new todo. The context is a creation request.
Step 2: This is an add action.
Step 3: Extracting title: 'call mom', due_date: 'tomorrow'.
Step 4: {{"action": "add", "title": "call mom", "description": null, "due_date": "tomorrow"}}
Step 5: Call add_todo(title="call mom", description=None, due_date="tomorrow")

Example 2:
User input: Mark the grocery shopping as complete
Step 1: The user wants to mark a todo as complete. The context is a completion request.
Step 2: This is a complete action.
Step 3: Extracting title: 'grocery shopping'.
Step 4: {{"action": "complete", "title": "grocery shopping"}}
Step 5: Call complete_todo(title="grocery shopping")

Example 3:
User input: Delete the old task and remind me to pay bills next week
Step 1: The user wants to delete a task and add a new reminder. This is a multi-action request.
Step 2: This is a delete action and an add action.
Step 3: Extracting title: 'old task' for delete, title: 'pay bills', due_date: 'next week' for add.
Step 4: [
  {{"action": "delete", "title": "old task"}},
  {{"action": "add", "title": "pay bills", "description": null, "due_date": "next week"}}
]
Step 5: Call delete_todo(title="old task") and add_todo(title="pay bills", description=None, due_date="next week")
'''

# --- MAIN CHAIN-OF-THOUGHTS PROMPT ---
CHAIN_OF_THOUGHTS_PROMPT = '''
You are an AI assistant for a todo app. Think step by step in a chain-of-thoughts manner. For each step, print what you are doing, then proceed to the next step. At the end, output a JSON object with the action and fields.

IMPORTANT: For both the JSON and Step 5, always use one of these action keywords: 'add', 'update', 'delete', 'complete', or 'summarize'.
For Step 5, describe which function should be called in the app to perform the action, using these function names: add_todo, modify_todo, delete_todo, complete_todo, summarize_todos. Specify the arguments to pass, matching the JSON fields.

{few_shot_examples}

Step 1: Analyze the context and determine what kind of task this is. Print your reasoning.
Step 2: Decide if this is an add, update, complete, delete, or summarize task. Print your reasoning.
Step 3: Upon understanding, extract the relevant fields (title, description, due date, etc.) and print what you are extracting.
Step 4: Output only a JSON object with the action and fields as the final answer, using the action keywords above. For multi-action, output a list of JSON objects. (Escape curly braces in JSON with double curly braces.)
Step 5: Describe which function (from add_todo, modify_todo, delete_todo, complete_todo, summarize_todos) should be called in the app to perform the action, and what arguments should be passed. Print your reasoning.

User input: {user_input}
Respond in the following format:
Step 1: ...\nStep 2: ...\nStep 3: ...\nStep 4: <JSON object or list only on this line>\nStep 5: ...
'''
