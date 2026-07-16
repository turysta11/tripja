from pydantic import BaseModel
from datetime import date

class TrackingCreate(BaseModel):
    hotel_name: str
    base_price: float
    check_in: date
    check_out: date
    occupants: int
    email: str