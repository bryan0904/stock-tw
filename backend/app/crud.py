from sqlalchemy.orm import Session
from models import OHLCV
from datetime import date

def upsert_ohlcv(db: Session, records: list[dict]):
    for r in records:
        obj = db.query(OHLCV)\
            .filter_by(stock_id=r["stock_id"], date=r["date"])\
            .first()
        if obj:
            for field in ["open","high","low","close","volume"]:
                setattr(obj, field, r[field])
        else:
            db.add(OHLCV(**r))
    db.commit()

def get_latest_price(db: Session, stock_id: str):
    return db.query(OHLCV)\
        .filter_by(stock_id=stock_id)\
        .order_by(OHLCV.date.desc())\
        .first()

def get_historical(db: Session, stock_id: str, start: date, end: date):
    return db.query(OHLCV)\
        .filter(OHLCV.stock_id==stock_id)\
        .filter(OHLCV.date>=start)\
        .filter(OHLCV.date<=end)\
        .order_by(OHLCV.date)\
        .all()
