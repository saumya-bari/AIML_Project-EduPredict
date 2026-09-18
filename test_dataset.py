import pandas as pd
from .config import DATA_FILE, FEATURES, TARGET

def load_dataset():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "Dataset not found. Run: python -m src.generate_dataset"
        )
    df = pd.read_csv(DATA_FILE)
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing columns: {missing}")
    return df
