
class RegimeEngine:

    def analyze(self, market):

        trend = market.get("trend", "NEUTRAL")
        volatility = float(market.get("volatility", 0.0))
        momentum = float(market.get("momentum", 0.0))

        if volatility >= 0.05:
            regime = "HIGH_VOLATILITY"

        elif trend == "UP" and momentum > 0.5:
            regime = "BULL"

        elif trend == "DOWN" and momentum < -0.5:
            regime = "BEAR"

        else:
            regime = "NEUTRAL"

        return {
            "regime": regime,
            "trend": trend,
            "volatility": volatility,
            "momentum": momentum
        }
