from fastapi import APIRouter
from yahoo_service import get_stock_data

router = APIRouter()

@router.get("/yahoo/{symbol}")
def yahoo_stock(symbol: str):
    data = get_stock_data(symbol)

    return data.reset_index().to_dict(orient="records")