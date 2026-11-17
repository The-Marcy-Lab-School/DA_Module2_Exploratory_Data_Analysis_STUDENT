# Exploratory Data Analysis Project

**Replace this README before submitting your final project with:**

- **Title and one-line summary:** what you analyzed and for whom.
- **Scenario:** your stakeholder and their business problem.
- **Data overview:** what the data is, where it's from, how big it is,
  and what you had to clean.
- **Statistical summary:** your key numbers, and why you trust the mean
  or the median for each.
- **Visualizations:** at least one real chart image embedded from
  `images/`, with a one-line caption.
- **Takeaways:** your answer to the stakeholder, plus one caveat.
- **How to run it:** the exact setup and run steps.

Five of these are the README sections from Day 12. The title line and
"How to run it" are added so the README works for an employer who has
never seen this assignment.

---

## Setup

### 1. Start in a new folder

Work in a folder that is **not** inside an existing git repo. Check with:

```bash
git status
```

You want `fatal: not a git repository`. If you see a branch name, `cd`
somewhere else first.

### 2. Use the template, not Fork

On this repo's GitHub page, click **Use this template**, then **Create a new
repository**. Don't Fork. Name it something like `flood-claims-eda`
and keep it **public**. Then clone **your** new repo and `cd` into it.

### 3. Check `.gitignore`

Confirm it has these lines, or create it with them:

```
.DS_Store
.vscode/
__pycache__/
.ipynb_checkpoints/
.venv/
venv/
```

- `.DS_Store` and `.vscode/`: Mac and VS Code files, not part of your
  project.
- `__pycache__/`: files Python generates when it runs.
- `.ipynb_checkpoints/`: Jupyter's autosave copies of your notebook.
- `.venv/` and `venv/`: your virtual environment (step 5). It's large and
  anyone can rebuild it from `requirements.txt`.

Don't ignore `images/`. Your README needs the charts in it.

### 4. Put your name on the LICENSE

`LICENSE` is the MIT License, which lets others reuse your work with
credit. Replace `[YOUR NAME]` with your name and commit:

```bash
git add LICENSE
git commit -m "add my name to LICENSE"
```

### 5. Install the packages

From your repo's top folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open `starter/analysis.ipynb` in VS Code. Click **Select Kernel** in the
top right and choose the `.venv` Python. Run the first code cell to
confirm pandas loads.

## The project

- Pick your domain in `SCENARIOS.md` and delete the other 3 data files in
  `data/`.
- Follow `CHECKLIST_TIMELINE.md` day by day. `RUBRIC.md` shows how it's
  graded. The MVP checklist is also in the LMS.
- Do your analysis in `starter/analysis.ipynb`. The notebook reads data
  from `../data/` and saves charts to `../images/`.
- Before every commit, run **Restart and Run All** to make sure the
  notebook works from top to bottom.

## Before you submit

Your final repo is for employers, not for school. Before your final push:

- Delete `CHECKLIST_TIMELINE.md`, `RUBRIC.md`, `SCENARIOS.md`, and
  `PROJECT_OVERVIEW.md`. They're school-facing and stay in the LMS.
- Rename the `starter` folder to `analysis`:

  ```bash
  git mv starter analysis
  ```

  The notebook's `../data/` and `../images/` paths still work after the
  rename.
- Replace this README with your own, using the sections at the top.
