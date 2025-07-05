# Pydantic models for request/response schemas and DB schema reference
from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    user_id: str = Field(..., description="Unique user identifier (device ID, cookie, etc.)")
    name: Optional[str] = None

class Todo(BaseModel):
    user_id: str = Field(..., description="ID of the user who owns this todo")
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None
    completed: bool = False

class Summarization(BaseModel):
    user_id: str = Field(..., description="ID of the user for whom the summary is generated")
    summary: str
    created_at: Optional[str] = None

# Example MongoDB document structure:
# users collection:
#   { _id: ObjectId, user_id: str, name: str }
# ai_todo collection:
#   { _id: ObjectId, user_id: str, title: str, description: str, due_date: str, completed: bool }
# summarizations collection:
#   { _id: ObjectId, user_id: str, summary: str, created_at: str }
