from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from database import engine, Base, get_db
from controller import *

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/users', response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@app.get('/users/{user_id}', response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@app.post('/users', response_model=UserOut)
def create_new_user(user: UserBase, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_by_id(db, user_id)

@app.put('/users/{user_id}', response_model=UserOut)
def update_user(user: UserUpdate, user_id: int, db: Session = Depends(get_db)):
    return update_by_id(db, user_id, user)

@app.patch('/users/{user_id}', response_model=UserOut)
def patch_user(user_id: int, user_data: UserPatch, db: Session = Depends(get_db)):
    return patch_user_by_id(db, user_id, user_data)