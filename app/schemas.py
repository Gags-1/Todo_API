from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from typing import Optional
#This is BaseModel used to set parameters in the posts that the user will create
class TaskBase(BaseModel):
    task: str
    completed: bool = True

class TaskCreate(TaskBase):
    pass
class UserReponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True


#for reposne to user
class Task(TaskBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserReponse #This is used to add the user details in the post response\
    # vote: int
    #Rest of the parameters are same as PostBase
    class config:
        orm_mode = True

class TaskOut(BaseModel):
    Task: Task
    votes: int

    class config:
        orm_mode = True

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