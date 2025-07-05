# CRUD operations for todos
from database import db
from models import Todo

def add_todo(title, description=None, due_date=None):
    todo = {
        "title": title,
        "description": description if description else None,
        "due_date": due_date if due_date else None,
        "completed": False
    }
    db.ai_todo.insert_one(todo)
    return True

def list_todos():
    return list(db.ai_todo.find())

def complete_todo(todo_id):
    from bson.objectid import ObjectId
    result = db.ai_todo.update_one({"_id": ObjectId(todo_id)}, {"$set": {"completed": True}})
    return result.modified_count > 0

def modify_todo(todo_id, title=None, description=None, due_date=None):
    from bson.objectid import ObjectId
    update_fields = {}
    if title is not None:
        update_fields["title"] = title
    if description is not None:
        update_fields["description"] = description
    if due_date is not None:
        update_fields["due_date"] = due_date
    if not update_fields:
        return False
    result = db.ai_todo.update_one({"_id": ObjectId(todo_id)}, {"$set": update_fields})
    return result.modified_count > 0

def delete_todo(todo_id):
    from bson.objectid import ObjectId
    result = db.ai_todo.delete_one({"_id": ObjectId(todo_id)})
    return result.deleted_count > 0
