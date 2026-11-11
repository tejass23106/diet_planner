# Diet Planner — Budget-Based Meal Planning App

<p align="center">
  <strong>Plan smarter meals. Balance your budget, calories, and protein.</strong>
  <br />
  An interactive Streamlit application that suggests food combinations based on a daily spending limit, calorie target, and dietary preference.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Handling-150458?logo=pandas" alt="Pandas" />
  <img src="https://img.shields.io/badge/Status-Student%20Project-blue" alt="Student project" />
</p>

---

## Table of Contents

1. [Overview](#1-overview)
2. [Project Highlights](#2-project-highlights)
3. [Features](#3-features)
4. [How It Works](#4-how-it-works)
5. [Meal Planning Logic](#5-meal-planning-logic)
6. [Food Catalogue](#6-food-catalogue)
7. [Technology Stack](#7-technology-stack)
8. [Application Architecture](#8-application-architecture)
9. [Project Structure](#9-project-structure)
10. [Requirements](#10-requirements)
11. [Installation and Setup](#11-installation-and-setup)
12. [Running the Application](#12-running-the-application)
13. [Using the Planner](#13-using-the-planner)
14. [Configuration and Customization](#14-configuration-and-customization)
15. [Troubleshooting](#15-troubleshooting)
16. [Current Scope and Limitations](#16-current-scope-and-limitations)
17. [Possible Future Improvements](#17-possible-future-improvements)
18. [Git Workflow](#18-git-workflow)
19. [Author](#19-author)

---

## 1. Overview

**Diet Planner** is a Python-based web application built with Streamlit. It helps users explore food combinations while considering three inputs:

- Daily food budget in Indian Rupees (₹).
- Daily calorie target in kilocalories (kcal).
- Dietary preference: vegetarian, non-vegetarian, or both.

The application filters a built-in food catalogue, generates a suggested selection using a greedy selection strategy, and displays estimated cost, protein, and calorie totals. It also highlights foods with a high protein-to-calorie ratio.

The interface makes the planning logic easy to explore without requiring a database, login, or separate backend service.

> **Important:** Food prices and nutrition values are hard-coded sample estimates. They are not live market prices or personalized nutritional recommendations. Check food labels and consult a qualified nutrition professional for individual dietary needs.

---

## 2. Project Highlights

| Area | Implementation |
|---|---|
| Application type | Interactive web app |
| Main use case | Budget- and calorie-aware food selection |
| Frontend and runtime | Streamlit |
| Programming language | Python |
| Data handling | Pandas |
| Selection and ranking | Python sorting and `heapq` |
| Food catalogue | In-code list of dictionaries |
| Dietary filters | Vegetarian, non-vegetarian, both |
| Currency display | Indian Rupee (₹) |
| Launch options | Streamlit CLI or Windows batch file |
| Database | Not required |
| Authentication | Not implemented |

---

## 3. Features

### 3.1 Budget-Based Planning

Set a daily budget using the sidebar control. The planner only adds a food item when its listed cost fits within the remaining budget.

### 3.2 Calorie Target

Choose a target calorie amount. The selection loop avoids adding an item if doing so would take the running calorie total above the selected target.

If the available food combinations cannot reach the target within the budget and calorie constraints, the application displays a message.

### 3.3 Dietary Preference

Choose one of three catalogue filters:

- **Veg:** includes vegetarian food entries.
- **Non-Veg:** includes non-vegetarian food entries.
- **Both:** includes all entries.

### 3.4 Suggested Meal Plan

When a selection is available, the app displays a table containing:

- Food name and listed serving description.
- Estimated cost.
- Protein in grams.
- Calories in kcal.
- Vegetarian classification.

### 3.5 Nutrition and Cost Summary

The dashboard summarizes:

- Total estimated cost.
- Total protein.
- Total calories.
- Selected calorie goal.

### 3.6 Protein-Efficient Food Ranking

The app identifies up to five foods with the highest protein-to-calorie ratio from the currently eligible catalogue.

The ratio is calculated as:

```text
Protein efficiency = Protein (g) / Calories (kcal)
```

This ranking is separate from the budget-based meal selection. It is a comparison aid, not a complete measure of food quality.

### 3.7 Available Food Table

The optional **Show available foods** setting displays entries eligible under the selected dietary preference.

---

## 4. How It Works

The application follows this data-processing flow:

```text
User Input
   |
   v
Budget + Calorie Target + Diet Preference
   |
   v
Filter Food Catalogue
   |
   +------------------------------+
   |                              |
   v                              v
Greedy Meal Selection       Protein-Efficiency Ranking
   |                              |
   v                              v
Cost / Protein / Calories    Top 5 Foods
   |                              |
   +---------------+--------------+
                   |
                   v
           Streamlit Dashboard
```

### User Input

The sidebar collects the budget, calorie target, diet type, and food-table visibility setting.

### Catalogue Filtering

The selected diet type determines which food entries are eligible for planning and ranking.

### Result Presentation

Pandas DataFrames organize the suggested meal plan and food catalogue before Streamlit renders the tables and metric cards.

---

## 5. Meal Planning Logic

The core logic is implemented in `diet.py`.

### 5.1 Food Filtering

The planner creates an eligible food list based on the selected diet type:

- `veg` keeps entries whose `veg` field is `True`.
- `nonveg` keeps entries whose `veg` field is `False`.
- `both` keeps every entry.

### 5.2 Greedy Selection

Eligible foods are sorted in descending order by protein and then calories. The application iterates through this sorted list and adds a food entry only if both conditions remain satisfied:

```text
Current cost + food cost <= Daily budget

Current calories + food calories <= Calorie target
```

For each selected entry, the application updates total cost, protein, and calories. The loop stops when the calorie target is reached or all eligible entries have been checked.

### 5.3 Protein-Efficiency Ranking with a Min-Heap

The `get_top_foods()` function uses Python's `heapq` module to retain up to five entries with the highest protein-per-calorie ratio.

This keeps the ranking focused on the best-scoring entries without sorting the entire catalogue solely to retrieve the top five.

### 5.4 Main Functions

| Function | Responsibility |
|---|---|
| `get_meal_plan(budget, tcalories, diet_type)` | Filters foods, selects a plan, calculates totals, and returns top foods |
| `get_top_foods(eligible_foods, limit=5)` | Finds the most protein-efficient food entries using a min-heap |
| `format_currency(value)` | Formats a numeric amount as Indian Rupees |
| `main()` | Configures and renders the Streamlit application |

---

## 6. Food Catalogue

The current catalogue is defined directly in `diet.py`. Each entry contains:

| Field | Description |
|---|---|
| `food` | Food name and listed serving description |
| `cost` | Estimated cost in ₹ |
| `protein` | Estimated protein in grams |
| `calories` | Estimated energy in kcal |
| `veg` | Boolean dietary classification |

The catalogue includes oats, rice, roti, dal, chana, soya chunks, paneer, milk, fruits, nuts, eggs, chicken, fish, and other food items.

The listed serving descriptions are part of the sample data. The application currently treats each catalogue entry as one selectable unit; it does not calculate scaled portions or quantities.

---

## 7. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic and data processing |
| Streamlit | Interactive web interface and application runtime |
| Pandas | Tabular data preparation and display |
| `heapq` | Min-heap implementation for top-food ranking |

The project also uses Python's built-in `heapq` module. It is part of Python and does not need to be installed separately.

---

## 8. Application Architecture

Diet Planner is a single-process Streamlit application.

```text
             User's Browser
                   |
                   v
          Streamlit Web Interface
                   |
                   v
                 diet.py
                   |
        +----------+----------+
        |                     |
        v                     v
  Food Catalogue        Planning Logic
  (Python List)         - Diet filtering
                        - Greedy selection
                        - Total calculations
                        - Heap-based ranking
        |                     |
        +----------+----------+
                   |
                   v
             Pandas DataFrames
                   |
                   v
        Tables and Metric Cards
```

There is no separate REST API, database server, or authentication service in the current implementation.

---

## 9. Project Structure

```text
diet_planner/
│
├── .gitignore
├── README.md
├── diet.py
├── requirements.txt
└── run.bat
```

### Important Files

| File | Responsibility |
|---|---|
| `diet.py` | Food catalogue, planning functions, ranking logic, and Streamlit UI |
| `requirements.txt` | Python package dependencies |
| `run.bat` | Windows launcher for the Streamlit application |
| `.gitignore` | Excludes virtual environments, Python cache files, and local environment files |
| `README.md` | Project documentation and setup guide |

---

## 10. Requirements

### Software

- Python 3.11 or later.
- pip (Python package installer).
- A modern web browser.
- Git (optional, for cloning and version control).

### Python Packages

The project uses two direct third-party dependencies:

- **Streamlit** — runs the interactive web application.
- **Pandas** — prepares the food and meal-plan tables.

The complete dependency list is maintained in `requirements.txt`.

---

## 11. Installation and Setup

### Step 1 — Clone the Repository

```bash
git clone https://github.com/tejass23106/diet_planner.git
cd diet_planner
```

If you have already downloaded the project, open a terminal in the project directory instead.

### Step 2 — Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

**macOS / Linux:**

```bash
python3 -m venv .venv
```

### Step 3 — Activate the Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### Step 4 — Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 12. Running the Application

Run the following command from the project root:

```bash
python -m streamlit run diet.py
```

Streamlit starts a local server and prints the local application URL in the terminal. Open that URL in your browser (normally `http://localhost:8501`).

### Windows Batch Launcher

On Windows, you can also run:

```bat
run.bat
```

Or double-click `run.bat` from File Explorer. The batch file runs the app through Python's Streamlit module and keeps the terminal open.

### Stop the Application

Return to the terminal running Streamlit and press `Ctrl + C`.

---

## 13. Using the Planner

1. Start the application.
2. Open **Planner settings** in the sidebar.
3. Enter the daily budget in ₹.
4. Set the calorie target in kcal.
5. Select `veg`, `nonveg`, or `both`.
6. Choose whether to show the available-food table.
7. Review the suggested meal plan and summary metrics.
8. Compare the top protein-efficient foods.
9. Adjust the inputs to explore different combinations.

If no food entry can be selected under the current constraints, increase the budget or adjust the calorie target and try again.

---

## 14. Configuration and Customization

### Add or Edit Food Entries

Open `diet.py` and locate the `foods` list near the beginning of the file.

Each food is represented as a dictionary:

```python
{
    "food": "Example Food (100g)",
    "cost": 25,
    "protein": 10,
    "calories": 150,
    "veg": True
}
```

Keep the field names and data types consistent:

- `food`: string.
- `cost`: numeric value.
- `protein`: numeric value.
- `calories`: numeric value.
- `veg`: `True` or `False`.

### Change the Default Planner Inputs

Inside `main()`, the sidebar controls define the initial budget and calorie target. Update the `value` arguments in the corresponding `st.number_input()` calls to change their defaults.

### Change the Number of Ranked Foods

The current implementation requests five entries:

```python
top_foods = get_top_foods(filtered, limit=5)
```

Change `limit` to display a different number of top-ranked entries.

---

## 15. Troubleshooting

### `streamlit` Is Not Recognized

Run Streamlit through the active Python interpreter:

```bash
python -m streamlit run diet.py
```

Also confirm that the virtual environment is activated and dependencies are installed.

### Module Not Found

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

### Application Opens on a Different Port

If port 8501 is already occupied, Streamlit may report another available local URL. Open the URL printed in the terminal.

### PowerShell Does Not Allow Environment Activation

If script execution policy blocks activation, use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

You can also run the application using the virtual environment's Python executable without activating it:

```powershell
.venv\Scripts\python.exe -m streamlit run diet.py
```

### No Meal Plan Is Generated

The selected budget, calorie target, and dietary filter may not allow any catalogue entry to be selected. Try increasing the budget, changing the diet filter, or adjusting the calorie target.

---

## 16. Current Scope and Limitations

The current version is a lightweight planning demonstration. Its behavior is limited to the data and logic present in the repository.

| Area | Current implementation |
|---|---|
| Food data | Hard-coded Python list |
| Price and nutrition values | Sample estimates |
| Meal selection | Greedy, sorted selection |
| Portion scaling | Not implemented |
| Dietary filtering | Vegetarian / non-vegetarian / both |
| Protein ranking | Protein-to-calorie ratio |
| Persistence | No database or saved user plans |
| User accounts | Not implemented |
| Personal health profiles | Not implemented |
| External nutrition API | Not connected |
| Live price updates | Not supported |
| Deployment URL | No live deployment configured in this repository |

### Algorithmic Note

The greedy selection strategy is simple and fast, but it does not guarantee a globally optimal meal combination. It sorts foods by protein and calories, then selects entries that fit the remaining budget and calorie limit. A different combination could sometimes provide a better overall result.

The current catalogue also treats every entry as a single fixed unit. It does not optimize serving sizes or generate breakfast, lunch, and dinner schedules.

### Nutrition Disclaimer

All cost and nutrition figures are illustrative values embedded in the source code. Actual nutrition can vary by brand, preparation method, ingredient, and serving size. This project should not be used as a substitute for professional dietary advice.

---

## 17. Possible Future Improvements

Potential enhancements for future versions include:

### Planning and Optimization
- Use a knapsack or other constrained-optimization algorithm.
- Support adjustable food quantities and serving sizes.
- Generate separate breakfast, lunch, and dinner suggestions.
- Add minimum protein and other nutrient targets.

### Data and Nutrition
- Move food data into CSV or JSON files.
- Add editable food catalogue management.
- Integrate a verified nutrition data source.
- Allow regional price customization.

### User Experience
- Add downloadable meal-plan reports.
- Add visual nutrition charts.
- Improve input validation and empty-result guidance.
- Add meal-plan comparison.

### Persistence and Deployment
- Save user preferences and generated plans.
- Add optional user accounts.
- Deploy the Streamlit app and publish a live demo.

These are ideas for future development and are not currently implemented features.

---

## 18. Git Workflow

### Clone

```bash
git clone https://github.com/tejass23106/diet_planner.git
cd diet_planner
```

### Check Changes

```bash
git status
```

### Stage Changes

```bash
git add README.md requirements.txt
```

### Commit

```bash
git commit -m "docs: improve project README and dependencies"
```

### Push

```bash
git push origin main
```

### Pull Latest Changes

```bash
git pull origin main
```

---

## 19. Author

**Tejas Kumar S**

Computer Science and Engineering Student

- GitHub: [@tejass23106](https://github.com/tejass23106)
- Project Repository: [Diet Planner](https://github.com/tejass23106/diet_planner)

---

<p align="center">
  <strong>Diet Planner</strong>
  <br />
  Plan within your budget. Keep your goals in view.
</p>