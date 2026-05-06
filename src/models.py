
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def build_pipeline():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

def train_model(X, y):
    model = build_pipeline()
    model.fit(X, y)
    return model
