
class UnifiedDecisionEngine:

    def decide(
        self,
        market,
        regime,
        research,
        strategy,
        risk,
        position,
        stop_loss,
        take_profit,
        portfolio
    ):

        score = float(
            research.get("score", 0)
        )

        confidence = float(
            risk.get("confidence", 0)
        )

        portfolio_allowed = bool(
            portfolio.get("allowed", False)
        )

        decision = "HOLD"

        if (
            score >= 0.70
            and confidence >= 0.60
            and portfolio_allowed
        ):
            decision = "BUY"

        elif (
            score <= -0.70
            and confidence >= 0.60
            and portfolio_allowed
        ):
            decision = "SELL"

        return {
            "decision": decision,
            "market": market,
            "regime": regime,
            "strategy": strategy,
            "research_score": round(score, 4),
            "confidence": round(confidence, 4),
            "risk": risk,
            "position": position,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "portfolio": portfolio
        }
