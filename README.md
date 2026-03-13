# kidney_disease_project
This project is a Machine Learning web application built with Streamlit that predicts whether a patient is likely to have Chronic Kidney Disease (CKD) based on clinical parameters.

🩺 Chronic Kidney Disease Predictor

A Machine Learning web application that predicts whether a patient is likely to have Chronic Kidney Disease (CKD) based on medical parameters. The app provides an interactive interface where users can input patient details and receive an instant prediction.

The application is built using Streamlit for the web interface and scikit-learn for machine learning model development.

🚀 Features

Predicts Chronic Kidney Disease (CKD) using patient health data

Interactive web interface built with Streamlit

Real-time prediction with trained ML model

Data preprocessing including encoding and feature scaling

Easy to deploy and run locally

📊 Input Parameters

The model uses the following medical features:

Age

Blood Pressure (BP)

Specific Gravity (SG)

Albumin (AL)

Hemoglobin (Hemo)

Serum Creatinine (SC)

Hypertension

Diabetes Mellitus

Coronary Artery Disease

Appetite

Protein in Urine

🧠 Machine Learning Workflow

Data Cleaning and Preprocessing

Handling Missing Values

Encoding Categorical Variables

Feature Scaling using MinMaxScaler

Model Training using Gradient Boosting Classifier

Model Serialization using Pickle

Deployment using Streamlit

🛠 Technologies Used

Python

Streamlit

scikit-learn

Pandas

NumPy

Pickle

📂 Project Structure
kidney_disease_predictor
│
├── app.py
├── models
│   ├── scaler.pkl
│   └── model_gbc.pkl
│
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/viveksikarwar13489-design/kidney-disease-predictor.git

Navigate to the project folder:

cd kidney-disease-predictor

Install required libraries:

pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit app:

streamlit run app.py

Then open your browser at:

http://localhost:8501
📈 Model Output

CKD Detected → Patient is likely to have Chronic Kidney Disease

No CKD Detected → Patient is unlikely to have Chronic Kidney Disease
