
class StrategySelector:

    def select(self, regime, performance):

        if not performance:
            raise ValueError("Geen strategie-data beschikbaar.")

        # Regime voorkeuren
        preferences = {
            "BULL": [
                "Momentum_Strategy",
                "Trend_Strategy",
                "MeanReversion_Strategy"
            ],
            "BEAR": [
                "MeanReversion_Strategy",
                "Momentum_Strategy",
                "Trend_Strategy"
            ],
            "HIGH_VOLATILITY": [
                "MeanReversion_Strategy",
                "Momentum_Strategy",
                "Trend_Strategy"
            ],
            "NEUTRAL": [
                "Momentum_Strategy",
                "MeanReversion_Strategy",
                "Trend_Strategy"
            ]
        }

        order = preferences.get(
            regime,
            list(performance.keys())
        )

        available = [
            name for name in order
            if name in performance
        ]

        if not available:
            available = list(performance.keys())

        # Selecteer op Sharpe
        selected = max(
            available,
            key=lambda name: performance[name]["sharpe"]
        )

        return {
            "regime": regime,
            "selected_strategy": selected,
            "performance": performance[selected]
        }
