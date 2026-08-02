
class DecisionEngine:

    def decide(self, research):

        score = research.get("score", 0.0)

        if score >= 0.50:
            return "BUY"

        if score <= -0.50:
            return "SELL"

        return "HOLD"
