import joblib
import pandas as pd

features = joblib.load("model/features.pkl")
print("Features:", features)

try:
    scaler = joblib.load("model/scaler.pkl")
    print("Scaler type:", type(scaler))
    print("Scaler features:", getattr(scaler, "feature_names_in_", None))
    print("Scaler mean:", getattr(scaler, "mean_", None))
except Exception as e:
    print("Scaler err:", e)
