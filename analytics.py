import pandas as pd
from .model import load_model
from .validator import validate_record

def predict_risk(record):
    errors = validate_record(record)
    if errors:
        raise ValueError("; ".join(errors))

    model = load_model()
    df = pd.DataFrame([record])
    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence = float(max(probabilities))

    return {
        "risk_level": prediction,
        "confidence": round(confidence, 4),
    }
