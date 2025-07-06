from fastapi import APIRouter, Depends
# 範例：此路由暫時回傳固定訊息
router = APIRouter()

@router.get("/ping")
def ping():
    return {"msg": "strategy works"}
