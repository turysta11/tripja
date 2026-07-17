import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # <-- Added declarative_base here

# Railway automatically provides the DATABASE_URL when you link Postgres
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hoteltracker")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the missing Base class that main.py is looking for
Base = declarative_base()  # <-- Added this line

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
