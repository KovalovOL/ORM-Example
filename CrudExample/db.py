from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/mydb"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Simple generator function (not a context manager)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
