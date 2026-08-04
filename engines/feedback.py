
class FeedbackEngine:

    def __init__(self, learning_engine):

        self.learning = learning_engine
        self.results = []

    def process(self, signals, result):

        result = float(result)

        if result > 0:
            outcome = "WIN"

        elif result < 0:
            outcome = "LOSS"

        else:
            outcome = "NEUTRAL"

        self.results.append({
            "signals": signals.copy(),
            "result": result,
            "outcome": outcome
        })

        self.learning.record_result(
            signals,
            result
        )

        return {
            "result": result,
            "outcome": outcome,
            "weights": self.learning.get_weights()
        }

    def get_results(self):

        return self.results.copy()
