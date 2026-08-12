# Data Sources and Access Plan — Draft v0.1

**Author:** Osayimwense Godsent Izinyon  
**Date:** 2026-08-12  
**Rule:** This git repository contains **no protected health information** and **no restricted registry extracts**.

---

## 1. Current development data (in repo)

| Dataset | Path | Description | License / terms |
| --- | --- | --- | --- |
| Synthetic cohort | `data/synthetic/synthetic_cohort.csv` | Simulated binary-outcome cohort for pipeline and calibration demos | Generated for this project; free to use with the repo |

Synthetic data are for **software and methodology demos only**. They are not clinical evidence.

## 2. Planned lawful analysis sources (not stored here)

Candidates under consideration (final choice will be locked before formal model comparison):

1. **SEER** research data (or SEER*Stat extracts) under NCI data-use terms — requires registration / DUA as applicable.  
2. Other **public** clinical or cancer epidemiology datasets with clear redistribution rules.  
3. Institutional data **only** under IRB / DUA; such data will never be committed to git.

For each selected source, this file will record:

- Official name and version/year  
- Access URL and application/registration status  
- Date of request / approval  
- Variables mapped to the protocol  
- Any redistribution restrictions

## 3. Access log (living)

| Date | Source | Action | Status | Evidence to file |
| --- | --- | --- | --- | --- |
| 2026-08-12 | Synthetic | Generated local demo cohort | Complete | CSV in repo |
| TBD | SEER / other public source | Registration or data request | Planned | Keep confirmation / approval records privately |

## 4. Handling rules

- Raw restricted files stay on encrypted local or institutional storage only.  
- Derived, de-identified analysis tables may be referenced by hash/path in notebooks, not uploaded if terms forbid it.  
- Public notebooks in this repo must run end-to-end on synthetic (or clearly public) data.

## 5. Next actions

1. Select primary public source aligned to a narrow prediction question in `docs/protocol.md`.  
2. Complete registration / request; save dated confirmation.  
3. Update this file with variable dictionary links and inclusion criteria.  
4. Add a non-synthetic analysis branch only after access is documented.
