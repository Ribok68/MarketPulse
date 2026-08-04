
class TrainingEngine:

    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.history = []

    def run_training(self, samples):

        results = []

        for sample in samples:

            market = sample["market"]
            outcome = float(sample["result"])

            result = self.pipeline.run(
                market,
                result=outcome
            )

            record = {
                "market": market.copy(),
                "decision": result["decision"],
                "result": outcome,
                "feedback": result["feedback"],
                "weights": result["learning_weights"]
            }

            self.history.append(record)
            results.append(record)

        return results

    def get_history(self):
        return self.history.copy()
