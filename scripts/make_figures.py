#!/usr/bin/env python3
"""Generate illustrative Bayesian / calibration figures for the docs site."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "docs" / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def fig_beta_binomial() -> None:
    """Conjugate Beta-Binomial: prior vs posterior after observing events."""
    a0, b0 = 2.0, 8.0  # skeptical low-risk prior
    n, y = 40, 11
    a1, b1 = a0 + y, b0 + (n - y)

    theta = np.linspace(0, 1, 400)
    prior = stats.beta.pdf(theta, a0, b0)
    post = stats.beta.pdf(theta, a1, b1)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(theta, prior, lw=2, label=rf"Prior Beta({a0:.0f},{b0:.0f})")
    ax.plot(theta, post, lw=2.5, label=rf"Posterior Beta({a1:.0f},{b1:.0f})")
    ax.axvline(y / n, color="gray", ls="--", lw=1.2, label=rf"MLE = {y/n:.2f}")
    ax.set_xlabel(r"Risk parameter $\theta$")
    ax.set_ylabel("Density")
    ax.set_title("Bayesian updating (Beta–Binomial toy example)")
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "beta_binomial_prior_posterior.png", dpi=160)
    plt.close(fig)


def fig_logistic_calibration() -> None:
    """Reliability-style plot from synthetic cohort + logistic baseline."""
    csv = ROOT / "data" / "synthetic" / "synthetic_cohort.csv"
    df = pd.read_csv(csv)
    features = ["age", "screening_gap_years", "density_score"]
    X = df[features]
    y = df["event"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=20260812, stratify=y
    )
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)
    p = model.predict_proba(X_test)[:, 1]
    yv = y_test.to_numpy()

    bins = np.linspace(0, 1, 8)
    centers, rates, ns = [], [], []
    dig = np.digitize(p, bins) - 1
    for b in range(len(bins) - 1):
        m = dig == b
        if m.sum() < 5:
            continue
        centers.append(p[m].mean())
        rates.append(yv[m].mean())
        ns.append(m.sum())

    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Perfect calibration")
    ax.scatter(centers, rates, s=[12 + 2.5 * n for n in ns], zorder=3)
    ax.plot(centers, rates, "-", lw=1.5, label="Logistic baseline (synthetic)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Predicted risk")
    ax.set_ylabel("Observed event rate")
    ax.set_title("Calibration diagram (synthetic demo)")
    ax.legend(frameon=False, loc="upper left")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "logistic_calibration.png", dpi=160)
    plt.close(fig)


def fig_predictive_uncertainty() -> None:
    """Show mean predictive curve with percentile band over bootstrap fits."""
    rng = np.random.default_rng(7)
    csv = ROOT / "data" / "synthetic" / "synthetic_cohort.csv"
    df = pd.read_csv(csv)

    # Focus on age effect while holding other covariates at medians
    gap = df["screening_gap_years"].median()
    dens = df["density_score"].median()
    ages = np.linspace(35, 80, 50)

    X = df[["age", "screening_gap_years", "density_score"]].to_numpy()
    y = df["event"].to_numpy()

    curves = []
    for _ in range(80):
        idx = rng.integers(0, len(df), size=len(df))
        model = LogisticRegression(max_iter=2000)
        model.fit(X[idx], y[idx])
        grid = np.column_stack(
            [ages, np.full_like(ages, gap), np.full_like(ages, dens)]
        )
        curves.append(model.predict_proba(grid)[:, 1])
    curves = np.asarray(curves)
    lo, mid, hi = np.percentile(curves, [10, 50, 90], axis=0)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.fill_between(ages, lo, hi, color="C0", alpha=0.22, label="80% bootstrap band")
    ax.plot(ages, mid, color="C0", lw=2.2, label="Median predictive risk")
    ax.set_xlabel("Age (years)")
    ax.set_ylabel(r"Predicted $P(Y=1 \mid x)$")
    ax.set_title("Predictive uncertainty (bootstrap illustration on synthetic data)")
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "predictive_uncertainty.png", dpi=160)
    plt.close(fig)


def main() -> None:
    fig_beta_binomial()
    fig_logistic_calibration()
    fig_predictive_uncertainty()
    print(f"Wrote figures to {FIG}")


if __name__ == "__main__":
    main()
