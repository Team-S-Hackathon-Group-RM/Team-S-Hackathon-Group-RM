"""Town-cost metric for Dataset C (Nov 2026 hackathon).

Rules from the 'Target Metric Information' sheet:
  * Everyone gets infected (100% infection probability).
  * Vaccines are posted to homes; an unused vaccine is wasted (still paid for).
  * Anyone who WANTS a vaccine but is not sent one must be paid the vaccine cost.
  * Hospitalisation cost = P(hospitalised | person, vaccinated?) x cost per stay.

Per-person cost, with V = vaccine cost, H = hospitalisation cost,
p_u / p_v = hospitalisation probability unvaccinated / vaccinated:

  sent=1, wants=1 (TP): V + p_v*H       vaccinated
  sent=1, wants=0 (FP): V + p_u*H       vaccine wasted, refuses it
  sent=0, wants=1 (FN): V + p_u*H       town pays cash, person stays unvaccinated
  sent=0, wants=0 (TN):     p_u*H

Optimal decision for a person with acceptance probability q:
  send if  q > V / (V + (p_u - p_v) * H)   -> a PERSONAL threshold.

V ($1,500) and H ($41,000) are GIVEN on the dataset sheet. The hospitalisation
probabilities, vaccine effectiveness and chronic multiplier are ASSUMPTIONS:
confirm them with several AIs (as the sheet asks) and record each answer in
the notebook. Ranking of models should
be checked to be stable across the plausible range (see sensitivity()).
"""
import numpy as np
import pandas as pd

VACCINE_COST = 1_500.0        # V, $ per dose (GIVEN on dataset sheet page 2)
HOSP_COST = 41_000.0          # H, $ per covid hospitalisation (GIVEN on dataset sheet page 2)
VACC_EFFECTIVENESS = 0.833    # mean of 3 AIs (docs/ai_hospitalisation_estimates.md)

# P(hospitalised | infected, unvaccinated) by age group (assumption, check with AI)
P_HOSP_AGE = {
    "18 - 34 Years": 0.0093,
    "35 - 44 Years": 0.0183,
    "45 - 54 Years": 0.0333,
    "55 - 64 Years": 0.0617,
    "65+ Years": 0.1533,
}
CHRONIC_MULT = 1.633          # mean of 3 AIs, per chronic condition (compounding)
P_CAP = 0.9                  # cap on hospitalisation probability
CHRONIC_COL = "number_chronic_med_conditions"   # count column in the Nov dataset (June had binary chronic_med_condition)


def hosp_probs(X: pd.DataFrame, p_age=None, chronic_mult=CHRONIC_MULT, ve=VACC_EFFECTIVENESS):
    """Return (p_unvaccinated, p_vaccinated) arrays for each row of X."""
    p_age = p_age or P_HOSP_AGE
    p_u = X["age_group"].map(p_age).fillna(np.mean(list(p_age.values()))).to_numpy(float)
    col = CHRONIC_COL if CHRONIC_COL in X.columns else ("chronic_med_condition" if "chronic_med_condition" in X.columns else None)
    if col is not None:
        n_chronic = X[col].fillna(0).clip(lower=0).to_numpy(float)
        p_u = p_u * chronic_mult ** n_chronic
    p_u = np.clip(p_u, 0, P_CAP)
    return p_u, p_u * (1 - ve)


def town_cost(y_true, sent, p_u, p_v, V=VACCINE_COST, H=HOSP_COST):
    """Total money spent by the town. Lower is better."""
    y, s = np.asarray(y_true).astype(int), np.asarray(sent).astype(int)
    vaccine = V * ((s == 1) | (y == 1))                        # sent, or paid cash because they wanted one
    hosp = H * np.where((s == 1) & (y == 1), p_v, p_u)         # only TP ends up vaccinated
    return float(np.sum(vaccine + hosp))


def personal_threshold(p_u, p_v, V=VACCINE_COST, H=HOSP_COST):
    return V / (V + (p_u - p_v) * H)


def decide(q, p_u, p_v, V=VACCINE_COST, H=HOSP_COST):
    """Send a vaccine (1) when expected saving beats the expected waste."""
    return (np.asarray(q) > personal_threshold(p_u, p_v, V, H)).astype(int)


def sensitivity(y_true, q, X, age_scales=(0.5, 1.0, 2.0), ves=(0.6, 0.8, 0.9)):
    """V and H are fixed by the sheet, so the uncertain inputs are the hospitalisation
    probabilities (scaled up/down) and vaccine effectiveness. Returns town cost per scenario."""
    rows = []
    for k in age_scales:
        p_age = {a: min(p * k, 1.0) for a, p in P_HOSP_AGE.items()}
        for ve in ves:
            p_u, p_v = hosp_probs(X, p_age=p_age, ve=ve)
            rows.append({"hosp_scale": k, "VE": ve,
                         "cost": town_cost(y_true, decide(q, p_u, p_v), p_u, p_v)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Hand check: 4 people, all aged 18-34, no chronic condition
    X = pd.DataFrame({"age_group": ["18 - 34 Years"] * 4})
    p_u, p_v = hosp_probs(X)
    y = np.array([1, 1, 0, 0]); s = np.array([1, 0, 1, 0])     # TP, FN, FP, TN
    expected = (1500 + p_v[0]*41000) + (1500 + p_u[0]*41000) + (1500 + p_u[0]*41000) + (p_u[0]*41000)
    assert np.isclose(town_cost(y, s, p_u, p_v), expected), town_cost(y, s, p_u, p_v)
    print("hand check OK:", expected)
    print("threshold 18-34:", round(personal_threshold(p_u, p_v)[0], 3))
