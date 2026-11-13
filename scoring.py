"""Illustrative scoring baseline only; NOT a validated research methodology."""
from math import isfinite

def score_location(metrics: dict[str, float], weights: dict[str, float]) -> float:
    """Return a 0–100 weighted score from pre-normalized 0–1 benefit metrics.

    Every metric is assumed to have already been oriented so higher is better.
    This does not determine normalization, fair weights, or geographic scope.
    """
    if not weights:
        raise ValueError("At least one weight is required")
    if set(metrics) != set(weights):
        raise ValueError("Metric and weight keys must match; missing data requires explicit policy")
    if any(not isfinite(v) or v < 0 or v > 1 for v in metrics.values()):
        raise ValueError("Metrics must be finite, pre-normalized values from 0 to 1")
    if any(not isfinite(w) or w < 0 for w in weights.values()):
        raise ValueError("Weights must be finite and nonnegative")
    total = sum(weights.values())
    if abs(total - 1.0) > 1e-9:
        raise ValueError("Weights must sum to 1.0")
    return 100 * sum(metrics[k] * weights[k] for k in weights)

def rank_locations(locations: dict[str, dict[str, float]], weights: dict[str, float]):
    """Rank synthetic or properly normalized inputs, highest score first."""
    return sorted(
        ((name, score_location(metrics, weights)) for name, metrics in locations.items()),
        key=lambda item: (-item[1], item[0]),
    )
