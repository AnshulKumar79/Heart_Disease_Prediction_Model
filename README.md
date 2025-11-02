# Heart_Disease_Prediction_Model
Trained a machine-learning model with Logistic Regression(classification based) whether a person is a heart patient or not.

Heart Disease Prediction using Logistic Regression

This project aims to build a Machine Learning model that predicts whether a person is a heart patient or not based on various medical attributes. The model uses Logistic Regression, a simple yet powerful classification algorithm ideal for binary outcomes.
## 🚀 Live Demo

You can try the live app here: https://heartdiseasepredictionmodel-8j685glydzooqusvwltiqb.streamlit.app/

Project Overview

Heart disease is one of the leading causes of death globally. Early prediction and detection can help in timely treatment and prevention.
This project utilizes patient data (such as age, cholesterol level, blood pressure, etc.) to classify individuals as:

1 → Heart patient

0 → Not a heart patient

Workflow

Data Collection & Loading

Dataset imported using pandas (CSV format)

Exploratory Data Analysis (EDA)

Visualized feature distributions and correlations using matplotlib and seaborn.

Data Preprocessing

Encoded categorical features

Split data into training and testing sets

Model Training

Applied Logistic Regression from sklearn.linear_model.

Trained the model on the processed training data.

Model Evaluation

Evaluated performance using:

Accuracy

Precision, Recall, F1-score

Confusion Matrix

Prediction

The trained model predicts whether a new input corresponds to a heart patient (1) or not (0).

Technologies Used
Category	Tools / Libraries
Language	Python
Data Handling	pandas, numpy
Visualization	matplotlib, seaborn
Model Building	scikit-learn
Environment	Jupyter Notebook
Results

Model: Logistic Regression

Accuracy Score: ~ 0.8646864686468647

F1 Score: 0.86

The model shows good performance in distinguishing heart patients from non-patients.
