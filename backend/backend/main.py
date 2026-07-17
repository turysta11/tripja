import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import tracking, admin, ws

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Price Tracker AI")

# This allows your mobile app and web dashboard to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect all the routes
app.include_router(tracking.router)
app.include_router(admin.router)
app.include_router(ws.router)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Hotel Tracker API is running!"}