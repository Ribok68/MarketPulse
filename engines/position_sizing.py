
class PositionSizingEngine:

    def calculate(
        self,
        capital,
        price,
        position_risk,
        stop_distance
    ):

        capital = float(capital)
        price = float(price)
        position_risk = float(position_risk)
        stop_distance = float(stop_distance)

        if capital <= 0:
            raise ValueError("Capital moet groter dan 0 zijn.")

        if price <= 0:
            raise ValueError("Price moet groter dan 0 zijn.")

        if stop_distance <= 0:
            raise ValueError(
                "Stop distance moet groter dan 0 zijn."
            )

        risk_amount = capital * position_risk

        units = risk_amount / stop_distance

        position_value = units * price

        exposure = position_value / capital

        return {
            "capital": round(capital, 2),
            "price": round(price, 2),
            "risk_percent": round(position_risk * 100, 4),
            "risk_amount": round(risk_amount, 2),
            "stop_distance": round(stop_distance, 2),
            "units": round(units, 6),
            "position_value": round(position_value, 2),
            "exposure": round(exposure, 4)
        }
