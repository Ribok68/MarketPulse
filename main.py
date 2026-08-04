
from engines.pipeline import MarketPulsePipeline

market = {
    "trend": "UP",
    "volatility": 0.021,
    "momentum": 0.75
}

pipeline = MarketPulsePipeline()

print()
print("========================================")
print("        MARKETPULSE V4.3")
print("========================================")

# Analyse
analysis = pipeline.run(market)

print()
print("ENVIRONMENT:")
print(analysis["environment"])

print()
print("RESEARCH:")
print(analysis["research"])

print()
print("RISK:")
print(analysis["risk"])

print()
print("DECISION:")
print(analysis["decision"])

print()
print("INITIAL WEIGHTS:")
print(analysis["learning_weights"])

# Simuleer een echte trade-uitkomst
trade_result = 1.0

# Feedback verwerken
updated = pipeline.run(
    market,
    result=trade_result
)

print()
print("FEEDBACK:")
print(updated["feedback"])

print()
print("UPDATED WEIGHTS:")
print(updated["learning_weights"])

print()
print("MEMORY:")
print(updated["memory"])

print()
print("========================================")
