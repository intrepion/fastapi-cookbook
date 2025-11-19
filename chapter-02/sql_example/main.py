from database import SessionLocal, User
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return users
