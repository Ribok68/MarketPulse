
import numpy as np


class WalkForwardEngine:

    def __init__(
        self,
        train_size=500,
        test_size=100
    ):

        self.train_size = int(train_size)
        self.test_size = int(test_size)

    def run(
        self,
        data,
        signal_column="Signal"
    ):

        df = data.copy()

        if signal_column not in df.columns:
            raise ValueError(
                f"Kolom '{signal_column}' ontbreekt."
            )

        results = []

        start = 0

        while (
            start
            + self.train_size
            + self.test_size
            <= len(df)
        ):

            train_end = (
                start
                + self.train_size
            )

            test_end = (
                train_end
                + self.test_size
            )

            train = df.iloc[
                start:train_end
            ]

            test = df.iloc[
                train_end:test_end
            ].copy()

            test["Strategy_Return"] = (
                test[signal_column].shift(1)
                * test["Return"]
            )

            test["Strategy_Return"] = (
                test["Strategy_Return"]
                .fillna(0.0)
            )

            strategy_return = float(
                (1.0 + test["Strategy_Return"])
                .prod() - 1.0
            )

            buy_hold_return = float(
                (1.0 + test["Return"].fillna(0.0))
                .prod() - 1.0
            )

            results.append({
                "train_start": str(train.index[0]),
                "train_end": str(train.index[-1]),
                "test_start": str(test.index[0]),
                "test_end": str(test.index[-1]),
                "train_rows": len(train),
                "test_rows": len(test),
                "strategy_return": strategy_return,
                "buy_hold_return": buy_hold_return
            })

            start += self.test_size

        if not results:
            raise ValueError(
                "Niet genoeg data voor walk-forward testing."
            )

        strategy_returns = np.array([
            x["strategy_return"]
            for x in results
        ])

        benchmark_returns = np.array([
            x["buy_hold_return"]
            for x in results
        ])

        summary = {
            "windows": len(results),
            "strategy_total": float(
                np.prod(1.0 + strategy_returns) - 1.0
            ),
            "buy_hold_total": float(
                np.prod(1.0 + benchmark_returns) - 1.0
            ),
            "average_window_return": float(
                strategy_returns.mean()
            ),
            "winning_windows": int(
                (strategy_returns > 0).sum()
            ),
            "losing_windows": int(
                (strategy_returns < 0).sum()
            )
        }

        return {
            "windows": results,
            "summary": summary
        }
