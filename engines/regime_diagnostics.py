import pandas as pd


class RegimeDiagnosticsEngine:

    def analyze(self, data):

        df = data.copy()

        regimes = []

        for _, row in df.iterrows():

            volatility = float(row.get("Volatility", 0.0))
            trend = float(row.get("Return", 0.0))
            momentum = float(row.get("Momentum", 0.0))

            if volatility >= 0.04:
                regime = "HIGH_VOLATILITY"
            else:
                regime = "NEUTRAL"

            regimes.append({
                "regime": regime,
                "trend": trend,
                "volatility": volatility,
                "momentum": momentum
            })

        result = pd.DataFrame(regimes)

        summary = (
            result
            .groupby("regime")
            .agg(
                samples=("regime", "size"),
                avg_trend=("trend", "mean"),
                avg_volatility=("volatility", "mean"),
                avg_momentum=("momentum", "mean")
            )
            .reset_index()
        )

        summary["percentage"] = (
            summary["samples"] / len(result) * 100
        )

        return summary
