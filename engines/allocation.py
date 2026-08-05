
class PortfolioAllocationEngine:

    def allocate(
        self,
        capital,
        trades,
        max_exposure=1.0
    ):

        capital = float(capital)
        max_exposure = float(max_exposure)

        if capital <= 0:
            raise ValueError("Capital moet groter dan 0 zijn.")

        if max_exposure <= 0:
            raise ValueError(
                "Max exposure moet groter dan 0 zijn."
            )

        max_value = capital * max_exposure

        requested = []

        for trade in trades:

            requested_value = float(
                trade.get("position_value", 0)
            )

            requested.append(
                max(0.0, requested_value)
            )

        total_requested = sum(requested)

        if total_requested <= max_value:

            allocations = requested

        else:

            scale = max_value / total_requested

            allocations = [
                value * scale
                for value in requested
            ]

        result = []

        for i, value in enumerate(allocations):

            result.append({
                "trade": i + 1,
                "requested_value": round(
                    requested[i], 2
                ),
                "allocated_value": round(
                    value, 2
                ),
                "allocation_percent": round(
                    value / capital * 100,
                    4
                )
            })

        total_allocated = sum(
            item["allocated_value"]
            for item in result
        )

        return {
            "capital": round(capital, 2),
            "max_exposure": round(
                max_exposure * 100,
                4
            ),
            "requested_total": round(
                total_requested,
                2
            ),
            "allocated_total": round(
                total_allocated,
                2
            ),
            "trades": result
        }
