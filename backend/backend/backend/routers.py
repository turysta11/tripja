from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import HotelTracking
from schemas import TrackingCreate

# 1. Tracking Router
tracking_router = APIRouter(prefix="/track", tags=["Tracking"])

@tracking_router.post("/")
def create_tracking(data: TrackingCreate, db: Session = Depends(get_db)):
    # Use .model_dump() if you use Pydantic v2, or keep .dict() for v1
    tracking = HotelTracking(**data.model_dump()) 
    db.add(tracking)
    db.commit()
    db.refresh(tracking)
    return tracking

@tracking_router.get("/{tracking_id}")
def get_tracking(tracking_id: int, db: Session = Depends(get_db)):
    return db.query(HotelTracking).filter_by(id=tracking_id).first()


# 2. Admin Router Placeholder
admin_router = APIRouter(prefix="/admin", tags=["Admin"])

@admin_router.get("/")
def admin_root():
    return {"message": "Admin dashboard placeholder"}


# 3. WebSockets Router Placeholder
ws_router = APIRouter(prefix="/ws", tags=["WebSockets"])

@ws_router.get("/")
def ws_root():
    return {"message": "WebSocket connection placeholder"}
