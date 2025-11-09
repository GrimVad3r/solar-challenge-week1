
## 📊 Task 2: Data Profiling, Cleaning & EDA

### 🎯 Objective

Perform an end-to-end exploratory data analysis (EDA) and cleaning workflow for a specific country's solar dataset. Prepare the data for downstream tasks such as comparison and region-ranking.

---

### 🗂️ Branch Naming Convention

Create a separate branch for each country’s EDA:

```
eda-[benin | togo |sierraleone]   # Example: eda-benin
```

---

### 📓 Notebook Naming Convention

Each country's notebook should follow the format:

```
<country>_eda.ipynb   # Example: benin_eda.ipynb
```

---

### 🔧 EDA Steps

#### 1. Summary Statistics & Missing Values

* Use `df.describe()` for numeric summary.
* Check for missing values:
  `df.isna().sum()`
* Flag any column with **>5% null values**.

#### 2. Outlier Detection & Basic Cleaning

* Focus on columns: `GHI`, `DNI`, `DHI`, `ModA`, `ModB`, `WS`, `WSgust`
* Compute **Z-scores** and flag outliers (`|Z| > 3`)
* Handle missing values:

  * Drop rows or impute using **median**
* Save cleaned data:

  * `data/<country>_clean.csv`
  * ⚠️ Ensure the `data/` directory is listed in `.gitignore` (do not commit raw or cleaned CSVs)

#### 3. Time Series Analysis

* Line/bar plots: `GHI`, `DNI`, `DHI`, `Tamb` vs. `Timestamp`
* Analyze trends by:

  * Day
  * Month
  * Peak/off-peak periods

#### 4. Cleaning Impact

* Compare `ModA`, `ModB` readings **pre/post-cleaning** using:

  ```python
  df.groupby('Cleaning')[['ModA', 'ModB']].mean()
  ```

#### 5. Correlation & Relationship Analysis

* Correlation heatmap:

  * Columns: `GHI`, `DNI`, `DHI`, `TModA`, `TModB`
* Scatter plots:

  * `WS`, `WSgust`, `WD` vs. `GHI`
  * `RH` vs. `Tamb`, `RH` vs. `GHI`

#### 6. Wind & Distribution Analysis

* Create wind rose or radial plots for `WS` and `WD`
* Plot histograms:

  * `GHI`
  * Another relevant variable (e.g., `WS`)

#### 7. Temperature & Humidity Interaction

* Explore how **relative humidity (`RH`)** affects:

  * Temperature (`Tamb`)
  * Solar radiation (`GHI`, `DNI`, etc.)

#### 8. Bubble Chart

* `GHI` vs. `Tamb`, with bubble size representing:

  * `RH` (Relative Humidity)
  * or `BP` (Barometric Pressure)

### 4. Current Progress
```bash

##Task-1
Project Kickoff: Version Control and CI/CD Setup
This report summarizes the essential steps and strategy employed during the initial phase of the project, focusing on establishing a robust Git environment, virtual environment, and Continuous Integration (CI) pipeline. This foundation ensures collaborative efficiency, dependency management, and code quality from day one.
________________________________________
Task Planning and Strategy: Git & Environment Setup
The strategy for Task 1 was highly structured and sequenced, prioritizing version control integrity and environment reproducibility before any data or code was introduced.
Step	Objective	Methodology & Priority
1. Repository Initialization	Create a central, accessible hub for collaboration.	High Priority: Initialize the solar-challenge-week1 GitHub repository and clone it locally.
2. Environment Isolation	Ensure project dependencies are isolated and documented.	High Priority: Create a Python virtual environment (venv or conda) and document exact dependencies in requirements.txt.
3. Branching & Feature Isolation	Maintain a clean main branch for stable code.	Create a dedicated feature branch, setup-task, to isolate setup changes.
4. Exclusion Strategy	Prevent unnecessary or sensitive files from being tracked.	Create a comprehensive .gitignore file specifically excluding large data/ folders and sensitive system files (.csv, .ipynb_checkpoints/).
5. Continuous Integration (CI)	Automate a basic check for environment reproducibility.	Implement a basic GitHub Actions workflow (ci.yml) to run a dependency check (pip install -r requirements.txt).
6. Documentation & Merging	Formalize the setup and integrate stable changes.	Document environment steps in README.md and merge setup-task into main via Pull Request (PR).
The key performance indicator (KPI), Dev Environment Setup, is directly tied to the successful completion of all these steps, confirming local and cloud reproducibility.
________________________________________
Feasibility and Proactive Planning
The plan is designed to be highly feasible and proactive in mitigating common early-stage project barriers, particularly related to dependency hell and environment drift.
•	Identified Challenge 1: Environment Reproducibility.
o	Proposed Solution: Use of a virtual environment (venv/conda) paired with an explicitly defined requirements.txt. The README.md acts as the primary document for users to follow the exact setup process.
•	Identified Challenge 2: Accidental Commit of Large/Sensitive Files.
o	Proposed Solution: Proactively adding key exclusions to .gitignore (data/, .csv, .ipynb_checkpoints/) prevents unnecessary large file commits and protects the repository history.
•	Identified Challenge 3: Lack of Initial Quality Gate.
o	Proposed Solution: Setting up a minimal GitHub Actions workflow (ci.yml) that runs pip install -r requirements.txt confirms that the dependency files are correctly formatted and accessible to an automated environment, verifying the initial Basic CI function.
•	Dependencies: The only dependency is the correct installation of Git and Python on the local machine; all other steps are self-contained within the repository structure.
Clarity and Organization of Report
The setup process results in a project structure that is clean, future-proof, and logically organized.
•	Git Commit Structure: The mandatory three commits on the setup-task branch ("init: add .gitignore", "chore: venv setup", "ci: add GitHub Actions workflow") provide a clear, linear history of the environment build.
•	Folder Structure: The suggested folder structure (e.g., separating notebooks/, src/, tests/) establishes an industry-standard architecture that allows for seamless growth as the project moves into data processing and modeling phases.
•	Documentation: The README.md is the central documentation point, ensuring that any new team member can reproduce the development environment by following the documented instructions.
This setup ensures that all subsequent data analysis and modeling tasks will be performed on a stable, reproducible, and version-controlled base.

##Task-2

Togo-Dapaong: A Standardized Data Preparation Pipeline
This report outlines the profiling, cleaning, and EDA methodology used in the togo_eda.ipynb notebook for the meteorological data from Togo-Dapaong.
Task Planning and Strategy
The Togo notebook follows the standardized pipeline established across all three projects, emphasizing consistency and reproducibility.
1.	Key Objective: Transform the initial 525,600 records into a usable, outlier-free dataset for modeling.
2.	Profiling (Methodology): Initial profiling relies on standard Pandas methods (.describe(), .info()) to quickly verify column data types and range statistics, establishing an immediate data baseline.
3.	Data Cleaning (Prioritization): Similar to the other projects, cleaning is prioritized using the Z-score (threshold > 3). This single, high-impact cleaning step addresses the largest data quality barrier (extreme outliers) before moving forward.
4.	EDA Focus: The EDA focuses on two core relationships via scatter plots: RH vs. Tamb and RH vs. GHI. This suggests an objective centered on understanding how humidity mediates temperature and solar performance.
Feasibility and Proactive Planning
The plan's greatest strength is its replicability and predictability:
•	Identified Challenge: The data contains a relatively high proportion of outliers (6.87%, or 36,116 records), indicating significant sensor noise or extreme transient conditions.
•	Proposed Solution: The systematic Z-score removal is a realistic and efficient solution for handling this volume of anomalies without requiring complex, feature-specific imputation, ensuring the remaining data is statistically stable.
•	Dependencies/Barriers: The only dependency is the successful execution of the outlier removal cell before any visualization is attempted. This is handled by creating the explicit df_clean DataFrame.
Clarity and Organization of Report
The notebook demonstrates excellent organizational clarity by strictly following the data science lifecycle. The output clearly shows the impact of the cleaning step (the size reduction from 525,600 to 489,484 records). The focused scatter plots on RH relationships effectively communicate targeted exploratory findings regarding atmospheric conditions and solar potential.

```
