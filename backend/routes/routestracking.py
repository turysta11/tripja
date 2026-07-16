from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import HotelTracking
from schemas import TrackingCreate

router = APIRouter(prefix="/track", tags=["Tracking"])

@router.post("/")
def create_tracking(data: TrackingCreate, db: Session = Depends(get_db)):
    tracking = HotelTracking(**data.dict())
    db.add(tracking)
    db.commit()
    db.refresh(tracking)
    return tracking

@router.get("/{tracking_id}")
def get_tracking(tracking_id: int, db: Session = Depends(get_db)):
    return db.query(HotelTracking).filter_by(id=tracking_id).first()