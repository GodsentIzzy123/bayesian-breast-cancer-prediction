# Bayesian Model Notes (Draft)

**Purpose:** Compact reference for the uncertainty-aware models in this repository.  
**Status:** Methods note for research infrastructure — **not** a clinical model card for deployed care.  
**Date:** 2026-08-12

Figures below are generated from **synthetic** data / conjugate toy examples (`scripts/make_figures.py`).

---

## 1. Why Bayesian for breast-cancer prediction?

Classical point estimates answer “what is the best guess?”  
Bayesian inference answers “what is the distribution of plausible risks given the data and a prior?”

That matters for calibration, subgroup uncertainty, and honest communication of limited evidence.

---

## 2. Binary risk model (logistic likelihood)

For person \(i\), let \(Y_i \in \{0,1\}\) be the event indicator and \(x_i\) predictors:

\[
Y_i \mid x_i, \beta \sim \mathrm{Bernoulli}\!\left(\pi_i\right),
\qquad
\pi_i = \sigma(x_i^\top \beta) = \frac{1}{1 + e^{-x_i^\top \beta}}.
\]

Likelihood for a sample:

\[
p(y \mid X, \beta) = \prod_{i=1}^n \pi_i^{y_i}\,(1-\pi_i)^{1-y_i}.
\]

---

## 3. Prior and posterior

Place a prior on coefficients, e.g. weakly informative Gaussian shrinkage:

\[
\beta_j \sim \mathcal{N}(0, \tau^2).
\]

Posterior:

\[
p(\beta \mid y, X) \propto p(y \mid X, \beta)\,p(\beta).
\]

For reporting, we typically summarize posterior means / medians and credible intervals, not only a MAP point.

---

## 4. Posterior predictive risk

For a new case \(x_{\mathrm{new}}\):

\[
p(y_{\mathrm{new}}=1 \mid x_{\mathrm{new}}, y, X)
=
\int \sigma(x_{\mathrm{new}}^\top \beta)\,
p(\beta \mid y, X)\,d\beta.
\]

This integral is the Bayesian predictive probability — the quantity we calibrate against observed event rates.

---

## 5. Hierarchical / partial-pooling sketch (multi-site or subgroup)

If site (or subgroup) \(s\) has its own intercept:

\[
\begin{aligned}
\beta_{0s} &\sim \mathcal{N}(\mu_0, \sigma_0^2), \\
\mu_0 &\sim \mathcal{N}(0, \tau_\mu^2), \\
\sigma_0 &\sim \mathrm{HalfNormal}(\cdot).
\end{aligned}
\]

Partial pooling shrinks unstable site estimates toward \(\mu_0\) instead of fitting fully separate models.

---

## 6. Conjugate warm-up: Beta–Binomial

For a simple proportion \(\theta\):

\[
\begin{aligned}
Y &\sim \mathrm{Binomial}(n, \theta), \\
\theta &\sim \mathrm{Beta}(a,b), \\
\theta \mid y &\sim \mathrm{Beta}(a+y,\, b+n-y).
\end{aligned}
\]

This is the pedagogical figure in this repo: prior → data → posterior concentration.

![Beta–Binomial prior and posterior](figures/beta_binomial_prior_posterior.png)

---

## 7. Calibration target

If predicted risks are \(p_i\) and outcomes \(y_i\), good calibration means:

\[
\mathbb{E}[Y \mid p] \approx p.
\]

We monitor calibration slope / intercept and reliability diagrams (see figure below). Discrimination (AUC) is secondary for this endeavor’s claims.

![Synthetic logistic calibration](figures/logistic_calibration.png)

![Predictive uncertainty bands](figures/predictive_uncertainty.png)

---

## 8. Implementation path in this repo

| Step | Artifact |
| --- | --- |
| Classical baseline | `notebooks/01_baseline_logistic_calibration.ipynb` |
| Bayesian formulas + figures | this page + `scripts/make_figures.py` |
| Next | Bayesian GLM notebook (MAP / Laplace or MCMC) on synthetic data, then SEER-derived analytic files under DUA (private) |

---

## 9. Regenerating figures

```bash
source .venv/bin/activate
python scripts/make_figures.py
```
