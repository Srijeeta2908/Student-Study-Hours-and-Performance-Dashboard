# Student Study-Hours and Performance Dashboard

## Project overview
A menu-driven Python application that analyses anonymised student study-hour and assessment-score records. It displays academic statistics, classifies performance, creates charts, and exports a summary.

## Features
- Read student records from a CSV file using Pandas.
- Validate missing values, duplicate IDs, study-hour limits, and score limits.
- Display student records and performance categories.
- Calculate class averages, highest and lowest scores, and pass/fail counts.
- Generate a scatter plot and a score-distribution histogram using Matplotlib.
- Add a new student record.
- Export a performance summary to CSV.

## Requirements
- Python 3.9 or later
- VS Code (recommended)
- Internet connection only for the first installation of the Python packages

## Setup and run
1. Extract this project folder.
2. Open the `student_performance_dashboard` folder in VS Code.
3. Open the VS Code terminal.
4. Create a virtual environment (recommended):

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install packages:
   ```bash
   python -m pip install -r requirements.txt
   ```
6. Run:
   ```bash
   python app.py
   ```

If `python` does not work on Windows, try `py app.py`.

## Menu
1. View student records
2. View performance dashboard
3. Add a student record
4. Generate charts
5. Export summary as CSV
6. Exit

## Input file
`data/students.csv` contains sample anonymised records with these columns:
- `student_id`: unique student code
- `student_name`: anonymous label or student name
- `study_hours`: daily study hours (0–24)
- `score`: assessment score (0–100)

You can replace the sample records with your own anonymised test data. Keep the column names unchanged.

## Performance categories
| Score | Category |
|---|---|
| 90–100 | Excellent |
| 75–89.99 | Very Good |
| 60–74.99 | Good |
| 40–59.99 | Developing |
| Below 40 | Needs Improvement |

The pass threshold used in the dashboard is 40. Confirm with your faculty if your course uses a different threshold.

## Output
Generated charts and exported summaries are saved in the `outputs` folder.

## Important note
The included data is synthetic sample data for demonstration. It does not represent actual students and should not be used to make real academic decisions.
