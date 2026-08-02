
from strategies.trend import trend_signal
from strategies.volatility import volatility_signal
from strategies.momentum import momentum_signal


class ResearchEngine:

    def analyze(self, market):

        trend = trend_signal(market)
        volatility = volatility_signal(market)
        momentum = momentum_signal(market)

        score = (
            trend * 0.40
            + volatility * 0.20
            + momentum * 0.40
        )

        return {
            "signals": {
                "trend": trend,
                "volatility": volatility,
                "momentum": momentum
            },
            "score": round(score, 4)
        }
