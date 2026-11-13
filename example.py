"""Synthetic demonstration only; names and values do not represent actual locations."""
from src.scoring import rank_locations

weights = {"demand": 0.40, "affordability": 0.35, "accessibility": 0.25}
synthetic_locations = {
    "Illustrative Site A": {"demand": 0.80, "affordability": 0.30, "accessibility": 0.75},
    "Illustrative Site B": {"demand": 0.65, "affordability": 0.70, "accessibility": 0.60},
}
for name, score in rank_locations(synthetic_locations, weights):
    print(f"{name}: {score:.1f}/100 (illustrative, unvalidated)")
