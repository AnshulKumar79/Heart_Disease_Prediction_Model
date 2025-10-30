# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model=pickle.load(open('C:/Users/Lenovo/Documents/saved_models/Trained_model.sav','rb'))
input_data=eval(input("\nEnter the details of the person in list: "))
for i in range(11): 
    if input_data[i]=='M':
        input_data[i]=0
    if input_data[i]=='F':
        input_data[i]=1
    if input_data[i]=='ATA': 
        input_data[i]=0
    if input_data[i]=='NAP': 
        input_data[i]=1
    if input_data[i]=='TA': 
        input_data[i]=2
    if input_data[i]=='ASY': 
        input_data[i]=-1 
    if input_data[i]=='Normal': 
        input_data[i]=0
    if input_data[i]=='LVH': 
        input_data[i]=1 
    if input_data[i]=='ST': 
        input_data[i]=-1 
    if input_data[i]=='N': 
        input_data[i]=0
    if input_data[i]=='Y': 
        input_data[i]=1
    if input_data[i]=='Flat': 
        input_data[i]=0
    if input_data[i]=='Up': 
        input_data[i]=1 
    if input_data[i]=='Down': 
        input_data[i]=-1

input_data_array=np.asarray(input_data)
input_data_reshaped=input_data_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction[0]==1: 
    print("\nill heart")
else:
    print("\nHealthy heart")