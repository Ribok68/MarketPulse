
def volatility_signal(market):
    volatility = float(market.get("volatility", 0.0))

    # Lage volatiliteit = gunstiger omgeving.
    if volatility < 0.02:
        return 1.0

    if volatility < 0.04:
        return 0.0

    return -1.0
