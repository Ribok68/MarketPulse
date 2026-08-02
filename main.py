
from engines.pipeline import MarketPulsePipeline


market = {
    "trend": "UP",
    "volatility": 0.021,
    "momentum": 0.75
}


pipeline = MarketPulsePipeline()

result = pipeline.run(market)


print()
print("========================================")
print("        MARKETPULSE V4")
print("========================================")

print("ENVIRONMENT:")
print(result["environment"])

print()
print("RESEARCH:")
print(result["research"])

print()
print("DECISION:")
print(result["decision"])

print()
print("MEMORY:")
print(result["memory"])

print("========================================")
