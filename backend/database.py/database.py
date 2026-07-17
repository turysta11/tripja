import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # <-- Added this missing import

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hoteltracker")

engine = create_engine(DATABASE_URL)

# Base is defined clearly right here
Base = declarative_base() 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
