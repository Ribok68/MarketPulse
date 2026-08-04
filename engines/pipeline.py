
from engines.environment import EnvironmentEngine
from engines.research import ResearchEngine
from engines.risk import RiskEngine
from engines.learning import LearningEngine
from engines.feedback import FeedbackEngine
from engines.memory import MemoryEngine
from engines.decision import DecisionEngine


class MarketPulsePipeline:

    def __init__(self):

        self.environment = EnvironmentEngine()
        self.learning = LearningEngine()
        self.research = ResearchEngine(self.learning)
        self.risk = RiskEngine()
        self.feedback = FeedbackEngine(self.learning)
        self.memory = MemoryEngine()
        self.decision = DecisionEngine()

    def run(self, market, result=None):

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

        feedback = None

        if result is not None:

            feedback = self.feedback.process(
                research["signals"],
                result
            )

        self.memory.remember(
            {
                "market": market,
                "environment": environment,
                "research": research,
                "risk": risk,
                "feedback": feedback,
                "learning_weights": self.learning.get_weights()
            },
            decision
        )

        return {
            "environment": environment,
            "research": research,
            "risk": risk,
            "feedback": feedback,
            "decision": decision,
            "learning_weights": self.learning.get_weights(),
            "memory": self.memory.last()
        }
