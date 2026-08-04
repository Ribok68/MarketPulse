
class LearningEngine:

    def __init__(self):
        self.weights = {
            "trend": 0.40,
            "volatility": 0.20,
            "momentum": 0.40
        }

        self.learning_rate = 0.05
        self.history = []

    def record_result(self, signals, result):

        result = float(result)

        self.history.append({
            "signals": signals.copy(),
            "result": result
        })

        for name in self.weights:

            signal = float(signals.get(name, 0.0))

            adjustment = (
                self.learning_rate
                * signal
                * result
            )

            self.weights[name] += adjustment

        self._normalize_weights()

    def _normalize_weights(self):

        total = sum(abs(v) for v in self.weights.values())

        if total == 0:
            return

        for name in self.weights:
            self.weights[name] = round(
                abs(self.weights[name]) / total,
                4
            )

    def get_weights(self):
        return self.weights.copy()

    def get_history(self):
        return self.history.copy()
