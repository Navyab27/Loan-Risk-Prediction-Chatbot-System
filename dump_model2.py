import joblib
import pprint

model = joblib.load("model/loan_risk_model.pkl")
print("Model type:", type(model))

# If RandomForest or similar, print feature importances
if hasattr(model, 'feature_importances_'):
    features = joblib.load("model/features.pkl")
    importances = model.feature_importances_
    fi = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)
    print("\nTop 10 Feature Importances:")
    pprint.pprint(fi[:10])
    
# If logistic regression, print coefficients
if hasattr(model, 'coef_'):
    features = joblib.load("model/features.pkl")
    coefs = model.coef_[0]
    ci = sorted(zip(features, coefs), key=lambda x: abs(x[1]), reverse=True)
    print("\nTop 10 Coefficients:")
    pprint.pprint(ci[:10])
