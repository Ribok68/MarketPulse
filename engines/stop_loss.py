
class StopLossEngine:

    def calculate(
        self,
        price,
        volatility,
        multiplier=2.0,
        direction="LONG"
    ):

        price = float(price)
        volatility = float(volatility)
        multiplier = float(multiplier)

        if price <= 0:
            raise ValueError("Price moet groter dan 0 zijn.")

        if volatility < 0:
            raise ValueError("Volatility mag niet negatief zijn.")

        if multiplier <= 0:
            raise ValueError("Multiplier moet groter dan 0 zijn.")

        distance = price * volatility * multiplier

        if direction.upper() == "LONG":

            stop_price = price - distance

        elif direction.upper() == "SHORT":

            stop_price = price + distance

        else:

            raise ValueError(
                "Direction moet LONG of SHORT zijn."
            )

        return {
            "price": round(price, 2),
            "volatility": round(volatility, 6),
            "multiplier": round(multiplier, 2),
            "direction": direction.upper(),
            "stop_distance": round(distance, 2),
            "stop_price": round(stop_price, 2)
        }
