# Streamlit-based Todo App main entry
import streamlit as st
from crud import add_todo, list_todos, complete_todo, modify_todo, delete_todo
import os
from ai.nlp import analyze_todo_command, summarize_todos
from datetime import datetime


st.title("AI Todo App")

# --- AI Section ---
st.header("AI Assistant: Natural Language Todo Management")
ai_input = st.text_input("Ask AI to manage your todos (e.g. 'Remind me to call mom tomorrow and delete the old task'):")
ai_result = None
if st.button("Let AI Handle It") and ai_input:
    # Setup Gemini/OpenAI LLM
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
    if not GEMINI_API_KEY:
        st.error("Gemini API key not found. Please set GEMINI_API_KEY in your environment or Streamlit secrets.")
    else:
        try:
            ai_result = analyze_todo_command(ai_input, GEMINI_API_KEY)
            st.code(ai_result, language="json")
            # Execute the action
            action = ai_result.get("action")
            if action == "add":
                add_todo(
                    ai_result.get("title", ""),
                    ai_result.get("description", ""),
                    ai_result.get("due_date", "")
                )
                st.success("AI added a todo!")
                st.rerun()
            elif action == "delete":
                todos = list_todos()
                for todo in todos:
                    if todo.get("title", "").lower() == ai_result.get("title", "").lower():
                        delete_todo(str(todo["_id"]))
                        st.success(f"AI deleted todo: {todo.get('title')}")
                        st.rerun()
                st.warning("No matching todo found to delete.")
            elif action == "complete":
                todos = list_todos()
                for todo in todos:
                    if todo.get("title", "").lower() == ai_result.get("title", "").lower():
                        complete_todo(str(todo["_id"]))
                        st.success(f"AI marked as complete: {todo.get('title')}")
                        st.rerun()
                st.warning("No matching todo found to complete.")
            elif action == "summarize":
                todos = list_todos()
                summary = summarize_todos(todos, GEMINI_API_KEY)
                st.info(f"AI Summary: {summary}")
            else:
                st.warning("AI could not determine a valid action.")
        except Exception as e:
            st.error(f"AI error: {e}")

# Add Todo
st.header("Add a New Todo")
with st.form("add_todo_form"):
    title = st.text_input("Title")
    description = st.text_area("Description")
    due_date = st.text_input("Due Date (YYYY-MM-DD)")
    submitted = st.form_submit_button("Add Todo")
    if submitted:
        if not title:
            st.error("Title is required!")
        else:
            try:
                if due_date:
                    datetime.strptime(due_date, "%Y-%m-%d")
                add_todo(title, description, due_date)
                st.success("Todo added!")
                st.rerun()
            except ValueError:
                st.error("Due date must be in YYYY-MM-DD format.")

# Filters and Sorting
st.header("Your Todos")
filter_status = st.selectbox("Filter by status", ["All", "Incomplete", "Completed"])
sort_by = st.selectbox("Sort by", ["Created Order", "Due Date"])

todos = list_todos()

# Filter
if filter_status == "Incomplete":
    todos = [todo for todo in todos if not todo.get('completed', False)]
elif filter_status == "Completed":
    todos = [todo for todo in todos if todo.get('completed', False)]

# Sort
if sort_by == "Due Date":
    def parse_due(todo):
        try:
            return datetime.strptime(todo.get('due_date', ''), "%Y-%m-%d")
        except Exception:
            return datetime.max
    todos = sorted(todos, key=parse_due)

if not todos:
    st.info("No todos found.")
else:
    for todo in todos:
        st.write(f"**{todo.get('title')}** | Completed: {todo.get('completed', False)} | Due: {todo.get('due_date', '')}")
        st.write(f"Description: {todo.get('description', '')}")
        col1, col2, col3 = st.columns(3)
        if not todo.get('completed', False):
            if col1.button("Complete", key=f"complete_{todo['_id']}"):
                try:
                    complete_todo(str(todo['_id']))
                    st.success("Todo marked as complete!")
                except Exception as e:
                    st.error(f"Error: {e}")
                st.rerun()
        if col2.button("Modify", key=f"modify_{todo['_id']}"):
            with st.form(f"modify_form_{todo['_id']}"):
                new_title = st.text_input("New Title", value=todo.get('title'))
                new_description = st.text_area("New Description", value=todo.get('description', ''))
                new_due_date = st.text_input("New Due Date", value=todo.get('due_date', ''))
                submitted_mod = st.form_submit_button("Update Todo")
                if submitted_mod:
                    try:
                        if new_due_date:
                            datetime.strptime(new_due_date, "%Y-%m-%d")
                        modify_todo(str(todo['_id']), new_title, new_description, new_due_date)
                        st.success("Todo updated!")
                    except ValueError:
                        st.error("Due date must be in YYYY-MM-DD format.")
                    except Exception as e:
                        st.error(f"Error: {e}")
                    st.rerun()
        if col3.button("Delete", key=f"delete_{todo['_id']}"):
            try:
                delete_todo(str(todo['_id']))
                st.warning("Todo deleted!")
            except Exception as e:
                st.error(f"Error: {e}")
            st.rerun()
