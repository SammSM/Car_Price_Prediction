import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

import pickle

with open('model_files/model2.pkl', 'rb') as file:
    model = pickle.load(file)

label_encoders = {}
for col in ['model', 'motor_type', 'color', 'type', 'status']:
    label_encoders[col] = joblib.load(f"model_files/label_{col}.pkl")

scaler = joblib.load("model_files/scaler.pkl")

def predict_price(input_list):
    df = pd.DataFrame([input_list], columns=['model', 'year', 'motor_type', 'running', 'wheel', 'color', 'type', 'status', 'motor_volume'])
    
    df = df.drop('wheel', axis=1)
    df['running'] = df['running'].apply(lambda p: float(p.split(' ')[0]) if p.split(' ')[-1] == 'km' else 1.6 * float(p.split(' ')[0]))
    
    for col in ['model', 'motor_type', 'color', 'type', 'status']:
        df[col] = label_encoders[col].transform(df[col])

    df_scaled = scaler.transform(df)
    df_scaled = df_scaled.reshape(1, 1, 8)

    return df_scaled
