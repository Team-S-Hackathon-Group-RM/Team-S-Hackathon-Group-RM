# Requirement checklist: Assignment 1, Data Science Challenge (30%), Nov 2026

Every requirement in the Canvas PDF, the dataset sheet, the target-metric sheet and the rules sheet, and where it is met.
✅ done · 🟡 started, team must finish · ⬜ team to do

## A. During the hackathon (10:00–16:00, Wed 11 Nov)
| # | Requirement (source) | Where / how | Status |
|---|---|---|---|
| A1 | GitHub organisation, all members added (PDF: before hackathon) | `docs/GITHUB_GUIDE.md` §1 | ⬜ |
| A2 | Repository inside the org, **fully public** (PDF: code presentation) | GITHUB_GUIDE §1 | ⬜ |
| A3 | Shared Colab, **Editor rights**, linked to data stored in GitHub (PDF: Colab & GitHub) | notebook data cell reads `raw.githubusercontent.com/.../data/` in Colab; GITHUB_GUIDE §2 | 🟡 fill in `GITHUB_DATA` |
| A4 | Deep EDA, many plots that drive pre-processing/modelling decisions (PDF: data exploration) | notebook §2: target balance, missingness, rate by 8 features, correlations, age × chronic heatmap | ✅ (EDA pair extends) |
| A5 | Pre-processing appropriate to models; **compare options** (PDF: pre-processing) | §4 two variants (one-hot+indicators vs ordinal+native NaN), §5.1 comparison, engineered features | ✅ |
| A6 | Models chosen for appropriateness; compare models (PDF: modelling) | §5: LogReg, RF, HistGB, LightGBM; §6 calibrated HGB; §8 ensemble | ✅ |
| A7 | **Discover the task metric** (not accuracy/F1) and compute it without a given formula (PDF + metric sheet) | §3: town-cost table, derivation of personal threshold, hand check; `src/town_cost.py` | ✅ |
| A8 | Use generative AI to estimate hospitalisation probabilities; **ask several AIs / several people** (metric sheet) | §3.3 table with rows AI 1–3 | ⬜ **fill in, then Run all** |
| A9 | Hospitalisation depends on dataset factors + vaccination status (metric sheet) | `hosp_probs()`: age group × chronic-condition count, × (1 − VE) if vaccinated | ✅ (extend if AIs name other factors) |
| A10 | Validate on unseen data (PDF: performance) | every score is out-of-fold | ✅ |
| A11 | Hyper-parameter tuning (PDF) | §7 randomised search, before/after | ✅ |
| A12 | **CV to measure size of random variation** (PDF) | 5-fold × 3 repeats, mean ± std, box plot §9.1, paired differences §9.1b | ✅ |
| A13 | Critically evaluate and choose what to submit (PDF) | §9.1b paired comparison, §9.2 threshold rule, §9.3 sensitivity of ranking, §12 | ✅ |
| A14 | **5 different** prediction files, ordered best→worst **by the task metric** (PDF + rubric) | `submission/`, order = mean town cost; `results/ranking.csv` | ✅ (re-run after A8) |
| A15 | File format = `dataset_C_example_submission.csv`: `respondent_id`, `covid_vaccine` (rules sheet) | asserted in §10 (columns, rows, ID order, 0/1 values) | ✅ |
| A16 | Names `challenge_submission_group_S_order_Y` (rules sheet) | §10 | ✅ |
| A17 | Submit to Canvas assignment **"Data Science Challenge Hackathon submissions"** by **16:00**, with **links to code** (rules sheet + PDF) | aim for 15:40 | ⬜ |
| A18 | Readable, commented code; markdown titles + explanations (PDF) | every section has a markdown cell; code commented | ✅ |
| A19 | Most coding done in session, visible in GitHub + Colab history (PDF) | everyone edits the one shared Colab from their own Google account; pushes to GitHub from their own GitHub account after their section (GITHUB_GUIDE §3) | ⬜ |
| A20 | Everyone has a clear task with coding + analysis, work in pairs (advice sheet) | README division-of-work table (sections per pair) | ⬜ assign names |

## B. After the hackathon (only XAI + figure styling + presentation)
| # | Requirement | Where / how | Status |
|---|---|---|---|
| B1 | XAI: most important features + how features affect predictions (PDF) | §11 SHAP summary (LightGBM) | 🟡 |
| B2 | **Multiple XAI techniques, critically evaluated for all models** (rubric: critical analysis tools) | add permutation importance for all 5 models + SHAP for trees + LogReg coefficients; compare | ⬜ |
| B3 | Figure polishing, code in GitHub/Colab (PDF) | style code in notebook | ⬜ |
| B4 | No new modelling after 16:00 (PDF) | only XAI/figure commits after today | ⬜ |
| B5 | Final notebook(s) uploaded to GitHub just before slide submission (PDF) | GITHUB_GUIDE §4 | ⬜ |

## C. Presentation, Tue 17 Nov (slides due **10:00**, talks from **13:00**)
| # | Requirement | Status |
|---|---|---|
| C1 | **Slide 1: GitHub org URL + shared Colab URL** | ⬜ |
| C2 | 10 minutes hard stop + 5 min questions | ⬜ rehearse twice with a timer |
| C3 | Model architecture and training scheme | ⬜ |
| C4 | EDA, performance analysis (task metric), XAI | ⬜ |
| C5 | Successes & failures | ⬜ |
| C6 | Teamwork: how work was delegated, group decisions, issues discussed | ⬜ |
| C7 | **Non-expert summary slide** (stakeholders, no data-science jargon) | ⬜ |
| C8 | Every student presents a section; everyone can answer questions on the **whole** project (20 pts Q&A) | ⬜ |
| C9 | Every plot/model shown exists in the code (−1 pt per plot without code; missing model = not done) | ⬜ |
| C10 | One slide submission per team on Canvas | ⬜ |
| C11 | Attend the presentation (absence = 0%) | ⬜ |

## D. Individual
| # | Requirement | Status |
|---|---|---|
| D1 | Feedback Fruits: grade teammates in 3 categories + self-assessment + short comment on teamwork | ⬜ each member |

## Rubric (100 pts)
Teamwork 10 · Peer review 10 · Implementation choices 15 · Critical analysis tools 10 · Presentation 25 · Understanding & critical thinking 20 · Challenge submission 10.
