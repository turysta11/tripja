import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# 1. Create database tables automatically FIRST before hitting any routes
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Price Tracker AI")

# 2. Setup Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Import routes HERE to break circular dependency chains
from routes import tracking, admin, ws

# 4. Connect all the routes
app.include_router(tracking.router)
app.include_router(admin.router)
app.include_router(ws.router)

@app.get("/")
def root():
    return {"status": "healthy", "message":
