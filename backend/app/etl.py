from apscheduler.schedulers.asyncio import AsyncIOScheduler
import httpx, pandas as pd
from crud import upsert_ohlcv
from database import SessionLocal

API_URL = "https://api.finmindtrade.com/api/v4/data"

async def fetch_and_store():
    params = {
        "dataset": "TaiwanStockPrice",
        "stock_id": "2330",
        "start_date": "2023-01-01"
    }
    async with httpx.AsyncClient() as client:
        r = await client.get(API_URL, params=params)
        data = r.json().get("data", [])
        if data:
            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["date"]).dt.date
            records = df.to_dict(orient="records")
            db = SessionLocal()
            upsert_ohlcv(db, records)
            db.close()

scheduler = AsyncIOScheduler()
scheduler.add_job(fetch_and_store, "interval", minutes=1)
