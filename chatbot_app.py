import streamlit as st
import requests

st.set_page_config(page_title="Loan Risk Chatbot", layout="wide")

API_URL = "http://127.0.0.1:8000/predict"

st.title("Loan Risk Assistant")
st.write("This chatbot evaluates the risk of loan applicants using a machine learning model.")

st.chat_message("assistant").write(
    "Hello! I can analyze whether a borrower is Low, Medium, or High Risk."
)

st.subheader("Enter Borrower Details")

# Initialize session state for demo values to fix Streamlit rerun issues
if "loan_amnt" not in st.session_state:
    st.session_state["loan_amnt"] = 15000
    st.session_state["int_rate"] = 13.5
    st.session_state["annual_inc"] = 60000
    st.session_state["dti"] = 18.0
    st.session_state["eval_trigger"] = False

def set_demo(risk_type):
    if risk_type == "low":
        st.session_state["loan_amnt"] = 10000
        st.session_state["int_rate"] = 9.0
        st.session_state["annual_inc"] = 85000
        st.session_state["dti"] = 10.0
    elif risk_type == "medium":
        st.session_state["loan_amnt"] = 20000
        st.session_state["int_rate"] = 16.0
        st.session_state["annual_inc"] = 50000
        st.session_state["dti"] = 25.0
    elif risk_type == "high":
        st.session_state["loan_amnt"] = 40000
        st.session_state["int_rate"] = 28.0
        st.session_state["annual_inc"] = 20000
        st.session_state["dti"] = 42.0
    st.session_state["eval_trigger"] = True

col1, col2 = st.columns(2)

with col1:
    loan_amnt = st.number_input("Loan Amount", key="loan_amnt")
    term = st.selectbox("Loan Term", [36, 60])
    int_rate = st.number_input("Interest Rate (%)", key="int_rate")

with col2:
    annual_inc = st.number_input("Annual Income", key="annual_inc")
    dti = st.number_input("Debt-to-Income Ratio", key="dti")

st.divider()

st.subheader("Quick Demo Scenarios (For Placement Demo)")

colA, colB, colC = st.columns(3)

colA.button("Low Risk Example", on_click=set_demo, args=("low",))
colB.button("Medium Risk Example", on_click=set_demo, args=("medium",))
colC.button("High Risk Example", on_click=set_demo, args=("high",))

eval_clicked = st.button("Evaluate Loan Risk")

if eval_clicked or st.session_state.get("eval_trigger", False):
    st.session_state["eval_trigger"] = False
    data = {
        "loan_amnt": loan_amnt,
        "term": term,
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

        "grade_B": 0,
        "grade_C": 0,
        "grade_D": 1,
        "grade_E": 0,
        "grade_F": 0,
        "grade_G": 0,

        "home_ownership_MORTGAGE": 0,
        "home_ownership_NONE": 0,
        "home_ownership_OTHER": 0,
        "home_ownership_OWN": 0,
        "home_ownership_RENT": 1,

        "verification_status_Source Verified": 0,
        "verification_status_Verified": 1,

        "purpose_credit_card": 0,
        "purpose_debt_consolidation": 1,
        "purpose_educational": 0,
        "purpose_home_improvement": 0,
        "purpose_house": 0,
        "purpose_major_purchase": 0,
        "purpose_medical": 0,
        "purpose_moving": 0,
        "purpose_other": 0,
        "purpose_renewable_energy": 0,
        "purpose_small_business": 0,
        "purpose_vacation": 0,
        "purpose_wedding": 0
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()

        st.chat_message("assistant").write("Analysis complete.")

        if result["risk_level"] == "High Risk":
            st.error(f"Risk Level: {result['risk_level']}")
        elif result["risk_level"] == "Medium Risk":
            st.warning(f"Risk Level: {result['risk_level']}")
        else:
            st.success(f"Risk Level: {result['risk_level']}")

        st.metric("Risk Score", result["risk_score"])
        st.metric("Default Probability", result["default_probability"])

    else:
        st.error("API connection failed.")