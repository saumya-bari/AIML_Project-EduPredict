from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"

DATA_FILE = DATA_DIR / "student_performance.csv"
MODEL_FILE = MODEL_DIR / "risk_model.joblib"
METRICS_FILE = MODEL_DIR / "metrics.json"

FEATURES = [
    "attendance",
    "study_hours",
    "assignment_completion",
    "internal_marks",
    "previous_gpa",
    "sleep_hours",
    "backlogs",
]
TARGET = "risk_level"
