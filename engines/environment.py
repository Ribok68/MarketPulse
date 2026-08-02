class EnvironmentEngine:
    def analyze(self, market):
        return {
            "trend": market.get("trend", "UNKNOWN"),
            "volatility": market.get("volatility", 0),
            "status": "OK"
        }
