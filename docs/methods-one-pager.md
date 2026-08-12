# Methods one-pager — Bayesian breast-cancer prediction research

**Osayimwense Godsent Izinyon** · Research repository display page · Synthetic / educational figures only  
**Repo:** https://github.com/GodsentIzzy123/bayesian-breast-cancer-prediction

*Use browser Print → Save as PDF on this page or the repository README.*

---

## Core formulas

**Logistic likelihood**

$$
Y_i \mid x_i,\beta \sim \mathrm{Bernoulli}(\pi_i),
\quad
\pi_i=\sigma(x_i^\top\beta)=\frac{1}{1+e^{-x_i^\top\beta}}.
$$

**Prior / posterior**

$$
\beta_j\sim\mathcal{N}(0,\tau^2),
\quad
p(\beta\mid y,X)\propto p(y\mid X,\beta)\,p(\beta).
$$

**Posterior predictive risk**

$$
p(y_{\mathrm{new}}=1\mid x_{\mathrm{new}},y,X)
=\int \sigma(x_{\mathrm{new}}^\top\beta)\,p(\beta\mid y,X)\,d\beta.
$$

**Partial pooling (site / subgroup intercepts)**

$$
\beta_{0s}\sim\mathcal{N}(\mu_0,\sigma_0^2).
$$

**Beta–Binomial conjugate update**

$$
\theta\sim\mathrm{Beta}(a,b),\quad
\theta\mid y\sim\mathrm{Beta}(a+y,\,b+n-y).
$$

---

## Figure 1 — Prior → posterior updating

![Beta–Binomial](figures/beta_binomial_prior_posterior.png)

---

## Figure 2 — Calibration (synthetic logistic baseline)

![Calibration](figures/logistic_calibration.png)

---

## Figure 3 — Predictive uncertainty

![Uncertainty](figures/predictive_uncertainty.png)

---

**Note:** These displays document methodological progress and software/analysis scaffolding. They are not SEER microdata results and are not for clinical use.
