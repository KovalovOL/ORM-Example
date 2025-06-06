from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database configuration
DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/mydb"

# Set up engine and session
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL to console
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ORM model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# Create the users table if it doesn't exist
Base.metadata.create_all(bind=engine)

# CRUD functions
def create_user(name: str, email: str):
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()
    print(f"User '{name}' created.")

def read_users():
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        print(f"{user.id} | {user.name} | {user.email}")
    session.close()

def update_user(user_id: int, new_name: str = None, new_email: str = None):     
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        session.commit()
        print(f"User ID {user_id} updated.")
    else:
        print(f"User ID {user_id} not found.")
    session.close()

def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User ID {user_id} deleted.")
    else:
        print(f"User ID {user_id} not found.")
    session.close()

