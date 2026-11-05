# Student Study-Hours and Performance Dashboard
## Preliminary Project Report

**Course:** B.Tech Python Lab  
**Project topic:** Student Study-Hours and Performance Dashboard  
**Student name:** Tirtha Banerjee  
**Institution:** Institute of Engineering & Management, Kolkata  
**Academic year:** 2026

> This is a preliminary report draft. The final report should be rearranged to match the exact format supplied by your faculty.

## 1. Abstract
The Student Study-Hours and Performance Dashboard is a Python-based application designed to analyse anonymised student study hours and assessment scores. It reads records from a CSV file, validates the data, calculates useful statistical values, classifies student performance, and presents results through charts. It also allows the user to add records and export a summary. The project demonstrates the practical use of Python functions, conditional statements, loops, file handling, Pandas, and Matplotlib.

## 2. Problem statement
Student study time and assessment results are often stored as separate records. Manually calculating averages, identifying score ranges, and comparing study hours with marks can take time. This project provides a simple program to organise and analyse these records.

## 3. Objectives
- Store student study-hour and score records in a CSV file.
- Validate input data before analysis.
- Calculate average study hours and assessment scores.
- Identify the highest and lowest scores.
- Classify scores into performance categories.
- Visualise the data using charts.
- Export a summary for later reference.

## 4. Tools and technologies
- Python 3
- Visual Studio Code
- Pandas for reading, processing, and summarising tabular data
- Matplotlib for charts
- CSV for data storage

## 5. System requirements
**Hardware:** A computer capable of running Python and VS Code.  
**Software:** Python 3.9 or later, VS Code, and the packages listed in `requirements.txt`.

## 6. Working methodology
1. Read student records from `data/students.csv`.
2. Check required columns and validate IDs, study hours, and scores.
3. Calculate class-level statistics.
4. Assign a performance category to each score.
5. Display the results in the terminal.
6. Generate a scatter plot and histogram when requested.
7. Save an analysis summary as a CSV file when requested.

## 7. Performance categories
- 90–100: Excellent
- 75–89.99: Very Good
- 60–74.99: Good
- 40–59.99: Developing
- Below 40: Needs Improvement

The demonstration dashboard uses 40 as the pass threshold.

## 8. Expected output
The program displays student records, class averages, highest and lowest scores, counts above and below the pass threshold, and a category-wise performance summary. It also saves two charts and a CSV summary in the `outputs` folder.

## 9. Testing
Test the application with:
- Valid student records.
- A duplicate student ID.
- A score below 0 or above 100.
- Study hours below 0 or above 24.
- A non-numeric score or study-hour value.
- An empty or incorrectly structured CSV file.

Expected behaviour: valid data is processed; invalid data is rejected with a clear error message.

## 10. Limitations
- The sample data is synthetic and small.
- Study hours are self-reported and may not be exact.
- A relationship between study hours and scores does not prove that study time alone causes higher marks.
- The program is a local demonstration, not a secure institutional student database.

## 11. Future scope
The project can later include subject-wise scores, semester comparisons, a graphical user interface, larger datasets, and a web-based dashboard.

## 12. Conclusion
The project demonstrates how Python can be used to store, validate, analyse, and visualise student performance data. It combines core Python programming with practical data-analysis libraries and produces useful summaries in a simple menu-driven application.

## 13. References
- Python documentation: https://docs.python.org/3/
- Pandas documentation: https://pandas.pydata.org/docs/
- Matplotlib documentation: https://matplotlib.org/stable/
