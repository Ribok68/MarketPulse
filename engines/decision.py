
class DecisionEngine:

    def decide(self, data):

        score = float(data.get("score", 0.0))
        confidence = float(data.get("confidence", 0.0))
        risk = float(data.get("risk", 1.0))

        if score >= 0.50 and confidence >= 0.50 and risk < 0.75:
            return "BUY"

        if score <= -0.50 and confidence >= 0.50 and risk < 0.75:
            return "SELL"

        return "HOLD"
