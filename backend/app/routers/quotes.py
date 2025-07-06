from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_latest_price
from database import get_db
from schemas import Quote

router = APIRouter()

@router.get("/{stock_id}", response_model=Quote)
def read_quote(stock_id: str, db: Session = Depends(get_db)):
    q = get_latest_price(db, stock_id)
    if not q:
        raise HTTPException(status_code=404, detail="Stock not found")
    return q
