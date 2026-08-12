"""Core evaluation metrics used by the protocol."""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LinearRegression


def brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """Mean squared error of probabilistic forecasts (binary)."""
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)
    if y_true.shape != y_prob.shape:
        raise ValueError("y_true and y_prob must have the same shape")
    return float(np.mean((y_prob - y_true) ** 2))


def calibration_slope_intercept(
    y_true: np.ndarray, y_prob: np.ndarray, eps: float = 1e-6
) -> tuple[float, float]:
    """Approximate calibration slope and intercept via logit-linear regression.

    Fits: y ~ intercept + slope * logit(p). Perfect calibration ≈ intercept 0, slope 1.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), eps, 1.0 - eps)
    logit = np.log(y_prob / (1.0 - y_prob)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(logit, y_true)
    return float(model.coef_[0]), float(model.intercept_)
