
class TakeProfitEngine:

    def calculate(
        self,
        price,
        stop_price,
        risk_reward=2.0,
        direction="LONG"
    ):

        price = float(price)
        stop_price = float(stop_price)
        risk_reward = float(risk_reward)

        if price <= 0:
            raise ValueError("Price moet groter dan 0 zijn.")

        if stop_price <= 0:
            raise ValueError("Stop price moet groter dan 0 zijn.")

        if risk_reward <= 0:
            raise ValueError(
                "Risk/reward moet groter dan 0 zijn."
            )

        direction = direction.upper()

        if direction == "LONG":

            risk = price - stop_price

            if risk <= 0:
                raise ValueError(
                    "Voor LONG moet stop_price onder price liggen."
                )

            reward = risk * risk_reward
            take_profit = price + reward

        elif direction == "SHORT":

            risk = stop_price - price

            if risk <= 0:
                raise ValueError(
                    "Voor SHORT moet stop_price boven price liggen."
                )

            reward = risk * risk_reward
            take_profit = price - reward

        else:

            raise ValueError(
                "Direction moet LONG of SHORT zijn."
            )

        return {
            "price": round(price, 2),
            "stop_price": round(stop_price, 2),
            "risk": round(risk, 2),
            "risk_reward": round(risk_reward, 2),
            "reward": round(reward, 2),
            "direction": direction,
            "take_profit": round(take_profit, 2)
        }
