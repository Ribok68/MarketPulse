
class UnifiedPipeline:

    def __init__(
        self,
        regime_engine,
        strategy_selector,
        risk_engine,
        position_engine,
        stop_loss_engine,
        take_profit_engine,
        portfolio_risk_engine,
        allocation_engine,
        decision_engine
    ):

        self.regime_engine = regime_engine
        self.strategy_selector = strategy_selector
        self.risk_engine = risk_engine
        self.position_engine = position_engine
        self.stop_loss_engine = stop_loss_engine
        self.take_profit_engine = take_profit_engine
        self.portfolio_risk_engine = portfolio_risk_engine
        self.allocation_engine = allocation_engine
        self.decision_engine = decision_engine

    def run(
        self,
        market,
        research,
        strategy_performance,
        capital=10000.0,
        direction="LONG"
    ):

        regime = self.regime_engine.analyze(market)
        regime_name = regime["regime"]

        selected_strategy = self.strategy_selector.select(
            regime=regime_name,
            performance=strategy_performance
        )

        risk = self.risk_engine.calculate(
            regime=regime_name,
            volatility=market["volatility"],
            confidence=research.get("confidence", 0.60)
        )

        stop_loss = self.stop_loss_engine.calculate(
            price=market["price"],
            volatility=market["volatility"],
            direction=direction
        )

        position = self.position_engine.calculate(
            capital=capital,
            price=market["price"],
            position_risk=risk["position_risk"],
            stop_distance=stop_loss["stop_distance"]
        )

        take_profit = self.take_profit_engine.calculate(
            price=market["price"],
            stop_price=stop_loss["stop_price"],
            direction=direction
        )

        portfolio = self.portfolio_risk_engine.calculate(
            capital=capital,
            trades=[position]
        )

        allocation = self.allocation_engine.allocate(
            capital=capital,
            trades=[position]
        )

        decision = self.decision_engine.decide(
            market=market,
            regime=regime,
            research=research,
            strategy=selected_strategy,
            risk=risk,
            position=position,
            stop_loss=stop_loss,
            take_profit=take_profit,
            portfolio=portfolio
        )

        return {
            "decision": decision,
            "allocation": allocation
        }
