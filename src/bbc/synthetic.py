"""Synthetic cohort generator for pipeline demos (not clinical data)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def make_synthetic_cohort(
    n: int = 800,
    seed: int = 20260812,
) -> pd.DataFrame:
    """Generate a simple synthetic binary-outcome cohort.

    Columns mimic a minimal risk-style table for software testing only.
    """
    rng = np.random.default_rng(seed)
    age = rng.normal(55, 10, size=n).clip(30, 85)
    screening_gap_years = rng.exponential(1.5, size=n).clip(0, 8)
    density_score = rng.normal(0, 1, size=n)
    linear = (
        -3.2
        + 0.035 * (age - 50)
        + 0.25 * screening_gap_years
        + 0.45 * density_score
    )
    prob = 1.0 / (1.0 + np.exp(-linear))
    event = rng.binomial(1, prob)

    return pd.DataFrame(
        {
            "age": np.round(age, 1),
            "screening_gap_years": np.round(screening_gap_years, 2),
            "density_score": np.round(density_score, 3),
            "event": event.astype(int),
            "true_risk": np.round(prob, 4),
        }
    )


def write_default_csv(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    make_synthetic_cohort().to_csv(path, index=False)
    return path


if __name__ == "__main__":
    out = write_default_csv(
        Path(__file__).resolve().parents[2] / "data" / "synthetic" / "synthetic_cohort.csv"
    )
    print(f"Wrote {out}")
