from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database config
DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 2. ORM model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# 3. Create tables
Base.metadata.create_all(bind=engine)

# 4. Interact with the database
def main():
    session = SessionLocal()

    # Add a new user
    new_user = User(name="Alice", email="alice@example.com")
    session.add(new_user)
    session.commit()

    # Query users
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name, user.email)

    session.close()

if __name__ == "__main__":
    main()
