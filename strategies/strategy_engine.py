
import numpy as np


class StrategyEngine:

    def momentum(self, data):
        return np.where(
            data["Momentum"] > 0,
            1.0,
            0.0
        )

    def trend(self, data, fast=20, slow=50):

        fast_ma = data["Close"].rolling(fast).mean()
        slow_ma = data["Close"].rolling(slow).mean()

        return np.where(
            fast_ma > slow_ma,
            1.0,
            0.0
        )

    def mean_reversion(self, data, window=20):

        mean = data["Close"].rolling(window).mean()

        return np.where(
            data["Close"] < mean,
            1.0,
            0.0
        )

    def generate(self, data):

        result = data.copy()

        result["Momentum_Strategy"] = self.momentum(result)
        result["Trend_Strategy"] = self.trend(result)
        result["MeanReversion_Strategy"] = self.mean_reversion(result)

        return result

    def compare(self, data):

        result = self.generate(data)

        strategies = [
            "Momentum_Strategy",
            "Trend_Strategy",
            "MeanReversion_Strategy"
        ]

        output = {}

        for strategy in strategies:

            returns = (
                result[strategy].shift(1)
                * result["Return"]
            ).fillna(0)

            total_return = (
                (1 + returns).prod() - 1
            )

            volatility = returns.std()

            sharpe = (
                returns.mean()
                / volatility
                * np.sqrt(252)
                if volatility > 0
                else 0
            )

            output[strategy] = {
                "total_return": round(
                    float(total_return), 4
                ),
                "sharpe": round(
                    float(sharpe), 4
                )
            }

        return output
