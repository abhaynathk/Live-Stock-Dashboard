from fastapi import FastAPI, HTTPException
from services.stock_service import StockService

app = FastAPI(title="Stock AI Agent")


@app.get("/")
def home():
    return {"message": "Stock AI Agent Running"}


@app.get("/stock/{symbol}")
def get_stock(symbol: str):

    try:
        data = StockService.get_stock_data(symbol.upper())
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/history/{symbol}")
def history(symbol: str):

    return StockService.get_history(symbol.upper())