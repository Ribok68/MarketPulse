
def trend_signal(market):
    trend = market.get("trend", "UNKNOWN")

    if trend == "UP":
        return 1.0
    if trend == "DOWN":
        return -1.0

    return 0.0
