"""
Program to use and test the model of MLP_RELU_model_v1.h5 using keras
"""

import numpy as np
import joblib

# File path user input
print("Enter File Path of Model (Ex: /User/.../model_v1.pkl): ")
fp = input()

# Load the model
model = joblib.load(fp)


# User data capture array
vals = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

# Output Array
types =['the Reserve Balance', 'the 10-Year Treasury Rate',
        'the Treasury General Account Balance', 'the Bank Credit',
        'the Federal Reserve Coin Value', 'the Reverse Repurchase Agreements']

# User data entry
for i in range(6):
    print("\nPlease enter the weekly percentage change of ",
          types[i], " (as of wednesday)...")
    vals[0][i] = float(input())

# Prediction
pred = model.predict_classes(vals)[0]

# Output prediction
if pred == 1: print("Model predicts S&P500 will go up in 2 weeks!")
if pred == 2: print("Model predicts S&P500 will go down in 2 weeks!")
if pred == 0: print("Model predicts S&P500 will have changed minimally "
                    "in 2 weeks")



