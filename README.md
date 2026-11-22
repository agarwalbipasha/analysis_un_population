# UN Population Analysis

A Python project that analyzes UN population dataset (`data_population.csv`) to generate statistical insights and `matplotlib` visualizations.

## Prerequisites

- Python 3.10+
- UN population dataset file (`data_population.csv`) placed in the project data directory

## Setup & Installation

1. **Navigate to the project directory:**
   ```bash
   cd analysis_un_population
   ```

2. **Create and activate a virtual environment:**
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not generated yet, run: `pip install matplotlib pylint`)*

## Running the Solutions

Ensure your virtual environment `(.venv)` is active, then execute any solution script from the root directory:

```bash
python solutions/solution1.py
python solutions/solution2.py
python solutions/solution3.py
python solutions/solution4.py
```

## Code Quality Check

Run `pylint` across all solution and helper modules to verify code quality:

```bash
pylint solution*.py
```
