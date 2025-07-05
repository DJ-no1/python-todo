
# Tool-calling wrappers for CRUD operations
from crud import add_todo, list_todos, complete_todo, modify_todo, delete_todo

def call_add_todo(args):
    return add_todo(
        args.get('title', ''),
        args.get('description', None),
        args.get('due_date', None)
    )

def call_delete_todo(args):
    # Find todo by title (case-insensitive)
    todos = list_todos()
    for todo in todos:
        if todo.get('title', '').lower() == args.get('title', '').lower():
            return delete_todo(str(todo['_id']))
    return False

def call_complete_todo(args):
    todos = list_todos()
    for todo in todos:
        if todo.get('title', '').lower() == args.get('title', '').lower():
            return complete_todo(str(todo['_id']))
    return False

def call_modify_todo(args):
    todos = list_todos()
    for todo in todos:
        if todo.get('title', '').lower() == args.get('title', '').lower():
            return modify_todo(
                str(todo['_id']),
                args.get('new_title', todo.get('title')),
                args.get('description', todo.get('description')),
                args.get('due_date', todo.get('due_date'))
            )
    return False

def call_summarize_todos(args):
    # This is a placeholder; actual summary is handled in main.py
    return 'summarize'

# Map function names to callables
TOOL_FUNCTIONS = {
    'add_todo': call_add_todo,
    'delete_todo': call_delete_todo,
    'complete_todo': call_complete_todo,
    'modify_todo': call_modify_todo,
    'summarize_todos': call_summarize_todos,
}
