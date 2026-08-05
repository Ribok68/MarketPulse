
import pandas as pd
import numpy as np


class BacktestEngine:

    def __init__(self, initial_capital=10000.0):

        self.initial_capital = float(initial_capital)

    def run(self, data, signal_column="Signal"):

        df = data.copy()

        if signal_column not in df.columns:
            raise ValueError(
                f"Kolom '{signal_column}' ontbreekt."
            )

        df["Strategy_Return"] = (
            df[signal_column].shift(1)
            * df["Return"]
        )

        df["Strategy_Return"] = (
            df["Strategy_Return"].fillna(0.0)
        )

        df["Equity"] = (
            self.initial_capital
            * (1.0 + df["Strategy_Return"]).cumprod()
        )

        df["BuyHold_Equity"] = (
            self.initial_capital
            * (1.0 + df["Return"].fillna(0.0)).cumprod()
        )

        running_max = df["Equity"].cummax()

        df["Drawdown"] = (
            df["Equity"] / running_max
        ) - 1.0

        final_equity = float(df["Equity"].iloc[-1])

        total_return = (
            final_equity / self.initial_capital
        ) - 1.0

        max_drawdown = float(
            df["Drawdown"].min()
        )

        daily_returns = df["Strategy_Return"]

        volatility = float(
            daily_returns.std() * np.sqrt(252)
        )

        if volatility > 0:
            sharpe = float(
                daily_returns.mean()
                / daily_returns.std()
                * np.sqrt(252)
            )
        else:
            sharpe = 0.0

        wins = int(
            (daily_returns > 0).sum()
        )

        losses = int(
            (daily_returns < 0).sum()
        )

        trades = wins + losses

        win_rate = (
            wins / trades
            if trades > 0
            else 0.0
        )

        metrics = {
            "initial_capital": self.initial_capital,
            "final_equity": round(final_equity, 2),
            "total_return": round(total_return, 4),
            "max_drawdown": round(max_drawdown, 4),
            "volatility": round(volatility, 4),
            "sharpe": round(sharpe, 4),
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 4)
        }

        return {
            "data": df,
            "metrics": metrics
        }
