import requests
import json

url = "http://127.0.0.1:8000/predict"
def test_case(loan_amnt, int_rate, annual_inc, dti):
    data = {
        "loan_amnt": loan_amnt,
        "term": 36,
        "int_rate": int_rate,
        "installment": 900,
        "emp_length": 2,
        "annual_inc": annual_inc,
        "dti": dti,
        "delinq_2yrs": 2,
        "revol_util": 85,
        "total_acc": 10,
        "loan_income_ratio": 0.8,
        "credit_risk_score": 7,
        "payment_burden": 0.03,
        "grade_B": 0, "grade_C": 0, "grade_D": 1, "grade_E": 0, "grade_F": 0, "grade_G": 0,
        "home_ownership_MORTGAGE": 0, "home_ownership_NONE": 0, "home_ownership_OTHER": 0, "home_ownership_OWN": 0, "home_ownership_RENT": 1,
        "verification_status_Source Verified": 0, "verification_status_Verified": 1,
        "purpose_credit_card": 0, "purpose_debt_consolidation": 1, "purpose_educational": 0, "purpose_home_improvement": 0, "purpose_house": 0, "purpose_major_purchase": 0, "purpose_medical": 0, "purpose_moving": 0, "purpose_other": 0, "purpose_renewable_energy": 0, "purpose_small_business": 0, "purpose_vacation": 0, "purpose_wedding": 0
    }
    r = requests.post(url, json=data)
    if r.status_code == 200:
        return r.json()
    else:
        return {"error": r.text}

print("Low:", test_case(10000, 9, 85000, 10))
print("Medium:", test_case(20000, 16, 50000, 25))
print("High:", test_case(40000, 28, 20000, 42))
print("High2:", test_case(35000, 30, 15000, 45))
