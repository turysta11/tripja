import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
# 1. Import your routes folder endpoints
from routes import tracking, admin, ws 

# Create tables safely on startup
Base.metadata.create_all(bind=engine)

# 2. Explicitly force the documentation paths
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

# 3. Register your active endpoints to the server
app.include_router(tracking.router)
app.include_router(admin.router)
app.include_router(ws.router)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Hotel Tracker API is running!"}
