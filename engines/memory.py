class MemoryEngine:
    def __init__(self):
        self.memory = []

    def remember(self, market, decision):
        self.memory.append({
            "market": market.copy(),
            "decision": decision
        })

    def last(self):
        return self.memory[-1] if self.memory else None
