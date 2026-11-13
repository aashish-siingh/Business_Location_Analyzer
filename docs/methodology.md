# Scoring methodology — research questions (not final decisions)

## Proposed candidate variables
Population, income, traffic, competitors, rent, parking, accessibility.

For each metric, document:
- Definition, units, and whether higher or lower is preferable
- Source, license, update frequency, and geographic coverage
- Trade-area radius or travel-time catchment, with justification
- Handling of outliers, missingness, uncertainty, and correlated variables

## Fairness and defensibility questions
1. Is min–max normalization appropriate across changing candidate sets, or would fixed reference bounds be more stable?
2. How should rent and competitor density be oriented? Does competition sometimes indicate demand?
3. How should weights be justified (literature, business-owner interviews, expert elicitation)?
4. What happens if a metric is missing? Do not silently treat missing as zero.
5. How stable are rankings when weights, radii, or inputs vary?
6. How should results explain tradeoffs and uncertainty?
7. How will rankings be evaluated against expert review or outcomes?

## Baseline code disclaimer
`src/scoring.py` assumes *already normalized benefit-direction values*. It does not decide the formulas or weights. Its only purpose is to demonstrate reproducible arithmetic and testing while methodology research continues.

## Decision log
| Decision | Status | Evidence needed |
| --- | --- | --- |
| Trade-area definition | Open | Literature and sensitivity tests |
| Normalization formula | Open | Comparative evaluation |
| Weight selection | Open | Expert/business-owner justification |
| Missing-data policy | Open | Coverage assessment |
| Validation approach | Open | External benchmarks or expert review |
