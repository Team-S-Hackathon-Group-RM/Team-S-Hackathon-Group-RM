# How every Group S member pushes to GitHub (step by step)

**Organisation:** https://github.com/orgs/Team-S-Hackathon-Group-RM/people
**Repository:** `Team-S-Hackathon-Group-RM` (if the repo has another name, replace it everywhere below)
**Notebook:** `FINAL GroupS TownCost.ipynb`

Why this matters: the Teamwork mark (10 pts) and the "most coding done during the hackathon" rule are checked from **GitHub commit history and Colab history**. Every member must push **from their own GitHub account** before 16:00 today. One person pushing everything = *Poor* band.

---

## Part A: ONE person does the setup (Integrator, ~10 min)

**A1. Invite everyone to the organisation**
1. Open https://github.com/orgs/Team-S-Hackathon-Group-RM/people
2. Click **Invite member** → type each member's GitHub username or email → role **Member** → **Send invitation**.
3. Repeat for all 8 other members. Each member must open the email (or https://github.com/orgs/Team-S-Hackathon-Group-RM/invitation) and click **Join**.

**A2. Repository (already exists)**
The repo is https://github.com/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM (created by Harshitha). It must be **Public**: Settings → General → Danger Zone → *Change visibility* if it is not.

**A3. Give everyone write access**
1. Repo → **Settings → Collaborators and teams → Add people** (or add a team containing everyone) → role **Write**.

**A4. First push of the project folder**

*Option 1: with git (Terminal):*
```bash
cd "<path to>/Group S - Dataset C"
git init -b main
git add .
git status                      # docs/reference/ must NOT be listed (course PDF + photos stay private)
git commit -m "Setup: data, town-cost metric, main notebook, team guidelines"
git remote add origin https://github.com/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM.git
git push -u origin main         # browser opens to log in the first time
```

*Option 2: no git (website):*
1. Open the repo page → **Add file → Upload files**.
2. Drag in: `FINAL GroupS TownCost.ipynb`, `README.md`, `requirements.txt`, `.gitignore`, and the folders `data/`, `src/`, `submission/`, `results/`, and `docs/` **without** `docs/reference/`.
3. Commit message `Setup: data, town-cost metric, main notebook, team guidelines` → **Commit changes**.

**A5. Create the ONE shared Colab**
1. Open https://colab.research.google.com/github/Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM/blob/main/FINAL%20GroupS%20TownCost.ipynb
2. **File → Save a copy in Drive**.
3. **Share** (top right) → General access: **Anyone with the link** → role **Editor** → **Copy link**.
4. Send the link to the group chat. Paste it into the notebook's first cell (*Shared Colab*) and into `README.md`.

---

## Part B: EVERY member (including the integrator), repeated during the day

**B1. One-time: connect Colab to your GitHub (2 min)**
1. Open the **shared Colab link** from the group chat (not your own copy).
2. **File → Save a copy in GitHub**. A pop-up asks to authorise. Click **Authorize googlecolab**.
3. On the authorisation page make sure **Team-S-Hackathon-Group-RM** shows **Grant** (click *Grant* next to it; if you see *Request*, ask the org owner to approve it at Settings → Third-party access).
4. Close the dialog for now (you push in B3).

**B2. Do your work**
1. Work only in **your own section** of the shared notebook (see the "Who does what" table in section 0).
2. Add new cells inside your section; put your name in every markdown heading you add, e.g. `### 2.6 Income vs vaccination (Iqra Fazal)`.
3. Run **your own cells** only (first run sections 1, 3 and 4 once so `train`, `X`, `y`, `evaluate` exist). Do not press *Run all* while others are working.

**B3. Push your work (every 30–45 min, or after each finished piece)**
1. In the shared Colab: **File → Save a copy in GitHub**.
2. Fill in:
   * Repository: `Team-S-Hackathon-Group-RM/Team-S-Hackathon-Group-RM`
   * Branch: `main`
   * File path: `FINAL GroupS TownCost.ipynb` (exactly this name, so it updates the same file)
   * Commit message: what **you** did, with your name (examples below)
   * Leave **Include a link to Colaboratory** ticked
3. Click **OK**. Check on GitHub: repo → **Commits**. Your name/username should be at the top.

Everyone edits the same Drive notebook, so the copy you push already contains everyone's latest work. Pushes do not overwrite each other's work.

**Example commit messages (one per person, change to what you actually did)**
| Member | Example message |
|---|---|
| Maruri Siva Harshitha | `EDA: vaccination rate by income and insurance (Maruri)` |
| Shruthi Chintalapudi | `EDA: missing-value pattern heatmap (Shruthi)` |
| Iqra Fazal | `Metric: AI hospitalisation estimates added to 3.3 (Iqra)` |
| Aqsa Iqbal | `Pre-processing: binning vs ordinal comparison (Aqsa)` |
| Kodi Chinthala Vaishnavi | `Models: XGBoost added, scored with town cost (Vaishnavi)` |
| Shravani Mukkarigari | `Tuning: random search on RF + fold box plot (Shravani)` |
| Lakshmi Nagaraju Manthri | `Results: sensitivity of ranking to hospital risk (Lakshmi)` |
| Varun Kumar Kashetty | `XAI: permutation importance for all models (Varun)` |

**If something goes wrong**
| Problem | Fix |
|---|---|
| Org repo not in the Colab list | B1 step 3: grant Colab access to the org; refresh the dialog |
| "Permission denied" on push | Integrator: repo Settings → Collaborators → give that person **Write** |
| Two people edited the same cell | Colab **File → Revision history** → restore, then push again |
| Accidentally pushed to the wrong file name | Push again with the correct path; delete the wrong file on GitHub |

---

## Part C: final steps today (Integrator, with one checker)
| Time | Action |
|---|---|
| 15:00 | Tell everyone to stop editing; last pushes |
| 15:15 | Colab **Runtime → Restart session and run all** (≈5–10 min); check section 10 prints no errors |
| 15:30 | **Save a copy in GitHub** with message `Final hackathon run: 5 ranked submissions` |
| 15:30 | Download the 5 files from the Colab file panel (`submission/` folder) **or** use the ones in the repo's `submission/` |
| **15:40** | Canvas → **Data Science Challenge Hackathon submissions** → upload `challenge_submission_group_S_order_1..5.csv` + paste the GitHub org link and the Colab link → Submit. Second person checks it appears. |

## After 16:00 and before 10:00 on Tue 17 Nov
* Only **XAI and figure styling** pushes (same B3 method), no new models.
* Just before the slides deadline, push the final notebook once more (brief: "upload a copy of your Colab notebook(s) just before submission").
* Slide 1 must show: https://github.com/Team-S-Hackathon-Group-RM and the shared Colab link.
