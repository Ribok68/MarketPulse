class DecisionEngine:
    def decide(self, market):
        trend = market.get("trend", "UNKNOWN")
        volatility = market.get("volatility", 0)

        if trend == "UP" and volatility < 0.03:
            return "BUY"

        if trend == "DOWN":
            return "SELL"

        return "HOLD"
