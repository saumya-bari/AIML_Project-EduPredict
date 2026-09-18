import json
from .config import METRICS_FILE

def load_metrics():
    if not METRICS_FILE.exists():
        raise FileNotFoundError(
            "Metrics not found. Run: python -m src.main train"
        )
    with open(METRICS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def print_metrics():
    metrics = load_metrics()
    print("Evaluation Metrics")
    print("------------------")
    print("Accuracy:", metrics["accuracy"])
    print("Weighted Precision:", metrics["weighted_precision"])
    print("Weighted Recall:", metrics["weighted_recall"])
    print("Weighted F1:", metrics["weighted_f1"])
    print("Test Rows:", metrics["test_rows"])
