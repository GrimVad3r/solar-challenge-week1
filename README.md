
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
git clone git@github.com:worashf/solar-challenge-week1.git
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

### 4. Running Tests
```bash
# Run unit tests locally
pytest tests/

# Or via GitHub Actions (see .github/workflows/unittests.yml)
```

## 🔧 Key Files
| File | Purpose |
|------|---------|
| `environment.yml` | Conda environment specification |
| `.github/workflows/unittests.yml` | Automated test runner |
| `notebooks/README.md` | Jupyter notebook guidelines |
| `src/` | Main Python package source |

## 📝 License
This project is [MIT licensed](LICENSE).

---
