from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import get_historical
from database import get_db
from datetime import date

router = APIRouter()

@router.get("/{stock_id}")
def read_historical(
    stock_id: str, 
    start: date, 
    end: date, 
    db: Session = Depends(get_db)
):
    records = get_historical(db, stock_id, start, end)
    return {
        "dates": [r.date.isoformat() for r in records],
        "ohlcv": [[r.open, r.high, r.low, r.close] for r in records]
    }
