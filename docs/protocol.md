# Research Protocol — Draft v0.1

**Title (working):** Uncertainty-Aware Bayesian Models for Breast-Cancer Risk Prediction: Calibration, Transportability, and Reproducible Evaluation  
**Author:** Osayimwense Godsent Izinyon  
**Protocol date:** 2026-08-12  
**Status:** Prespecification draft (amendments will be versioned in git)

---

## 1. Scientific question

Can Bayesian predictive models for breast-cancer–related risk (or closely related clinical endpoints supported by lawful data) produce **better-calibrated, uncertainty-aware probabilities** than transparent classical baselines under a **prespecified** evaluation protocol that includes calibration, proper scoring rules, subgroup reporting, and (where data permit) temporal / site transportability checks?

The endeavor does **not** assume that a more complex Bayesian model is always superior. Complexity must earn its keep under the same splits and metrics.

## 2. Intended contribution

1. A calibration-first evaluation framework for clinical prediction in this domain.  
2. Hierarchical / shrinkage modeling where multi-site or subgroup structure warrants partial pooling.  
3. Reproducible software artifacts (pipelines, tests, documentation patterns) that others can adapt.

## 3. Population and outcome (to be locked to a specific lawful dataset)

**Population (conceptual):** Adult women (or the cohort definition required by the chosen public dataset) at risk of breast cancer or evaluated in a screening / diagnostic / prognostic pathway consistent with the data dictionary.

**Primary endpoint (example classes; one will be locked before model comparison):**

- Incident diagnosis within a defined horizon; **or**
- Stage / advanced-disease marker available in the source; **or**
- Recurrence / related time-to-event endpoint if follow-up supports valid analysis.

**Final population, inclusion/exclusion, and endpoint** will be fixed in `docs/data.md` when a specific public source (e.g., SEER research files under terms, or another lawful public cohort) is selected. Until then, development uses **synthetic data only**.

## 4. Predictors

Candidate predictors will be limited to variables that are:

- Available at the intended prediction time (no leakage);
- Documented in the data dictionary;
- Ethically and legally permissible to analyze under the source terms.

Examples of *classes* of predictors (not a final list): age, screening history proxies, tumor/pathology features when predicting prognosis (not risk), socioeconomic or geographic proxies **only if** present and appropriate for the scientific question.

## 5. Missing data

Prespecified options (choose one primary strategy before fitting comparison models):

1. Complete-case analysis with reporting of missingness rates; or  
2. Multiple imputation with imputation model documented; or  
3. Model-based handling where the likelihood supports it.

Sensitivity analyses will be described in an amendment if needed.

## 6. Validation design

- Train / test split or nested cross-validation with a locked random seed.  
- Where calendar time exists: **temporal validation**.  
- Where site / registry structure exists: **leave-site-out** or grouped evaluation.  
- Subgroup metrics reported with **sample sizes and uncertainty**; unstable subgroup estimates will not be over-interpreted.

## 7. Models

**Baselines (required first):**

- Logistic regression (binary endpoints) and/or Cox / other standard survival baselines for time-to-event endpoints.

**Bayesian candidates (after baselines run):**

- Bayesian GLM with weakly informative priors;  
- Hierarchical models with partial pooling across sites/subgroups when structure exists;  
- Optional shrinkage priors for higher-dimensional predictor sets.

## 8. Metrics (prespecified)

| Domain | Metrics |
| --- | --- |
| Calibration | Calibration-in-the-large, calibration slope, reliability plots |
| Proper scoring | Brier score (binary); analogous proper scores for survival if used |
| Discrimination | AUC / C-index (secondary to calibration for this endeavor’s claims) |
| Decision utility | Decision-curve / net benefit **only if** a decision threshold context is defined |
| Uncertainty | Posterior intervals; interval coverage checks on held-out data where applicable |

## 9. Software and reproducibility

- Version-controlled analysis code in this repository.  
- Environment file (`environment.yml` / `requirements.txt`).  
- Automated tests for core metric helpers.  
- Model card / documentation stub updated when a non-synthetic model is fit.

## 10. Ethics and limitations

- No PHI in this repository.  
- No claim of clinical safety, FDA clearance, or readiness for care delivery.  
- Results on synthetic data demonstrate **pipeline readiness**, not clinical performance.

## 11. Amendment log

| Version | Date | Change |
| --- | --- | --- |
| v0.1 | 2026-08-12 | Initial prespecification draft committed to git |
