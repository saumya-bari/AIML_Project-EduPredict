import json
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

from .config import MODEL_DIR, MODEL_FILE, METRICS_FILE
from .data_loader import load_dataset
from .preprocessor import prepare_data

def train_model():
    df = load_dataset()
    X_train, X_test, y_train, y_test = prepare_data(df)

    model = RandomForestClassifier(
        n_estimators=250,
        max_depth=8,
        min_samples_leaf=3,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "weighted_precision": round(float(precision_score(y_test, predictions, average="weighted", zero_division=0)), 4),
        "weighted_recall": round(float(recall_score(y_test, predictions, average="weighted", zero_division=0)), 4),
        "weighted_f1": round(float(f1_score(y_test, predictions, average="weighted", zero_division=0)), 4),
        "test_rows": int(len(y_test)),
        "classification_report": classification_report(y_test, predictions, zero_division=0, output_dict=True),
    }

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_FILE)
    with open(METRICS_FILE, "w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)

    print("Model trained successfully.")
    print(f"Model saved to: {MODEL_FILE}")
    print(f"Metrics saved to: {METRICS_FILE}")
    print("Accuracy:", metrics["accuracy"])
    print("Weighted F1:", metrics["weighted_f1"])
    return metrics

def load_model():
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            "Trained model not found. Run: python -m src.main train"
        )
    return joblib.load(MODEL_FILE)
