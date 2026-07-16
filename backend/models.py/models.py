from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class HotelTracking(Base):
    __tablename__ = "hotel_tracking"

    id = Column(Integer, primary_key=True)
    hotel_name = Column(String)
    base_price = Column(Float)
    check_in = Column(Date)
    check_out = Column(Date)
    occupants = Column(Integer)
    email = Column(String)

    prices = relationship("DailyPrice", back_populates="tracking")

class DailyPrice(Base):
    __tablename__ = "daily_price"

    id = Column(Integer, primary_key=True)
    tracking_id = Column(Integer, ForeignKey("hotel_tracking.id"))
    site = Column(String)
    price = Column(Float)
    deeplink = Column(String, nullable=True)
    checked_at = Column(DateTime, default=datetime.utcnow)

    tracking = relationship("HotelTracking", back_populates="prices")