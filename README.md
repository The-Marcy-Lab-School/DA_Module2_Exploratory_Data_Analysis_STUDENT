# Exploratory Data Analysis Project

**Replace this README before submitting your final project with:**

- **Title and one-line summary:** what you analyzed, for whom, and the
  headline finding.
- **Stakeholder and business problem:** who needs the answer, what they
  asked, and why it matters to them.
- **Data:** where it's from, how big it is, what one row is, and what you
  cleaned.
- **Analysis:** what you did and why: your cleaning decisions, the
  feature you added, and the statistics you chose for the data's shape.
- **Statistical summary:** a table of the summary statistics for your
  key variables (count, mean, median, standard deviation, min, max), and
  one or two sentences on what the shape of the data means for which
  number to trust.
- **Findings:** your key numbers, with at least one chart embedded from
  `images/` and a one-line caption.
- **Recommendations:** what the stakeholder should do, plus one caveat on
  how far to trust it.
- **How AI was used:** where you used AI, what it got right or wrong, and
  how you checked it.
- **How to run it:** the exact setup and run steps.

Write it for an employer who has never seen this assignment and will skim
it in under a minute.

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

- Pick your domain in `PROJECT_OVERVIEW.md` and delete the other 3 data files in
  `data/`.
- Open `CHECKLIST_RUBRIC.md`. The MVP checklist at the top is the
  minimum to pass (it's also in the LMS), then Above & Beyond, then a
  day-by-day plan, and the rubric at the bottom.
- Do your analysis in `starter/analysis.ipynb`. The notebook reads data
  from `../data/` and saves charts to `../images/`.
- Before every commit, run **Restart and Run All** to make sure the
  notebook works from top to bottom.

## Before you submit

Your final repo is for employers, not for school. Before your final push:

- Delete `CHECKLIST_RUBRIC.md` and `PROJECT_OVERVIEW.md`. They're
  school-facing and stay in the LMS.
- Make the notebook employer-facing. Delete every
  **Instructions (delete before you submit)** block, every `TODO`, and the
  "Questions my analysis can answer" section. Replace them with your own
  explanations, so the notebook reads like a finished analysis.
- Rename the `starter` folder to `project`:

  ```bash
  git mv starter project
  ```

  The notebook's `../data/` and `../images/` paths still work after the
  rename.
- Replace this README with your own, using the sections at the top.
- Keep committing with descriptive messages that say what changed, such
  as `Clean payment columns and add total_paid`, not `update` or `final`.
