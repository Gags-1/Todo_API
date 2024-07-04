from fastapi import FastAPI
from . import models
from .database import engine
from .routers import task, user, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine) #Base engine for orm //from database.py file
#^
#|, dont need that anymore as we have alembic

app=FastAPI()

origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def message():
    return {'Message': 'Welcome to the todo site'}

app.include_router(task.router)
app.include_router(user.router)
app.include_router(auth.router)

