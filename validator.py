from .config import FEATURES
from .data_loader import load_dataset
from .model import load_model

def dataset_summary():
    df = load_dataset()
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "risk_distribution": df["risk_level"].value_counts().to_dict(),
        "average_attendance": round(float(df["attendance"].mean()), 2),
        "average_gpa": round(float(df["previous_gpa"].mean()), 2),
    }

def feature_importance():
    model = load_model()
    return dict(sorted(
        zip(FEATURES, model.feature_importances_),
        key=lambda item: item[1],
        reverse=True
    ))
