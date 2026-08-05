
class TradeManager:

    def create_trade(
        self,
        capital,
        price,
        position_risk,
        stop_price,
        take_profit,
        direction="LONG"
    ):

        capital = float(capital)
        price = float(price)
        position_risk = float(position_risk)
        stop_price = float(stop_price)
        take_profit = float(take_profit)

        direction = direction.upper()

        if capital <= 0:
            raise ValueError("Capital moet groter dan 0 zijn.")

        if price <= 0:
            raise ValueError("Price moet groter dan 0 zijn.")

        risk_amount = capital * position_risk

        if direction == "LONG":

            risk_per_unit = price - stop_price

            if risk_per_unit <= 0:
                raise ValueError(
                    "LONG: stop_price moet onder entry liggen."
                )

        elif direction == "SHORT":

            risk_per_unit = stop_price - price

            if risk_per_unit <= 0:
                raise ValueError(
                    "SHORT: stop_price moet boven entry liggen."
                )

        else:
            raise ValueError(
                "Direction moet LONG of SHORT zijn."
            )

        units = risk_amount / risk_per_unit

        position_value = units * price

        if direction == "LONG":
            reward_per_unit = take_profit - price
        else:
            reward_per_unit = price - take_profit

        reward_amount = units * reward_per_unit

        risk_reward = (
            reward_amount / risk_amount
            if risk_amount > 0
            else 0
        )

        return {
            "direction": direction,
            "capital": round(capital, 2),
            "entry": round(price, 2),
            "units": round(units, 6),
            "position_value": round(position_value, 2),
            "risk_amount": round(risk_amount, 2),
            "stop_loss": round(stop_price, 2),
            "take_profit": round(take_profit, 2),
            "reward_amount": round(reward_amount, 2),
            "risk_reward": round(risk_reward, 4)
        }
