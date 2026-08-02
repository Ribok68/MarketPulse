from engines.pipeline import MarketPulsePipeline

market = {
    "trend": "UP",
    "volatility": 0.021
}

pipeline = MarketPulsePipeline()
result = pipeline.run(market)

print("========== MARKETPULSE V3 ==========")
print("ENVIRONMENT:", result["environment"])
print("DECISION:", result["decision"])
print("MEMORY:", result["memory"])
