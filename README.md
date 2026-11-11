# Team S: Data Science Hackathon (Research Methods in Data Science, 11 November 2026)
## COVID Vaccine Allocation: Minimising Town Cost (Dataset C)

**Data Science Challenge Hackathon, 11 November 2026, Group S**

| | |
|---|---|
| GitHub organisation | https://github.com/Team-S-Hackathon-Group-RM |
| Shared Colab notebook (Editor) | to be created by a team member from their own Google account (File → Save a copy in Drive → Share: Editor) |
| Open the main notebook in Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM/blob/main/FINAL%20GroupS%20TownCost.ipynb) |

## The problem
A town posts COVID vaccines to residents' homes. For each resident in the test set we decide **send a vaccine (1) or not (0)**.
The score is the **total money the town spends** (lower is better):

* Vaccine **$1,500** per dose sent. Unused doses are wasted but still paid for.
* Anyone who wants a vaccine but is not sent one is paid **$1,500 in cash** and stays unvaccinated.
* Everyone is infected; each hospitalisation costs **$41,000**. Hospitalisation risk depends on age, number of chronic conditions and vaccination status (estimated with generative AI, see notebook section 3.3).

The optimal rule sends a vaccine when `P(accept) > V / (V + (p_unvaccinated − p_vaccinated) × H)`, a **personal threshold** for every resident.

## Notebooks
* `FINAL GroupS TownCost.ipynb`: the complete pipeline that produces the 5 submission files.
* `Team_S_Hackathon.ipynb`: the team's shared Colab notebook started before the hackathon.

## Repository structure
```
FINAL GroupS TownCost.ipynb   main notebook: EDA → metric → pre-processing → models → tuning → ranking → XAI
data/                            training, testing and example-submission CSVs + dataset information sheet
src/town_cost.py                 the town-cost metric as a stand-alone, tested module
submission/                      the 5 ranked files sent to Canvas (challenge_submission_group_S_order_1..5.csv)
results/ranking.csv              which model is in which file, with cross-validated cost ± std
docs/                            requirement checklist, GitHub workflow, HOW_TO_PUSH.md (step-by-step for every member)
```

## How to run
**Colab:** click the *Open in Colab* badge above, then *Runtime → Run all* (about 15–25 min on the free CPU). The notebook reads the CSVs straight from this repo's `data/` folder; the last cell of section 10 downloads the 5 submission files as a zip.
**Local:**
```bash
pip install -r requirements.txt
jupyter notebook "FINAL GroupS TownCost.ipynb"    # Run all (~5 min on a laptop)
python src/town_cost.py                              # metric hand check
```

## Results (5-fold CV repeated 3×, town cost per resident)
| Order | Model | Cost / resident |
|---|---|---|
| 1 | LightGBM (tuned) | $3,224 ± 105 |
| 2 | LightGBM | $3,230 ± 101 |
| 3 | Mean ensemble (LogReg + LightGBM tuned + calibrated HGB) | $3,231 ± 107 |
| 4 | Logistic Regression | $3,235 ± 106 |
| 5 | Random Forest | $3,235 ± 107 |

Baselines per resident: send nobody $4,010, send everybody $3,901, perfect knowledge $2,891. Personal thresholds save ≈ $564k vs a 0.5 cut-off on a town the size of the test set. Order 1 is also the most robust model across the 9 hospitalisation scenarios (mean rank 1.78).
Hospitalisation inputs: average of 3 AIs (`docs/ai_hospitalisation_estimates.md`). The top models differ by less than the fold-to-fold noise (see notebook §9.1b).

## Team members (Group S)
| # | Name | Notebook sections / role |
|---|---|---|
| 1 | Maruri Siva Harshitha | 2 EDA |
| 2 | Shruthi Chintalapudi | 2 EDA |
| 3 | Iqra Fazal | 3 Metric + AI hospitalisation research |
| 4 | Aqsa Iqbal | 4 Pre-processing, 5.1 |
| 5 | Kodi Chinthala Vaishnavi | 5–6 Models + calibration |
| 6 | Shravani Mukkarigari | 7–8 Tuning + ensemble |
| 7 | Lakshmi Nagaraju Manthri | 9 Results, variability, sensitivity |
| 8 | Varun Kumar Kashetty | 11–12 XAI, critical analysis, slides |
| 9 | Sai Raghavendra Ummareddy | absent from the hackathon on 11 Nov; no sections assigned |

## Division of work
One shared notebook for the whole team; each pair owns sections of it.

| Member(s) | Notebook sections |
|---|---|
| | 1 Setup + GitHub/Colab, final integration and submission (§10) |
| | 2 EDA |
| | 3 Metric + generative-AI research on hospitalisation |
| | 4 Pre-processing (§4, §5.1) |
| | 5–6 Models + calibration |
| | 7–8 Tuning + ensemble, 9 results and variability |
| | 11 XAI + figure styling, 12 critical analysis, slides |

## Use of generative AI
Generative AI was used, as the brief instructs, to estimate hospitalisation probabilities and vaccine effectiveness (several AIs, answers recorded in notebook section 3.3). (Edit to list any other use.)
