import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# Create tables safely on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Price Tracker AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Hotel Tracker API is running!"}
