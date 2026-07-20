import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# Absolute import telling Python to look inside the backend folder package
from backend.routers import tracking_router, admin_router, ws_router

# Create tables safely on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hotel Price Tracker AI",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the routers from your single file
app.include_router(tracking_router)
app.include_router(admin_router)
app.include_router(ws_router)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Hotel Tracker API is running!"}
