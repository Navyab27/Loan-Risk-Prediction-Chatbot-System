# Loan Risk Prediction Chatbot System

An intelligent loan risk assessment application that predicts borrower default probability using machine learning. It provides an API backend for making predictions and a Streamlit chatbot frontend to interactively analyze borrower risk profiles. 

## Features

- **Risk Categorization**: Evaluates borrower profiles and categorizes them as Low, Medium, or High Risk, simulating real-world credit risk assessment.
- **Explainability**: Identifies the top risk factors driving the prediction using SHAP values (SHapley Additive exPlanations).
- **Fraud Detection**: Flags potential fraudulent applications using rule-based logic (e.g., extremely high loan amounts requested by those with very low annual income).
- **Interactive Chatbot UI**: A user-friendly Streamlit interface that accepts borrower details and returns the analysis. Includes pre-set demo options for quick testing.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Machine Learning API)
- **Frontend**: [Streamlit](https://streamlit.io/) (Interactive web UI)
- **Machine Learning**: Scikit-Learn, SHAP, Pandas, Joblib

## Project Structure

- `app/api.py`: FastAPI server handling prediction requests and SHAP logic.
- `chatbot_app.py`: Streamlit frontend capturing user input and displaying risk assessment.
- `model/`: Serialized ML models (`loan_risk_model.pkl`), feature lists (`features.pkl`), and data scaler (`scaler.pkl`).
- `eda.ipynb` & `data_cleaning.ipynb`: Jupyter notebooks used for data exploration and preprocessing.
- `model_training.ipynb`: Jupyter notebook detailing the model training pipeline.

## Getting Started

### Prerequisites

You need Python 3.8+ installed. It is recommended to use a virtual environment.

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Navyab27/Loan-Risk-Prediction-Chatbot-System.git
   cd Loan-Risk-Prediction-Chatbot-System
   ```
2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn streamlit scikit-learn pandas shap joblib requests
   ```

### Running the Application

This project requires simultaneous execution of the backend API and the frontend application.

**1. Start the Backend API (FastAPI):**
In a terminal, run the following command to start the FastAPI server:
```bash
uvicorn app.api:app --reload
```
The API will be available at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

**2. Start the Frontend App (Streamlit):**
Open a new terminal window/tab and run:
```bash
streamlit run chatbot_app.py
```
This will launch the chatbot UI in your browser (typically at `http://localhost:8501`). Enter the borrower metrics and click "Evaluate Loan Risk" to receive instantaneous feedback!
