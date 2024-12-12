# EPL JUPYTER

# Premier League Probability Analysis

## Overview
This repository allows users to scrape, process, and analyze English Premier League match data. Users can calculate probabilities for 1 x 2 match results and over/under goals using statistical modeling.

Alternatively, analysis for upcoming and past matches can be viewed in the output directory. They are named by the matchup and in directories by date eg. `output/12-14-24/ars_v_evt.ipynb`. This project began midway through the 2024-2025 season.

All probabilities are currently based on *this season's results*. If you choose to gamble, do so with caution and remember that *all models are wrong, some are useful*.

Good luck and have fun 🚀

## Prerequisites
1. Python 3.8 or later
2. Jupyter Lab
3. Browser to access Jupyter Lab

## Installation and Setup

### 1. Fork and Clone the Repository
1. Click on the **Fork** button on the top-right corner of this repository to fork it to your GitHub account.
2. Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   ```
3. Navigate to the project directory:
   ```bash
   cd <repo-name>
   ```

### 2. Set Up a Virtual Environment (Recommended)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Launch Jupyter Lab
Start your Jupyter Lab server in the project directory:
```bash
jupyter lab
```

Access the server using the link provided in your terminal.

---

## Workflow Instructions
The analysis involves three Jupyter notebooks located in the `/notebooks` directory. Follow these steps:

### Notebook 1: `01_scrape_data.ipynb`
#### Purpose:
Scrapes match data from Understat and saves it as raw CSV files in the `data/raw/` directory.

#### Instructions:
1. Open `01_scrape_data.ipynb`.
2. Run all cells (`Run All` or press `Shift + Enter`).
3. Confirm that `data/raw/home_table.csv` and `data/raw/away_table.csv` are updated.
4. Proceed to `02_process_data.ipynb`.

---

### Notebook 2: `02_process_data.ipynb`
#### Purpose:
Processes raw match data to calculate metrics needed for probability analysis.

#### Instructions:
1. Open `02_process_data.ipynb`.
2. Run all cells (`Run All` or press `Shift + Enter`).
3. Verify processed data is saved to:
   - `data/processed/home_table.csv`
   - `data/processed/away_table.csv`
4. Proceed to `03_analysis_template.ipynb`.

---

### Notebook 3: `03_analysis_template.ipynb`
#### Purpose:
Performs probability calculations for a specific match and generates insights.

#### Instructions:
1. Open `03_analysis_template.ipynb`.
2. Ensure all cells in `01_scrape_data.ipynb` and `02_process_data.ipynb` have been run.
3. Define the `home_side` and `away_side` in the first cell.
4. Run all cells (`Run All` or press `Shift + Enter`).
5. View the calculated probabilities and projections in the final cell.
6. Optionally:
   - Copy the notebook to `output/<matchday_directory>/`.
   - Rename the file for match-specific analysis.

---

## File Structure
```
<repo-name>/
├── data/
│   ├── raw/
│   │   ├── home_table.csv
│   │   └── away_table.csv
│   ├── processed/
│       ├── home_table.csv
│       └── away_table.csv
├── notebooks/
│   ├── 01_scrape_data.ipynb
│   ├── 02_process_data.ipynb
│   └── 03_analysis_template.ipynb
├── output/
│   └── <matchday_directory>/
├── src/
│   └── utils/
└── requirements.txt
```

## Notes
- All CSV files are automatically saved during processing.
- Follow instructions within each notebook for smooth execution.
- Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

---

Happy Analyzing!
