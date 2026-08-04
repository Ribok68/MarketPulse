
class PerformanceEngine:

    def __init__(self):
        self.trades = []

    def record(self, decision, result):

        result = float(result)

        self.trades.append({
            "decision": decision,
            "result": result
        })

    def stats(self):

        if not self.trades:
            return {
                "trades": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0.0,
                "total_return": 0.0
            }

        wins = sum(
            1 for trade in self.trades
            if trade["result"] > 0
        )

        losses = sum(
            1 for trade in self.trades
            if trade["result"] < 0
        )

        total = len(self.trades)

        win_rate = wins / total

        total_return = sum(
            trade["result"]
            for trade in self.trades
        )

        return {
            "trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 4),
            "total_return": round(total_return, 4)
        }

    def get_trades(self):
        return self.trades.copy()
