import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Railway automatically provides the DATABASE_URL when you link Postgres
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hoteltracker")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()