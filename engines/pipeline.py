
from engines.environment import EnvironmentEngine
from engines.research import ResearchEngine
from engines.memory import MemoryEngine
from engines.decision import DecisionEngine


class MarketPulsePipeline:

    def __init__(self):

        self.environment = EnvironmentEngine()
        self.research = ResearchEngine()
        self.memory = MemoryEngine()
        self.decision = DecisionEngine()


    def run(self, market):

        environment = self.environment.analyze(market)

        research = self.research.analyze({
            **market,
            **environment
        })

        decision = self.decision.decide(research)

        self.memory.remember(
            {
                "market": market,
                "environment": environment,
                "research": research
            },
            decision
        )

        return {
            "environment": environment,
            "research": research,
            "decision": decision,
            "memory": self.memory.last()
        }
