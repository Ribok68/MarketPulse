
class RiskEngineV2:

    def calculate(
        self,
        regime,
        volatility,
        confidence,
        base_risk=0.02
    ):

        regime_multiplier = {
            "BULL": 1.00,
            "BEAR": 0.50,
            "HIGH_VOLATILITY": 0.35,
            "NEUTRAL": 0.75
        }.get(regime, 0.50)

        if volatility <= 0:
            volatility_multiplier = 1.0
        elif volatility < 0.02:
            volatility_multiplier = 1.0
        elif volatility < 0.04:
            volatility_multiplier = 0.75
        elif volatility < 0.06:
            volatility_multiplier = 0.50
        else:
            volatility_multiplier = 0.25

        confidence_multiplier = max(
            0.25,
            min(1.0, float(confidence))
        )

        position_risk = (
            base_risk
            * regime_multiplier
            * volatility_multiplier
            * confidence_multiplier
        )

        return {
            "regime": regime,
            "volatility": round(float(volatility), 6),
            "confidence": round(float(confidence), 4),
            "regime_multiplier": regime_multiplier,
            "volatility_multiplier": volatility_multiplier,
            "confidence_multiplier": confidence_multiplier,
            "position_risk": round(position_risk, 6)
        }
