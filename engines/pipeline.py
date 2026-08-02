
from engines.environment import EnvironmentEngine
from engines.research import ResearchEngine
from engines.risk import RiskEngine
from engines.memory import MemoryEngine
from engines.decision import DecisionEngine


class MarketPulsePipeline:

    def __init__(self):
        self.environment = EnvironmentEngine()
        self.research = ResearchEngine()
        self.risk = RiskEngine()
        self.memory = MemoryEngine()
        self.decision = DecisionEngine()

    def run(self, market):

        environment = self.environment.analyze(market)

        research = self.research.analyze({
            **market,
            **environment
        })

        risk = self.risk.analyze(
            market,
            research
        )

        decision = self.decision.decide({
            **research,
            **risk
        })

        self.memory.remember(
            {
                "market": market,
                "environment": environment,
                "research": research,
                "risk": risk
            },
            decision
        )

        return {
            "environment": environment,
            "research": research,
            "risk": risk,
            "decision": decision,
            "memory": self.memory.last()
        }
