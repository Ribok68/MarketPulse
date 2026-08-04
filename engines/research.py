
class ResearchEngine:

    def __init__(self, learning=None):
        self.learning = learning

    def analyze(self, market):

        trend = market.get("trend", "NEUTRAL")
        volatility = float(market.get("volatility", 0.0))
        momentum = float(market.get("momentum", 0.0))

        trend_signal = (
            1.0 if trend == "UP"
            else -1.0 if trend == "DOWN"
            else 0.0
        )

        volatility_signal = (
            1.0 if volatility < 0.02
            else 0.0 if volatility < 0.04
            else -1.0
        )

        momentum_signal = (
            1.0 if momentum > 0.5
            else -1.0 if momentum < -0.5
            else 0.0
        )

        signals = {
            "trend": trend_signal,
            "volatility": volatility_signal,
            "momentum": momentum_signal
        }

        if self.learning:
            weights = self.learning.get_weights()
        else:
            weights = {
                "trend": 0.40,
                "volatility": 0.20,
                "momentum": 0.40
            }

        score = sum(
            signals[name] * weights[name]
            for name in signals
        )

        return {
            "signals": signals,
            "weights": weights,
            "score": round(score, 4)
        }
