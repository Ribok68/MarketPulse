
def momentum_signal(market):
    momentum = float(market.get("momentum", 0.0))

    if momentum > 0:
        return 1.0

    if momentum < 0:
        return -1.0

    return 0.0
