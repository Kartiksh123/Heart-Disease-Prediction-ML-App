import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and expected columns
model = joblib.load("models/knn_heart_model.pkl")
scaler = joblib.load("models/heart_scaler.pkl")
expected_columns = joblib.load("models/heart_columns.pkl")

st.title("Heart Stroke Prediction by Kartik")
st.markdown("This application helps you estimate your risk of heart disease based on common health metrics.")
st.info("Please provide your health details below. If you are unsure about a term, hover over the info icon (ⓘ) or read the description provided. **This tool is for informational purposes only and is not a substitute for professional medical advice.**")
# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain_type_options = {
        "Atypical Angina": "Chest pain not related to the heart.\n",
        "Non-Anginal Pain": "Typically not a heart-related pain.\n",
        "Typical Angina": "Classic heart-related chest pain.\n",
        "Asymptomatic": "No chest pain at all."
    }
chest_pain = st.selectbox(
        "Chest Pain Type",
        list(chest_pain_type_options.keys()),
        help="Select the type of chest pain you experience. ⓘ " + ", ".join([f"{k}: {v}" for k, v in chest_pain_type_options.items()])
    )
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
st.markdown("#### Fasting Blood Sugar")
st.info("A value greater than 120 mg/dL is often an indicator of diabetes, a risk factor for heart disease.")
fasting_bs = st.radio("Is your Fasting Blood Sugar > 120 mg/dL?", options=["Yes", "No"], index=1)
fasting_bs = 1 if fasting_bs == "Yes" else 0 
resting_ecg_options = {
        "Normal": "Normal heart rhythm.\n",
        "ST-T Wave Abnormality": "Minor changes in the heart's electrical activity.\n",
        "Left Ventricular Hypertrophy": "Enlargement of the heart's left ventricle."
    }
resting_ecg = st.selectbox(
        "Resting ECG",
        list(resting_ecg_options.keys()),
        help="Select your resting ECG result. ⓘ " + ", ".join([f"{k}: {v}" for k, v in resting_ecg_options.items()])
    )

max_hr = st.slider("Maximum Heart Rate (beats/min)", 60, 220, 150)
    
exercise_angina = st.radio("Do you experience exercise-induced angina?", ["Yes", "No"], help="Angina is chest pain. This refers to pain triggered by physical activity. ⓘ")
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0, help="ST depression is a key finding on ECG during a stress test.")
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"], help="The slope of the ST segment of the ECG during peak exercise. ⓘ")

# When Predict is clicked
if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
