import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hoteltracker")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Base class for database models (Expected by main.py)
Base = declarative_base()

# Session factory for handling connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to inject DB sessions into route handlers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
