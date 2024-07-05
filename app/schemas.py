from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# Base model used to set parameters in the tasks that the user will create
class TaskBase(BaseModel):
    task: str
    completed: bool = False 

class TaskCreate(TaskBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

# For response to user
class Task(TaskBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse # This is used to add the user details in the task response

    class Config:
        from_attributes = True

class TaskOut(BaseModel):
    task: Task

    class Config:
        from_attributes = True

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]
