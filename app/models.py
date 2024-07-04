from sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer, String, Boolean, text
from .database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__="tasks"


    id=Column(Integer,primary_key=True, nullable=False)
    task=Column(String, nullable=False)
    competed=Column(Boolean,server_default='FALSE', nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    user_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) #Adding foreign key to connect the user table with the users table
    
    user=relationship("User") #Adding a relationship to connect the user table with the tasks table

    # REMEMBER IF YOU WANT TO CHANGE ANYTHING IN YOUR PRE-EXISTING TABLE, YOU FIRST HAVE TO DELETE THE TABLE
    # AND THEN ONLY A NEW TABLE CAN BE CREATED WHICH IS KIND OF WEIRD BECAUSE YOU'LL THEN HAVE TO DELETE ALL YOUR DATA
    # SO MAKE SURE TO CHECK OTHER OPTIONS AFTER THIS, YOU CAN USE A DATABASE MIGRATION TOOL



class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True, nullable=False)
    username=Column(String, nullable=False)
    email=Column(String, nullable=False,unique=True)
    password=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))