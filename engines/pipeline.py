from engines.environment import EnvironmentEngine
from engines.memory import MemoryEngine
from engines.decision import DecisionEngine

class MarketPulsePipeline:
    def __init__(self):
        self.environment = EnvironmentEngine()
        self.memory = MemoryEngine()
        self.decision = DecisionEngine()

    def run(self, market):
        environment = self.environment.analyze(market)
        decision = self.decision.decide(environment)

        self.memory.remember(environment, decision)

        return {
            "environment": environment,
            "decision": decision,
            "memory": self.memory.last()
        }
