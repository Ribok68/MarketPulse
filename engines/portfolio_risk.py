
class PortfolioRiskEngine:

    def calculate(
        self,
        capital,
        trades,
        max_portfolio_risk=0.05,
        max_exposure=1.0
    ):

        capital = float(capital)
        max_portfolio_risk = float(max_portfolio_risk)
        max_exposure = float(max_exposure)

        if capital <= 0:
            raise ValueError("Capital moet groter dan 0 zijn.")

        total_risk = 0.0
        total_exposure = 0.0

        for trade in trades:
            total_risk += float(
                trade.get("risk_amount", 0)
            )
            total_exposure += float(
                trade.get("position_value", 0)
            )

        risk_percent = total_risk / capital
        exposure_percent = total_exposure / capital

        risk_allowed = (
            risk_percent <= max_portfolio_risk
        )

        exposure_allowed = (
            exposure_percent <= max_exposure
        )

        allowed = (
            risk_allowed
            and exposure_allowed
        )

        return {
            "capital": round(capital, 2),
            "trades": len(trades),
            "total_risk": round(total_risk, 2),
            "risk_percent": round(risk_percent * 100, 4),
            "total_exposure": round(total_exposure, 2),
            "exposure_percent": round(exposure_percent * 100, 4),
            "max_portfolio_risk": round(
                max_portfolio_risk * 100, 4
            ),
            "max_exposure": round(
                max_exposure * 100, 4
            ),
            "risk_allowed": risk_allowed,
            "exposure_allowed": exposure_allowed,
            "allowed": allowed
        }
