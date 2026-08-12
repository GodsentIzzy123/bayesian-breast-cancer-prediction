# Model Card (Stub) — Bayesian Breast-Cancer Prediction Research Models

**Card version:** 0.1  
**Date:** 2026-08-12  
**Owner:** Osayimwense Godsent Izinyon

## Model details

- **Type:** Research prediction models (classical baselines → Bayesian candidates)  
- **Intended use:** Method development, calibration evaluation, reproducible science — **not** clinical care  
- **Out of scope:** Diagnosis, treatment recommendations, autonomous triage in care settings

## Training data

- Current public demo: synthetic cohort only (`data/synthetic/`)  
- Future: document exact public/registry source, version, and DUA status in `docs/data.md`

## Evaluation data

Same split policy as `docs/protocol.md`. Report calibration and uncertainty, not only AUC.

## Metrics

Calibration-in-the-large, calibration slope, Brier score, discrimination secondary; decision curves only with a defined decision context.

## Ethical considerations

- No PHI in repository  
- Risk of misuse if research outputs are treated as medical devices — README and this card forbid that use  
- Subgroup analyses reported with uncertainty; avoid overclaiming equity results from sparse cells

## Caveats and recommendations

Replace this stub when a non-synthetic model is frozen; record hyperparameters, priors, seeds, and software versions used to produce the tagged release.
