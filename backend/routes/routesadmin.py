from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import HotelTracking, DailyPrice

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/trackings")
def all_trackings(db: Session = Depends(get_db)):
    return db.query(HotelTracking).all()

@router.get("/prices/{tracking_id}")
def price_history(tracking_id: int, db: Session = Depends(get_db)):
    return db.query(DailyPrice).filter(DailyPrice.tracking_id == tracking_id).order_by(DailyPrice.checked_at).all()