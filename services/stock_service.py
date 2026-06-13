import yfinance as yf
import numpy as np
from services.indicator_service import IndicatorService

class StockService:

    @staticmethod
    def get_stock_data(symbol):

        stock = yf.Ticker(symbol)

        info = stock.info

        return {
            "symbol": symbol,
            "company": info.get("longName"),
            "current_price": info.get("currentPrice"),
            "previous_close": info.get("previousClose"),
            "open": info.get("open"),
            "day_high": info.get("dayHigh"),
            "day_low": info.get("dayLow"),
            "volume": info.get("volume"),
            "market_cap": info.get("marketCap"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow")
        }

    @staticmethod
    def get_history(symbol, period="6mo"):
        stock = yf.Ticker(symbol)
        history = stock.history(period=period)

        # 1. Check if the ticker is valid and returned data
        if history.empty:
            return [] 

        # 2. Calculate indicators
        history = IndicatorService.calculate(history)

        # 3. Fix JSON NaN issues: Replace pandas/numpy NaN with Python None
        history = history.replace({np.nan: None})

        # 4. Fix JSON Timestamp issues: Convert DatetimeIndex to string format
        # yfinance often returns timezone-aware datetimes, so we format it simply
        history.index = history.index.strftime('%Y-%m-%d')

        return history.reset_index().to_dict("records")