import streamlit as st
import pandas as pd
import pickle

# Load scaler and model
scaler = pickle.load(open("models/scaler.pkl", "rb"))
model_gbc = pickle.load(open("models/model_gbc.pkl", "rb"))


# Prediction function
def predict_chronic_disease(age, bp, sg, al, hemo, sc, htn, dm, cad, appet, pc):

    data = {
        "age": [age],
        "bp": [bp],
        "sg": [sg],
        "al": [al],
        "hemo": [hemo],
        "sc": [sc],
        "htn": [htn],
        "dm": [dm],
        "cad": [cad],
        "appet": [appet],
        "pc": [pc]
    }

    df = pd.DataFrame(data)

    # Encode categorical columns
    df["htn"] = df["htn"].map({"yes": 1, "no": 0})
    df["dm"] = df["dm"].map({"yes": 1, "no": 0})
    df["cad"] = df["cad"].map({"yes": 1, "no": 0})
    df["appet"] = df["appet"].map({"good": 1, "poor": 0})
    df["pc"] = df["pc"].map({"normal": 1, "abnormal": 0})

    # Scale numerical columns
    numeric_cols = ["age", "bp", "sg", "al", "hemo", "sc"]
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Prediction
    prediction = model_gbc.predict(df)

    return prediction[0]


# ------------------ Streamlit UI ------------------

st.title("Chronic Kidney Disease Predictor")

st.write("Enter patient details below to predict CKD.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=48)
    bp = st.number_input("Blood Pressure", min_value=40, max_value=200, value=80)
    sg = st.number_input("Specific Gravity", min_value=1.005, max_value=1.050, value=1.020, step=0.001)
    al = st.number_input("Albumin", min_value=0.0, max_value=5.0, value=1.0)
    hemo = st.number_input("Hemoglobin", min_value=5.0, max_value=20.0, value=15.0)
    sc = st.number_input("Serum Creatinine", min_value=0.5, max_value=10.0, value=1.2)

with col2:
    htn = st.selectbox("Hypertension", ["yes", "no"])
    dm = st.selectbox("Diabetes", ["yes", "no"])
    cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
    appet = st.selectbox("Appetite", ["good", "poor"])
    pc = st.selectbox("Protein in Urine", ["normal", "abnormal"])


if st.button("Predict"):

    result = predict_chronic_disease(age, bp, sg, al, hemo, sc, htn, dm, cad, appet, pc)

    if result == 1:
        st.error("The patient is likely to have Chronic Kidney Disease (CKD).")
    else:
        st.success("The patient is unlikely to have Chronic Kidney Disease.")