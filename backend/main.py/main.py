import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import tracking, admin, ws

# 1. Initialize the FastAPI app instance first so it's ready in memory
app = FastAPI(title="Hotel Price Tracker AI")

# 2. Setup Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Use FastAPI lifespan events to create tables *on startup* instead of global scope
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# 4. Connect your routers
app.include_router(tracking.router)
app.include_router(admin.router)
app.include_router(ws.router)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Hotel Tracker API is running!"}
