# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 19:09:10 2025

@author: Lenovo
"""

import numpy as np
import pickle
import streamlit as st

# --- 1. LOAD THE SAVED MODEL ---

# Use @st.cache_resource to load the model only once
@st.cache_resource
def load_model():
    """Loads the pickled model file."""
    # The 'model.pkl' file must be in the same folder as this 'app.py' file
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Error: 'model.pkl' file not found.")
        st.error("Please make sure the model file is in the same directory as this script.")
        return None
    except Exception as e:
        st.error(f"An error occurred loading the model: {e}")
        return None

# Load the model
loaded_model = load_model()

# --- 2. PREDICTION FUNCTION ---
def heart_prediction(input_data):
    """Predicts heart disease based on input data."""
    if loaded_model is None:
        return "Model not loaded. Cannot predict."
        
    try:
        # Convert all inputs to float for the model
        input_data_array = np.asarray(input_data, dtype=float)
        # Reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_array.reshape(1, -1)
        
        # Ensure the number of features matches the model
        if input_data_reshaped.shape[1] != 11:
            return f"Error: Expected 11 features, but got {input_data_reshaped.shape[1]}"
            
        prediction = loaded_model.predict(input_data_reshaped)
        
        if prediction[0] == 1:
            return "Patient has a high chance of Heart Disease"
        else:
            return "Patient has a low chance of Heart Disease"
    except ValueError:
        return "Error: Please ensure all inputs are valid numbers."
    except Exception as e:
        return f"An error occurred during prediction: {e}"

# --- 3. MAIN APP FUNCTION (UI) ---
def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="Heart Disease Predictor", layout="wide")
    st.title('❤️ Heart Disease Predictor Web App')
    st.write("Enter the patient's details below to predict the likelihood of heart disease.")

    if loaded_model is None:
        return # Stop the app if the model didn't load

    # --- Create Dictionaries for Categorical Mappings ---
    # !!! IMPORTANT !!!
    # You MUST verify these numbers match what you used for training
    # For example, if you mapped 'Male' to 1 and 'Female' to 0, change sex_map.
    
    sex_map = {'Male': 0, 'Female': 1}
    cp_map = {'Typical Angina (TA)': 2, 'Atypical Angina (ATA)': 0, 'Non-Anginal Pain (NAP)': 1, 'Asymptomatic (ASY)': -1}
    ecg_map = {'Normal': 0, 'ST-T Wave Abnormality (ST)': -1, 'Left Ventricular Hypertrophy (LVH)': 1}
    angina_map = {'No': 0, 'Yes': 1}
    slope_map = {'Flat': 0, 'Upsloping': 1, 'Downsloping': -1}
    fasting_bs_map = {'No (<= 120 mg/dl)': 0, 'Yes (> 120 mg/dl)': 1}
    
    # --- Create columns for a cleaner layout ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Personal Info")
        Age = st.number_input('Age', min_value=1, max_value=120, value=50, step=1)
        Sex_str = st.selectbox('Sex', options=sex_map.keys())
        FastingBS_str = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=fasting_bs_map.keys())

    with col2:
        st.subheader("Chest & Heart")
        ChestPainType_str = st.selectbox('Chest Pain Type', options=cp_map.keys())
        RestingBP = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=250, value=120, step=1)
        RestingECG_str = st.selectbox('Resting ECG Result', options=ecg_map.keys())

    with col3:
        st.subheader("Exercise & Vitals")
        Cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200, step=1)
        MaxHR = st.number_input('Max Heart Rate Achieved', min_value=50, max_value=250, value=150, step=1)
        ExerciseAngina_str = st.selectbox('Exercise-Induced Angina', options=angina_map.keys())
        Oldpeak = st.number_input('ST Depression (Oldpeak)', min_value=-5.0, max_value=10.0, value=1.0, step=0.1, format="%.1f")
        ST_Slope_str = st.selectbox('ST Slope', options=slope_map.keys())

    # --- 4. CONVERT USER INPUTS TO NUMERIC VALUES ---
    
    # Convert string inputs to their numeric values using the maps
    Sex = sex_map[Sex_str]
    ChestPainType = cp_map[ChestPainType_str]
    FastingBS = fasting_bs_map[FastingBS_str]
    RestingECG = ecg_map[RestingECG_str]
    ExerciseAngina = angina_map[ExerciseAngina_str]
    ST_Slope = slope_map[ST_Slope_str]
    
    # --- 5. PREPARE DATA AND PREDICT ---
    
    # Create the list of all inputs in the EXACT order your model expects
    # This order comes directly from your model.pkl file
    data = [
        Age,
        Sex,
        ChestPainType,
        RestingBP,
        Cholesterol,
        FastingBS,
        RestingECG,
        MaxHR,
        ExerciseAngina,
        Oldpeak,
        ST_Slope
    ]

    diagnosis = ""

    # Create a prominent button for prediction
    if st.button("Get Heart Test Result", type="primary", use_container_width=True):
        diagnosis = heart_prediction(data)
        
        # Display the result
        if "low chance" in diagnosis:
            st.success(diagnosis, icon="✅")
        elif "high chance" in diagnosis:
            st.warning(diagnosis, icon="⚠️")
        else:
            st.error(diagnosis, icon="❌") # Show any errors

# --- 6. RUN THE APP ---
if __name__ == '__main__':
    main()

