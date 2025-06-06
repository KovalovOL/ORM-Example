from db import get_db
from models import User

def create_user(name: str, email: str):
    db = next(get_db())
    user = User(name=name, email=email)
    db.add(user)
    db.commit()

def read_users():
    db = next(get_db())
    users = db.query(User).all()
    return users

def update_user(user_id: int, new_name: str = None, new_email: str = None):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        db.commit()

def delete_user(user_id: int):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
