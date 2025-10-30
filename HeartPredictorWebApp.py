# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 19:13:26 2025

@author: Lenovo
"""

import numpy as np 
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:\Users\Lenovo\Desktop\ML_task03\Heart_Disease_Prediction_Model\Trained_model.sav','rb'))

#creating function for prediction
def heart_prediction(input_data):
    input_data_array=np.asarray(input_data)
    input_data_reshaped=input_data_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    #print(prediction)
    if prediction[0]==1: 
        return "\nill heart"
    else:
        return "\nHealthy heart"


def main():

    st.title('Heart Disease Predictor Web App')

    Age=st.text_input('Enter your age: ')
    ChestPainType=st.text_input('Enter your chest pain type: ')
    Sex=st.text_input('Enter your gender: ')
    RestingBP=st.text_input('Enter your restingBP: ')
    Cholesterol=st.text_input('Enter your cholesterol: ')
    FastingBS=st.text_input('Enter your fasting BS: ')
    RestingECG=st.text_input('Enter your resting ECG: ')
    MaxHR=st.text_input('Enter your max Heart-rate: ')
    ExerciseAngina=st.text_input('Enter your exercise angina: ')
    Oldpeak=st.text_input('Enter your old-peak value: ')
    ST_Slope=st.text_input('What is your ST slope: ')

    data=[Age,ChestPainType,Sex,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]
    for i in range(11): 
        if data[i]=='M':
            data[i]=0
        if data[i]=='F':
            data[i]=1
        if data[i]=='ATA': 
            data[i]=0
        if data[i]=='NAP': 
            data[i]=1
        if data[i]=='TA': 
            data[i]=2
        if data[i]=='ASY': 
            data[i]=-1 
        if data[i]=='Normal': 
            data[i]=0
        if data[i]=='LVH': 
            data[i]=1 
        if data[i]=='ST': 
            data[i]=-1 
        if data[i]=='N': 
            data[i]=0
        if data[i]=='Y': 
            data[i]=1
        if data[i]=='Flat': 
            data[i]=0
        if data[i]=='Up': 
            data[i]=1 
        if data[i]=='Down': 
            data[i]=-1

    
    diagnosis=""

    #creating button for prediction via the above function

    if st.button("Heart Test Result"):
        diagnosis=heart_prediction(data)
    st.success(diagnosis)

    if __name__=='__main__':
        main()