from sklearn.model_selection import train_test_split
from .config import FEATURES, TARGET

def prepare_data(dataframe):
    X = dataframe[FEATURES]
    y = dataframe[TARGET]
    return train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
