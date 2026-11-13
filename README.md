# Business Location Analyzer

**Status: Research in progress · Prototype scaffold (not a deployed or validated recommendation system)**

A funded undergraduate research project exploring how to compare potential small-business locations fairly, transparently, and reproducibly.

**Researcher:** Aashish Singh · Honors MIS, Minnesota State University, Mankato  
**Support:** Foundation Grant ($1,500 stipend + $500 supplies)

## The problem
Business owners must weigh multiple, sometimes conflicting location factors. This project investigates defensible ways to define, normalize, weight, and compare those factors before presenting a location recommendation.

## Current scope
Candidate factors include population, income, traffic, competition, rent, parking, and accessibility. Their definitions, geographical catchment areas, data sources, treatment of missing observations, and weights are **not finalized**.

This repository is a **starter research scaffold**, not the researcher's original Streamlit prototype. The included Python example implements an illustrative weighted-scoring calculation using synthetic input values. It is **not** a validated methodology or a real-world recommendation.

## Run the illustrative calculation
Requires Python 3.10+.

```bash
python -m unittest discover -s tests -v
python example.py
```

No external packages are required for this starter. A Streamlit application may be added after the researcher's existing `app.py` is available.

## Repository map
- `src/scoring.py`: transparent, small illustrative scoring function
- `tests/test_scoring.py`: tests for bounds, weights, missing values, and ranking
- `example.py`: clearly synthetic sample inputs
- `docs/methodology.md`: research questions and decisions still to validate
- `docs/roadmap.md`: proposed development milestones
- `data/README.md`: data provenance rules

## What is not claimed
- No live deployment or real customer adoption
- No measured time savings or business outcomes
- No validated optimal weights, radius, or competitor definition
- No claim that synthetic scores reflect actual Mankato sites

## Next steps
1. Incorporate the original Streamlit prototype after reviewing its source.
2. Define every metric, unit, geographic radius, and data source.
3. Evaluate normalization choices and missing-data policies.
4. Perform sensitivity analysis and benchmark against expert judgments or historical outcomes.
5. Publish a reproducible demo only when limitations are clearly stated.

## Portfolio context
This is an ongoing research project focused on **explainable decision support**, not an automated site-selection authority.
