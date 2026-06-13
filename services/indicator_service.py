import pandas as pd

from ta.momentum import RSIIndicator
from ta.trend import (
    MACD,
    EMAIndicator,
    SMAIndicator,
    ADXIndicator
)
from ta.volatility import BollingerBands
from ta.volume import VolumeWeightedAveragePrice


class IndicatorService:

    @staticmethod
    def calculate(df: pd.DataFrame):

        df = df.copy()

        # RSI
        df["RSI"] = RSIIndicator(df["Close"]).rsi()

        # MACD
        macd = MACD(df["Close"])

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_DIFF"] = macd.macd_diff()

        # EMA
        df["EMA20"] = EMAIndicator(df["Close"], window=20).ema_indicator()
        df["EMA50"] = EMAIndicator(df["Close"], window=50).ema_indicator()

        # SMA
        df["SMA200"] = SMAIndicator(df["Close"], window=200).sma_indicator()

        # Bollinger
        bb = BollingerBands(df["Close"])

        df["BB_HIGH"] = bb.bollinger_hband()
        df["BB_LOW"] = bb.bollinger_lband()

        # ADX
        adx = ADXIndicator(
            df["High"],
            df["Low"],
            df["Close"]
        )

        df["ADX"] = adx.adx()

        # VWAP
        vwap = VolumeWeightedAveragePrice(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            volume=df["Volume"]
        )

        df["VWAP"] = vwap.volume_weighted_average_price()

        return df