from pathlib import Path
import random
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_FILE = DATA_DIR / "student_performance.csv"

def generate_dataset(rows=600, seed=42):
    random.seed(seed)
    records = []
    for _ in range(rows):
        attendance = random.randint(45, 100)
        study_hours = round(random.uniform(1, 10), 1)
        assignment_completion = random.randint(40, 100)
        internal_marks = random.randint(35, 95)
        previous_gpa = round(random.uniform(4.5, 9.5), 2)
        sleep_hours = round(random.uniform(4, 9), 1)
        backlogs = random.randint(0, 5)

        score = (
            attendance * 0.20
            + study_hours * 5
            + assignment_completion * 0.15
            + internal_marks * 0.25
            + previous_gpa * 5
            + sleep_hours
            - backlogs * 5
        )

        if score >= 75:
            risk_level = "Low"
        elif score >= 55:
            risk_level = "Medium"
        else:
            risk_level = "High"

        records.append({
            "attendance": attendance,
            "study_hours": study_hours,
            "assignment_completion": assignment_completion,
            "internal_marks": internal_marks,
            "previous_gpa": previous_gpa,
            "sleep_hours": sleep_hours,
            "backlogs": backlogs,
            "risk_level": risk_level,
        })

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv(DATA_FILE, index=False)

    old_file = PROJECT_ROOT / "src" / "student_performance.csv"
    if old_file.exists():
        old_file.unlink()

    print(f"Generated {rows} rows: {DATA_FILE}")
    return DATA_FILE

if __name__ == "__main__":
    generate_dataset()
