# AIDA Lab - Local Development Setup 🎉

Welcome to the **Applied AI in Data Analytics** program! This is your local development environment setup.

> **🚀 New to the course?** Start with **[Google Colab](https://colab.research.google.com/gist/git-steb/1b6fcf993ef730629e9e6ff3e8576c59)** for zero setup, then return here when you're ready for local development.
> 
> **📦 Universal Setup**: This single setup works for **all modules** (1-8) and **all platforms** (Windows/macOS/Linux). You only need to download and configure this once!

> **ℹ️ Note:** You **do not** need this local lab setup for the first half of the course—**all labs can be completed entirely in Google Colab**. Treat this local environment as **optional** and best suited for advanced users who want more control, offline work, or deeper tooling integration.

## 🚀 Quick Start

### Step 1: Download Setup Files

**Option A: Download as ZIP (Recommended)**
1. **Visit the gist** (link provided in Module 1)
2. **Click "Download ZIP"** button (top-right menu)
3. **Unzip the files** and rename folder to `aida-lab-env`
4. **Navigate to the folder**: `cd aida-lab-env`

**Option B: Manual Download**
1. **Download each file** from the gist (pyproject.toml, setup.py, README.md)
2. **Create a folder** (e.g., `aida-lab-env/`)
3. **Put all files** into that folder

### Step 2: Choose Your Setup Method

**🚀 Option 1: Universal Setup (Recommended - No uv Required)**
```bash
# Auto-detects best package manager for your system (uv → poetry → pip)
# Works on Windows, macOS, and Linux
python setup_universal.py
```

**⚡ Option 2: uv Setup (Fast & Modern - RECOMMENDED)**

**First, install uv if you don't have it:**

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Then run setup using proper UV project workflow:**
```bash
# Modern UV project workflow (recommended)
# This automatically creates .venv, manages dependencies, and sets up .gitignore
uv sync
uv run python -m ipykernel install --name python3 --user

# Start Jupyter with UV environment
uv run jupyter lab
```

**📚 Option 3: Poetry Setup (If you prefer poetry)**
```bash
poetry install
python -m ipykernel install --name python3 --user
```

**📦 Option 4: pip Setup (Universal Fallback)**
```bash
# Works everywhere, including Google Colab
python setup_colab.py
```

### Manual Setup (Alternative)
```bash
# With uv (recommended - modern project workflow)
uv sync
uv run jupyter lab

# With poetry  
poetry install
poetry run jupyter lab

# With pip (fallback only - not recommended for new projects)
pip install -r requirements.txt
jupyter lab
```

> **⚠️ Note**: This setup uses the modern UV project workflow with `pyproject.toml`. The old `requirements.txt` approach is not recommended for new projects as it doesn't take advantage of UV's native project management capabilities.

## 🚀 UV Project Workflow (Modern Approach)

**Why UV's Project Workflow is Better:**
- **Automatic virtual environment management** - no manual activation needed
- **Automatic dependency resolution** - handles conflicts intelligently  
- **Automatic .gitignore creation** - excludes virtual environments
- **Faster package installation** - optimized for speed
- **Better Cursor integration** - automatic interpreter detection
- **Native project structure** - uses `pyproject.toml` instead of `requirements.txt`
- **Simplified workflow** - `uv add` and `uv remove` instead of manual pip commands

### UV Project Workflow Commands

```bash
# Start Jupyter with UV (automatic environment)
uv run jupyter lab

# Add new packages (automatically updates pyproject.toml)
uv add pandas matplotlib

# Remove packages (automatically updates pyproject.toml)
uv remove package-name

# Sync dependencies
uv sync

# Upgrade all packages
uv sync --upgrade

# Check available kernels
jupyter kernelspec list
```

### 🎯 Proper UV Project Initialization

**For new projects, use the proper UV workflow:**

```bash
# Initialize a new UV project (creates pyproject.toml, .venv, .gitignore automatically)
uv init my-aida-project

# Add dependencies (automatically updates pyproject.toml)
uv add pandas matplotlib seaborn

# Start working
uv run jupyter lab
```

**This setup already uses the proper UV project structure:**
- ✅ **pyproject.toml** - Native UV project configuration
- ✅ **No requirements.txt** - Avoids mixed workflow confusion  
- ✅ **Automatic .venv management** - No manual activation needed
- ✅ **Automatic .gitignore** - Excludes virtual environments
- ✅ **Native dependency management** - `uv add`/`uv remove` commands

### Cursor Integration with UV

**Automatic Interpreter Detection:**
1. **Open Cursor** in your aida-setup folder
2. **Cursor automatically detects** the UV virtual environment
3. **Select the UV interpreter** when prompted
4. **Jupyter notebooks** will automatically use the correct kernel

**Manual Interpreter Selection:**
1. **Press Cmd+Shift+P** (macOS) or **Ctrl+Shift+P** (Windows/Linux)
2. **Type "Python: Select Interpreter"**
3. **Choose the UV interpreter** (usually shows as `./.venv/bin/python`)
4. **Restart Cursor** if needed

## 📚 What You Get

This setup includes all the tools you need for the course:

### Core Data Science Stack
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Basic plotting
- **seaborn** - Statistical visualization

### AI/ML Tools
- **scikit-learn** - Machine learning
- **openai** - AI assistance
- **autoviz** - Automatic visualization (optional - may have compatibility issues)
- **ydata-profiling** - Automated EDA reports (optional - install separately if needed)

### Jupyter Environment
- **JupyterLab** - Modern notebook interface
- **ipywidgets** - Interactive widgets
- **jupytext** - Python notebook format

## 🎯 Module-Specific Tools

- **Module 2**: EDA with AI (optional autoviz, optional ydata-profiling)
- **Module 3**: Data Prep (pandas, numpy)
- **Module 4**: Insights & Dashboards (visualization tools)
- **Module 5**: No-Code/Low-Code ML (scikit-learn)
- **Module 6**: MLOps (deployment tools)
- **Module 7**: Hyperparameter Tuning (optimization)
- **Module 8**: Advanced AI (deep learning)

## 🛠️ Available Commands

**With uv (recommended - modern project workflow):**
```bash
# UV Project Workflow (recommended)
uv sync                   # Set up environment
uv run jupyter lab        # Start Jupyter with UV environment
uv add package-name        # Add new packages
uv remove package-name    # Remove packages
uv sync --upgrade         # Upgrade all packages

# Using poe tasks (alternative)
uv run poe setup          # Set up environment
uv run poe check          # Check if everything works
uv run poe pull           # Update to latest version
uv run poe jupyter        # Start Jupyter
```

**With poetry:**
```bash
poetry run poe setup      # Set up environment
poetry run poe check      # Check if everything works
poetry run poe pull       # Update to latest version
poetry run jupyter lab    # Start Jupyter
```

**With pip:**
```bash
jupyter lab               # Start Jupyter (after pip install)
```

## 🔗 Getting Started

1. **Download this setup** (see Step 1 above)
2. **Choose your setup method** (see Step 2 above)
3. **Start Jupyter**:
   - With uv: `uv run --with jupyter jupyter lab`
   - With poetry: `poetry run jupyter lab`
   - With pip: `jupyter lab`
4. **Begin with Module 1** notebooks

## 🔄 Migration Path: Colab → Local Development

**When you're ready to move from Colab to local development:**

1. **Start with Colab** - Complete Module 1 with zero setup
2. **Download this setup** - When you need offline access or advanced features  
3. **Run Universal Setup** - `python setup_universal.py`
4. **Start Jupyter** - `uv run --with jupyter jupyter lab` (or equivalent)
5. **Continue seamlessly** - All your Colab work transfers directly

## 💡 Tips

- **Begin with Colab** for quick experiments and learning (no setup needed)
- **Upgrade to local** for serious work, offline access, and advanced features
- **Universal Setup** works on any platform with any package manager
- Ask your **AI assistant** for help with any questions!

## 🔧 Optional Package Installation

### Installing Optional EDA Tools (if needed for Module 2)

If you want to use the automated EDA features in Module 2, you can install these packages separately:

```bash
# With UV (recommended)
uv add ydata-profiling autoviz

# With pip (alternative)
pip install ydata-profiling autoviz
```

**Note**: These packages have dependency requirements that may conflict with other packages:
- **ydata-profiling**: Requires specific scipy versions
- **autoviz**: May have matplotlib style compatibility issues

The Module 2 notebooks are designed to work with or without these packages.

## 🆘 Troubleshooting

### Windows Issues

**PowerShell execution policy error?**
```powershell
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Command not found after installing uv?**
- Close and reopen PowerShell/Terminal
- The PATH should update automatically

**Python not found?**
- Install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### General Issues

**"No module named X" errors?**
- Try the Universal Setup: `python setup_universal.py`
- It will automatically use pip if uv/poetry aren't available

**Still having problems?**
- Start with Colab (no installation needed)
- Ask your AI assistant for help
- Check the course materials in Module 1

## 🐙 Setting Up Your Own GitHub Repository

Once you're comfortable with the basics, setting up your own GitHub repository will help you:
- **Save your work** and access it from anywhere
- **Share notebooks** with instructors and peers
- **Build a portfolio** of your data science projects
- **Collaborate** on group projects

### Step 1: Create Your Repository

1. **Go to GitHub.com** and sign in (or create an account)
2. **Click "New Repository"** (green button)
3. **Name your repository**: `aida-lab-my-work` (or similar)
4. **Make it Public** (so you can share your work)
5. **Add a README** (optional, but recommended)
6. **Click "Create Repository"**

### Step 2: Connect Your Local Setup

```bash
# Navigate to your aida-lab-env folder
cd aida-lab-env

# Initialize git (if not already done)
git init

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/aida-lab-my-work.git

# Add all files to git
git add .

# Make your first commit
git commit -m "Initial AIDA Lab setup"

# Push to GitHub
git push -u origin main
```

### Step 3: Organize Your Work

Create folders for each module:
```bash
mkdir module-01 module-02 module-03 module-04
mkdir module-05 module-06 module-07 module-08
```

### Step 4: Daily Workflow

```bash
# Start your day
cd aida-lab-env
uv run --with jupyter jupyter lab

# When you're done working
git add .
git commit -m "Completed Module 2 - Data Understanding"
git push
```

## 📁 Sharing Your Work

### Sharing Individual Notebooks

**Option 1: GitHub Gists (Recommended)**
1. **Open your notebook** in Jupyter
2. **File → Download as → Notebook (.ipynb)**
3. **Go to gist.github.com**
4. **Upload your .ipynb file**
5. **Share the gist link** with instructors/peers

**Option 2: GitHub Repository**
1. **Push your notebook** to your GitHub repo
2. **Share the GitHub link** to the specific file
3. **Others can view** and download your work

### Sharing Your Entire Project

**Option 1: Public Repository**
- **Make your repo public** on GitHub
- **Share the repository URL**
- **Others can clone** and run your work

**Option 2: Collaboration**
- **Invite collaborators** to your private repository
- **Use GitHub Issues** for project discussions
- **Use Pull Requests** for code reviews

## 🤝 Collaborative Development

### Working with Peers

**Setting up collaboration:**
1. **Invite collaborators** to your repository
2. **Create branches** for different features
3. **Use Pull Requests** for code reviews
4. **Use Issues** for project discussions

**Example workflow:**
```bash
# Create a new branch for a feature
git checkout -b feature/module-4-analysis

# Work on your feature
# ... make changes ...

# Commit your work
git add .
git commit -m "Add advanced visualization for Module 4"

# Push your branch
git push origin feature/module-4-analysis

# Create a Pull Request on GitHub
# (GitHub will show you a button after pushing)
```

### Working with Instructors

**Sharing your progress:**
1. **Push your work** to GitHub regularly
2. **Share specific notebook links** for feedback
3. **Use GitHub Issues** to ask questions
4. **Tag instructors** in comments for help

## 📊 Building Your Portfolio

### Organizing Your Work

**Create a portfolio structure:**
```
aida-lab-my-work/
├── README.md                 # Your project overview
├── module-01/               # Foundations
│   ├── notebook-1.ipynb
│   └── analysis-summary.md
├── module-02/               # Data Understanding
│   ├── eda-analysis.ipynb
│   └── insights.md
├── projects/                # Your own projects
│   ├── capstone-project/
│   └── personal-analysis/
└── portfolio/               # Showcase your best work
    ├── best-notebooks/
    └── project-showcase.md
```

### Showcasing Your Work

**Create a portfolio README:**
```markdown
# My AIDA Lab Journey 🚀

## About This Repository
This repository contains my work from the Applied AI in Data Analytics program.

## Key Projects
- **Module 2**: [Data Understanding Analysis](module-02/eda-analysis.ipynb)
- **Module 4**: [AI Insights Dashboard](module-04/insights-dashboard.ipynb)
- **Capstone**: [Final Project](projects/capstone-project/)

## Skills Developed
- Data analysis with pandas
- AI-assisted insights
- Data visualization
- Machine learning applications

## Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
```

## 🔧 Advanced Development Practices

### Version Control Best Practices

**Commit frequently:**
```bash
# Good commit messages
git commit -m "Add data cleaning for Module 3"
git commit -m "Fix visualization bug in Module 4"
git commit -m "Complete Module 5 analysis"

# Bad commit messages
git commit -m "stuff"
git commit -m "changes"
```

**Use branches for experiments:**
```bash
# Create experimental branch
git checkout -b experiment/new-visualization

# Try new approaches
# ... make changes ...

# If it works, merge back
git checkout main
git merge experiment/new-visualization

# If it doesn't work, delete the branch
git checkout main
git branch -d experiment/new-visualization
```

### Documentation

**Document your work:**
- **Add comments** to your notebooks
- **Write README files** for each module
- **Explain your analysis** in markdown cells
- **Include data sources** and methodology

**Example notebook structure:**
```python
# Cell 1: Title and Overview
"""
# Module 2: Data Understanding Analysis
## Objective: Analyze customer data with AI assistance
## Dataset: Customer transactions (2023)
## Tools: pandas, ydata-profiling, AI insights
"""

# Cell 2: Imports and Setup
import pandas as pd
import numpy as np
# ... other imports ...

# Cell 3: Data Loading
# Load and examine the dataset
df = pd.read_csv('customer_data.csv')
print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Cell 4: Analysis
# ... your analysis code ...

# Cell 5: Conclusions
"""
## Key Findings:
1. Customer segmentation reveals 3 distinct groups
2. AI insights suggest seasonal patterns
3. Recommendations for business strategy
"""
```

## 🎯 Next Steps

1. **Set up your GitHub repository** using the steps above
2. **Start with Module 1** and commit your work regularly
3. **Share your progress** with instructors and peers
4. **Build your portfolio** as you complete each module
5. **Collaborate** with classmates on group projects

## 💡 Pro Tips

- **Commit early and often** - don't wait until everything is perfect
- **Write clear commit messages** - your future self will thank you
- **Use branches** for experiments and new features
- **Document your work** - it helps with learning and sharing
- **Share your progress** - the community is here to help
- **Ask questions** - use GitHub Issues for technical questions

Happy learning! 🚀
