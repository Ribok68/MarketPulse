
import pandas as pd
import yfinance as yf


class MarketDataEngine:

    def __init__(self):
        self.data = None

    def load(self, ticker, period="5y", interval="1d"):

        df = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            raise ValueError(
                f"Geen marktdata gevonden voor {ticker}"
            )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.dropna()

        required = ["Open", "High", "Low", "Close", "Volume"]

        missing = [
            column for column in required
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Ontbrekende kolommen: {missing}"
            )

        df["Return"] = df["Close"].pct_change()

        df["Volatility"] = (
            df["Return"]
            .rolling(20)
            .std()
        )

        df["Momentum"] = (
            df["Close"]
            .pct_change(20)
        )

        df = df.dropna()

        self.data = df

        return df

    def latest(self):

        if self.data is None or self.data.empty:
            return None

        row = self.data.iloc[-1]

        return {
            "close": float(row["Close"]),
            "return": float(row["Return"]),
            "volatility": float(row["Volatility"]),
            "momentum": float(row["Momentum"])
        }

    def get_data(self):

        return self.data.copy()
