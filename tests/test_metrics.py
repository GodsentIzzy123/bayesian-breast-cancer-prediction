"""Smoke tests for core helpers."""

from pathlib import Path

import numpy as np
import pandas as pd

from bbc.metrics import brier_score, calibration_slope_intercept
from bbc.synthetic import make_synthetic_cohort


def test_brier_perfect():
    y = np.array([0.0, 1.0, 1.0, 0.0])
    p = np.array([0.0, 1.0, 1.0, 0.0])
    assert brier_score(y, p) == 0.0


def test_calibration_runs():
    rng = np.random.default_rng(0)
    y = rng.binomial(1, 0.3, size=200)
    p = np.clip(y * 0.7 + 0.15 + rng.normal(0, 0.05, size=200), 0.01, 0.99)
    slope, intercept = calibration_slope_intercept(y, p)
    assert np.isfinite(slope) and np.isfinite(intercept)


def test_synthetic_cohort_shape():
    df = make_synthetic_cohort(n=100, seed=1)
    assert len(df) == 100
    assert set(df.columns) >= {"age", "event", "true_risk"}
    assert df["event"].isin([0, 1]).all()


def test_synthetic_csv_present():
    root = Path(__file__).resolve().parents[1]
    csv_path = root / "data" / "synthetic" / "synthetic_cohort.csv"
    assert csv_path.exists(), "Run: python -m bbc.synthetic"
    df = pd.read_csv(csv_path)
    assert len(df) >= 100
