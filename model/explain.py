import shap
import joblib
import pandas as pd

model = joblib.load("model/loan_risk_model.pkl")

explainer = shap.TreeExplainer(model)

def explain_prediction(input_df):
    shap_values = explainer.shap_values(input_df)
    return shap_values