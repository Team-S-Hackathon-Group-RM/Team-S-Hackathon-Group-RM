# GitHub + Colab workflow for Group S

The brief marks teamwork from your **GitHub commit history and Colab history**, and says most coding must be done **between 10:00 and 16:00 today**. So the rule is simple: **everyone edits the one shared notebook from their own Google account, and pushes it to GitHub from their own GitHub account, today.**

> Commits must come from each member's own GitHub account. Do not let one person push everything: "GitHub use carried out by only one person" is the *Poor* band of the Teamwork criterion.

---

## 1. One-time setup (integrator, ~10 min)
1. github.com → your avatar → **Your organizations → New organization** → Free plan. Name e.g. `uh-dsc-group-s-2026`.
2. **People → Invite member**: add all 9 members (they must accept the email invite).
3. Repository: https://github.com/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM (already created, must be **Public**).
4. Upload the starter files from this folder (drag-and-drop on github.com → *Add file → Upload files*), **excluding `docs/reference/`** (course PDFs and phone photos; `.gitignore` already excludes them if you use git):
   `FINAL GroupS TownCost.ipynb`, `README.md`, `requirements.txt`, `.gitignore`, `data/`, `src/`, `submission/`, `results/`, `docs/CHECKLIST.md`, `docs/GITHUB_GUIDE.md`.
   Commit message: `setup: data, metric module, starter notebook`.
5. Fill in `GITHUB_DATA` in the notebook's data-loading cell with
   `https://raw.githubusercontent.com/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM/main/data/`
   (this is the "Colab linked to data stored in GitHub" requirement).

## 2. Shared Colab notebook
1. Open `https://colab.research.google.com/github/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM/blob/main/FINAL%20GroupS%20TownCost.ipynb`.
2. *File → Save a copy in Drive* → **Share → Anyone with the link → Editor**. Put this link on slide 1 and in the Canvas submission.
3. To push Colab edits back to GitHub: *File → Save a copy in GitHub* → pick the org repo, branch `main`, add a commit message.
   (First time: Colab asks to authorise GitHub, tick **Include private repos / organisation access** so the org repo appears.)

## 3. How the team works on ONE shared notebook (teamwork evidence)
There is a single notebook, `FINAL GroupS TownCost.ipynb`, opened as the shared Colab (Drive copy, Editor rights). Pairs divide it by section:

| Pair | Sections they own and extend |
|---|---|
| Integrator | 1 Setup, 10 final ranking + submission files, GitHub pushes at milestones |
| EDA | 2: extra plots (distributions, missing-pattern heatmap, target by every feature) |
| Metric | 3: AI answers for hospitalisation probabilities (table in 3.3), cost table, hand check |
| Pre-processing | 4 + 5.1: try more options (binning, other imputation/encoding) and compare with the town cost |
| Models | 5–6: add models (e.g. XGBoost, MLP), scored with `evaluate()` |
| Tuning / results | 7–9: tuning, box plot of fold costs, paired comparison, sensitivity |
| XAI + slides | 11–12 (XAI and figure styling may continue after 16:00) |

**Rules so nobody loses work**
1. Everyone works **in the shared Colab** (not in their own downloaded copy), each in **their own section**. Colab saves everyone's edits into the same Drive notebook, and *File → Revision history* records who changed what (this is the "Colab history" the brief checks).
2. Add cells **inside your own section only**. Start each of your markdown cells with your name, e.g. `### 2.6 Income vs vaccination (YourName)`, so contributions are visible in the notebook itself.
3. Do **not** press *Run all* while others are working (it is slow and resets everyone's outputs). Run your own cells; the integrator does *Restart and run all* at 15:15.
4. Pushing to GitHub: after finishing a piece of work, the person who did it pushes **from their own GitHub account**: *File → Save a copy in GitHub* → repo `Team-S-Hackathon-Group-RM`, path `FINAL GroupS TownCost.ipynb`, branch `main`, message saying what they did, e.g. `EDA: income and insurance plots (YourName)`.
   (First time, Colab asks to authorise GitHub: allow access to the organisation so the org repo appears in the list.)
   Because everyone edits the same Drive notebook, the copy saved to GitHub always contains the whole team's latest work, so pushes do not overwrite each other.
5. **Commit little and often** (every 30–45 min) and from **different people**: 8 names in the history with clear messages is what the Teamwork criterion rewards; "GitHub use carried out by only one person" is the *Poor* band.

## 4. Timeline for GitHub today
| Time | GitHub action |
|---|---|
| now | org + repo + invites + starter files; Colab shared with Editor rights |
| every 30–45 min | whoever just finished a piece of work pushes the shared notebook from their own account |
| 15:15 | integrator: *Runtime → Restart and run all* on the final notebook, push it **with outputs** + `submission/` + `results/ranking.csv` |
| 15:40 | Canvas "Data Science Challenge Hackathon submissions": 5 files from `submission/` + GitHub org link + Colab link |
| after 16:00 | **only** XAI and figure styling commits (the brief forbids new modelling after the hackathon; the commit timestamps will show it) |
| before 10:00, 17 Nov | final notebooks pushed ("upload a copy of your Colab notebook(s) just before submission"), slides on Canvas with both URLs on slide 1 |

## 5. Before every push: checklist
- [ ] Notebook runs top to bottom without errors, **outputs saved** (markers read it on GitHub).
- [ ] Every plot that will appear in the slides has its plotting code in a notebook (1 point lost per plot without code).
- [ ] Markdown title + explanation above each step.
- [ ] No passwords / tokens in any cell.
- [ ] Repo is **Public**; Colab link set to **Editor**.
