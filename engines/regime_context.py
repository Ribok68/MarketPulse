
class RegimeContextEngine:

    def apply(self, regime_data, research, risk):

        regime = regime_data["regime"]

        research = research.copy()
        risk = risk.copy()

        if regime == "BULL":
            research["regime_bias"] = 1.0
            risk["regime_risk_multiplier"] = 0.90

        elif regime == "BEAR":
            research["regime_bias"] = -1.0
            risk["regime_risk_multiplier"] = 1.25

        elif regime == "HIGH_VOLATILITY":
            research["regime_bias"] = 0.0
            risk["regime_risk_multiplier"] = 1.50

        else:
            research["regime_bias"] = 0.0
            risk["regime_risk_multiplier"] = 1.00

        risk["adjusted_risk"] = round(
            risk["risk"] * risk["regime_risk_multiplier"],
            4
        )

        return {
            "regime": regime,
            "research": research,
            "risk": risk
        }
