
# Ten Academy Week 0: Python Data Science Environment Setup

![](https://img.shields.io/badge/Python-3.9+-blue)
![](https://img.shields.io/badge/Conda-4.12+-green)
![](https://img.shields.io/badge/License-MIT-yellow)

Project template for setting up a Python data science environment with Conda, unit testing, and Jupyter notebooks.

## 🛠️ Project Structure

```
     
├── .github/
│   └── workflows
        |── ci.yml
│       ├── unittests.yml        # GitHub Actions CI
├── .gitignore
├── requirements.txt             # Pip dependencies (alternative)
├── environment.yml              # Conda dependencies (primary)
├── README.md
├── src/                         # Main source code
├── notebooks/                   # Jupyter notebooks
│   ├── __init__.py
│   └── README.md
├── tests/                       # Unit tests
│   ├── __init__.py
└── scripts/                     # Utility scripts
    ├── __init__.py
    └── README.md
```

## 🚀 Setup Instructions

### 1. Clone & Prepare
```bash
git clone git@github.com:GrimVad3r/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Conda Environment Setup
```bash
# Create from environment.yml
conda env create -f environment.yml

# Activate
conda activate solar-challenge-week1

# Install pip requirements (if needed)
pip install -r requirements.txt
```

### 3. Development Tools
```bash
# Install development dependencies
conda install jupyter pytest pylint

# Launch Jupyter
jupyter notebook --notebook-dir=./notebooks
```

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

Sierra Leone-Bumbuna: Data Quality and Meteorological Correlation Analysis
This report summarizes the preparatory steps taken in the sierraleone-eda.ipynb notebook, focusing on the quality assessment and initial exploratory analysis of meteorological and solar irradiance data from Sierra Leone-Bumbuna.
Task Planning and Strategy
The notebook adheres to a highly prioritized and linear strategy optimized for data cleaning efficiency, as is common with large, time-series data:
1.	Initial Profile (Objective): Quickly establish dataset size (525,600 records) and feature statistics using df.describe() to identify basic data range violations.
2.	Data Cleaning (Methodology): Adopt the Z-score method (threshold > 3) as the sole cleaning step. This method is prioritized for handling extreme outliers in numerical features, which are common in sensor data.
3.	Exploratory Data Analysis (EDA Outline): Focus the EDA almost exclusively on bivariate and multivariate scatter plots to visualize sensor relationship integrity, specifically between Relative Humidity (RH), Ambient Temperature (Tamb), and Global Horizontal Irradiance (GHI).
Feasibility and Proactive Planning
The approach is highly feasible due to its focus on a singular, powerful cleaning technique:
•	Identified Challenge: Sensor data is prone to anomalous readings (spikes/drops).
•	Proposed Solution: The Z-score outlier removal method (which flagged approximately 6.86% of records for Sierra Leone) is a realistic and efficient solution for statistical data cleaning. The cleaned subset (df_clean) ensures subsequent visualizations are not skewed by these extreme values.
•	Dependencies/Barriers: The primary dependency is the assumption that the removed 36,079 records were genuine errors and not meaningful extreme weather events. This is a common and necessary trade-off for producing a clean baseline model input.
Clarity and Organization of Report
The notebook is clearly organized into three primary segments—loading, cleaning, and visualization—with a strong focus on visualizing sensor relationships. The use of bubble charts (scatter plots sized by a third variable like RH or BP) effectively allows for a multivariate view, communicating complex data dependencies clearly.

```


### 📝 License
This project is [MIT licensed](LICENSE).

