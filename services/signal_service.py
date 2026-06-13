class SignalService:

    @staticmethod
    def generate(df):

        latest = df.iloc[-1]

        score = 0

        reasons = []

        if latest["RSI"] < 30:
            score += 1
            reasons.append("RSI indicates oversold conditions.")

        elif latest["RSI"] > 70:
            score -= 1
            reasons.append("RSI indicates overbought conditions.")

        if latest["MACD"] > latest["MACD_SIGNAL"]:
            score += 1
            reasons.append("Bullish MACD crossover.")

        else:
            score -= 1
            reasons.append("Bearish MACD crossover.")

        if latest["Close"] > latest["EMA20"]:
            score += 1
            reasons.append("Price is above EMA20.")

        if latest["Close"] > latest["EMA50"]:
            score += 1
            reasons.append("Price is above EMA50.")

        if score >= 3:
            signal = "BUY"

        elif score <= -2:
            signal = "SELL"

        else:
            signal = "HOLD"

        return {
            "signal": signal,
            "score": score,
            "reasons": reasons
        }