
class RiskEngine:

    def analyze(self, market, research):

        volatility = float(market.get("volatility", 0.0))
        score = float(research.get("score", 0.0))

        if volatility < 0.02:
            volatility_risk = 0.20
        elif volatility < 0.04:
            volatility_risk = 0.50
        elif volatility < 0.07:
            volatility_risk = 0.75
        else:
            volatility_risk = 1.00

        signal_strength = min(abs(score), 1.0)

        confidence = signal_strength * (
            1.0 - volatility_risk * 0.50
        )

        return {
            "volatility_risk": round(volatility_risk, 4),
            "signal_strength": round(signal_strength, 4),
            "risk": round(volatility_risk, 4),
            "confidence": round(confidence, 4)
        }
