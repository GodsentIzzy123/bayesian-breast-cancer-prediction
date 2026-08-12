# Bayesian Breast-Cancer Prediction — Research Repository

**Petitioner / author:** Osayimwense Godsent Izinyon  
**Purpose:** Reproducible research infrastructure for uncertainty-aware Bayesian modeling of breast-cancer risk / related clinical prediction endpoints, with transparent classical baselines, calibration-first evaluation, and software-ready analysis pipelines.

This repository is **research infrastructure**, not a medical device or clinical decision-support product. It does not provide medical advice and is not intended for patient care use.

## Status (started August 2026)

| Artifact | Location | Status |
| --- | --- | --- |
| Research protocol | [`docs/protocol.md`](docs/protocol.md) | Draft v0.1 |
| Data / access plan | [`docs/data.md`](docs/data.md) | Draft v0.1 |
| Manuscript outline | [`docs/manuscript-outline.md`](docs/manuscript-outline.md) | Draft v0.1 |
| Model card stub | [`docs/model-card.md`](docs/model-card.md) | Stub |
| Baseline notebook | [`notebooks/01_baseline_logistic_calibration.ipynb`](notebooks/01_baseline_logistic_calibration.ipynb) | Synthetic demo |
| Environment | [`environment.yml`](environment.yml), [`requirements.txt`](requirements.txt) | Defined |
| Tests | [`tests/`](tests/) | Smoke tests |

## Design principles (aligned to the proposed endeavor)

1. **Prespecify before comparing.** Population, outcome, predictors, splits, and metrics are written down before model shopping.
2. **Calibration before novelty.** Discrimination alone is not enough; calibration, proper scoring rules, and uncertainty are first-class.
3. **Baselines first.** Transparent classical models run before hierarchical / fully Bayesian extensions.
4. **No restricted data in git.** Only synthetic or explicitly public demonstration data live in this repository.
5. **Reproducible environments.** Dependencies are pinned; key calculations are tested.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
jupyter lab notebooks/01_baseline_logistic_calibration.ipynb
```

Or with conda:

```bash
conda env create -f environment.yml
conda activate bbc-prediction
```

## Repository map

```
docs/           Protocol, data plan, manuscript outline, model card
notebooks/      Analysis notebooks (baselines → Bayesian)
src/bbc/        Small reusable Python helpers
data/synthetic/ Public synthetic demo data only
tests/          Unit / smoke tests
```

## Citation

If you use this repository, please cite the repository URL and version/tag, and the author's related peer-reviewed prediction / clinical-embedding work as appropriate.

## License

Code is released under the MIT License (see [`LICENSE`](LICENSE)). Documentation may be reused with attribution. Do not represent analyses from this repo as clinically validated tools.
