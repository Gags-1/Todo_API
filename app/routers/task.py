from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from typing import List, Optional
from .. database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/", response_model=list[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    tasks = db.query(models.Task).filter(
        models.Task.user_id == current_user.id,
        models.Task.task.contains(search)
    ).limit(limit).offset(skip).all()
    
    return [{"task": task} for task in tasks]

    
    return results

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_task = models.Task(user_id=current_user.id, **task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/{id}", response_model=schemas.TaskOut)
def get_task(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # task = db.query(models.Task).filter(models.Task.id == id).first()

    task=db.query(models.Task).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")
    return task

@router.delete("/{id}")
def delete_task(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")

    if task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    task_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Task deleted"}

@router.put("/{id}", response_model=schemas.Task)
def update_task(id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")

    if task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    task_query.update(updated_task.dict(), synchronize_session=False)
    db.commit()
    return task_query.first()
