from pydantic import BaseModel
from datetime import date

class OHLCVBase(BaseModel):
    stock_id: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: float

    class Config:
        orm_mode = True

class Quote(BaseModel):
    stock_id: str
    close: float
    date: date
