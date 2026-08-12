"""Helpers for Bayesian breast-cancer prediction research demos."""

from .metrics import brier_score, calibration_slope_intercept
from .synthetic import make_synthetic_cohort

__all__ = [
    "brier_score",
    "calibration_slope_intercept",
    "make_synthetic_cohort",
]
