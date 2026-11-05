"""
Student Study-Hours and Performance Dashboard
Python Lab End-Semester Project

Run:
    pip install -r requirements.txt
    python app.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

REQUIRED_COLUMNS = ["student_id", "student_name", "study_hours", "score"]


def ensure_files():
    """Create required folders and a starter CSV if it does not exist."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        sample = [
            ["S001", "Student 1", 1.5, 38],
            ["S002", "Student 2", 2.0, 45],
            ["S003", "Student 3", 2.5, 52],
            ["S004", "Student 4", 3.0, 58],
            ["S005", "Student 5", 3.5, 63],
            ["S006", "Student 6", 4.0, 68],
            ["S007", "Student 7", 4.5, 72],
            ["S008", "Student 8", 5.0, 78],
            ["S009", "Student 9", 5.5, 83],
            ["S010", "Student 10", 6.0, 88],
            ["S011", "Student 11", 6.5, 92],
            ["S012", "Student 12", 7.0, 96],
        ]
        pd.DataFrame(sample, columns=REQUIRED_COLUMNS).to_csv(DATA_FILE, index=False)


def load_data():
    """Load records and validate the file structure and values."""
    ensure_files()
    try:
        df = pd.read_csv(DATA_FILE)
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        raise ValueError(f"Could not read the CSV file: {error}")

    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError("CSV is missing required columns: " + ", ".join(missing))

    df = df[REQUIRED_COLUMNS].copy()
    df["student_id"] = df["student_id"].astype(str).str.strip()
    df["student_name"] = df["student_name"].astype(str).str.strip()
    df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("Some records contain blank or invalid values. Please correct data/students.csv.")
    if (df["student_id"] == "").any() or (df["student_name"] == "").any():
        raise ValueError("Student ID and student name cannot be blank.")
    if df["student_id"].duplicated().any():
        raise ValueError("Duplicate student IDs found. Each student ID must be unique.")
    if ((df["study_hours"] < 0) | (df["study_hours"] > 24)).any():
        raise ValueError("Study hours must be between 0 and 24.")
    if ((df["score"] < 0) | (df["score"] > 100)).any():
        raise ValueError("Scores must be between 0 and 100.")
    return df


def get_grade(score):
    """Return a readable performance category for a score."""
    if score >= 90:
        return "Excellent"
    if score >= 75:
        return "Very Good"
    if score >= 60:
        return "Good"
    if score >= 40:
        return "Developing"
    return "Needs Improvement"


def show_records(df):
    view = df.copy()
    view["performance"] = view["score"].apply(get_grade)
    print("\nSTUDENT RECORDS")
    print("-" * 76)
    print(view.to_string(index=False, formatters={"study_hours": "{:.1f}".format,
                                                  "score": "{:.1f}".format}))
    print("-" * 76)


def show_dashboard(df):
    total = len(df)
    average_hours = df["study_hours"].mean()
    average_score = df["score"].mean()
    highest = df.loc[df["score"].idxmax()]
    lowest = df.loc[df["score"].idxmin()]
    passed = int((df["score"] >= 40).sum())

    print("\n" + "=" * 48)
    print("       STUDENT PERFORMANCE DASHBOARD")
    print("=" * 48)
    print(f"Total students          : {total}")
    print(f"Average study hours     : {average_hours:.2f} hours")
    print(f"Average assessment score: {average_score:.2f} / 100")
    print(f"Highest score           : {highest['score']:.1f} ({highest['student_name']})")
    print(f"Lowest score            : {lowest['score']:.1f} ({lowest['student_name']})")
    print(f"Students scoring 40+    : {passed}")
    print(f"Students below 40       : {total - passed}")
    print("=" * 48)

    print("\nPERFORMANCE CATEGORY SUMMARY")
    categories = df["score"].apply(get_grade).value_counts()
    order = ["Excellent", "Very Good", "Good", "Developing", "Needs Improvement"]
    for category in order:
        print(f"{category:22}: {int(categories.get(category, 0))}")


def add_record():
    df = load_data()
    print("\nADD A NEW STUDENT")
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be blank.")
        return
    if student_id in df["student_id"].values:
        print("This student ID already exists.")
        return

    name = input("Enter student name (or an anonymous label): ").strip()
    if not name:
        print("Student name cannot be blank.")
        return

    try:
        hours = float(input("Enter daily study hours (0 to 24): "))
        score = float(input("Enter assessment score (0 to 100): "))
    except ValueError:
        print("Please enter numbers for study hours and score.")
        return

    if not 0 <= hours <= 24:
        print("Study hours must be between 0 and 24.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
        return

    new_row = pd.DataFrame([[student_id, name, hours, score]], columns=REQUIRED_COLUMNS)
    updated = pd.concat([df, new_row], ignore_index=True)
    updated.to_csv(DATA_FILE, index=False)
    print("Student record added successfully.")


def create_charts(df):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Chart 1: Study hours compared with assessment score
    plt.figure(figsize=(8, 5))
    plt.scatter(df["study_hours"], df["score"])
    plt.title("Study Hours vs Assessment Score")
    plt.xlabel("Daily Study Hours")
    plt.ylabel("Assessment Score")
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)
    scatter_path = OUTPUT_DIR / "study_hours_vs_score.png"
    plt.tight_layout()
    plt.savefig(scatter_path, dpi=150)
    plt.show()
    plt.close()

    # Chart 2: Distribution of assessment scores
    plt.figure(figsize=(8, 5))
    plt.hist(df["score"], bins=5, edgecolor="black")
    plt.title("Distribution of Student Scores")
    plt.xlabel("Assessment Score")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", alpha=0.3)
    histogram_path = OUTPUT_DIR / "score_distribution.png"
    plt.tight_layout()
    plt.savefig(histogram_path, dpi=150)
    plt.show()
    plt.close()

    print(f"Charts saved in: {OUTPUT_DIR}")


def export_summary(df):
    summary = pd.DataFrame({
        "Metric": [
            "Total students",
            "Average study hours",
            "Average score",
            "Highest score",
            "Lowest score",
            "Students scoring 40 or above",
            "Students scoring below 40",
        ],
        "Value": [
            len(df),
            round(df["study_hours"].mean(), 2),
            round(df["score"].mean(), 2),
            round(df["score"].max(), 2),
            round(df["score"].min(), 2),
            int((df["score"] >= 40).sum()),
            int((df["score"] < 40).sum()),
        ],
    })
    output_file = OUTPUT_DIR / "performance_summary.csv"
    summary.to_csv(output_file, index=False)
    print(f"Summary exported to: {output_file}")


def main():
    ensure_files()
    print("Welcome to the Student Study-Hours and Performance Dashboard!")

    while True:
        print("\nMAIN MENU")
        print("1. View student records")
        print("2. View performance dashboard")
        print("3. Add a student record")
        print("4. Generate charts")
        print("5. Export summary as CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        try:
            df = load_data()
            if choice == "1":
                show_records(df)
            elif choice == "2":
                show_dashboard(df)
            elif choice == "3":
                add_record()
            elif choice == "4":
                create_charts(df)
            elif choice == "5":
                export_summary(df)
            elif choice == "6":
                print("Thank you for using the dashboard. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        except (ValueError, KeyError) as error:
            print(f"\nData error: {error}")
            print("Check data/students.csv and try again.")


if __name__ == "__main__":
    main()
