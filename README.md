# 🚗 Car Price Prediction Telegram Bot

This project is a Telegram bot that predicts car prices based on a trained machine learning model. Users provide car specifications through a chat interface, and the bot returns an estimated price.

---

## 🤖 Features

- Predicts car prices using a trained neural network
- Accepts natural text input with car details
- Handles preprocessing (label encoding, scaling) dynamically

---

🧠 ML Model Logic
The car price prediction model is trained on real-world car listing data. It uses the following features:

model, year, motor_type, running, color, type, status, motor_volume

Workflow:
1. Preprocessing:

- Categorical features are encoded using LabelEncoder
- The encoders for each feature are saved as .pkl files (e.g., label_model.pkl, label_color.pkl) in the model_files/ directory
- Mileage values like "km" or "miles" are converted to a numeric format (with miles converted to kilometers using a coefficient)
- Features are scaled using StandardScaler, which is also saved as scaler.pkl

2. Model Architecture:

- A deep neural network built with Keras
- The output layer uses a linear activation function to perform regression

3. Deployment:

- The trained model is stored as model2.pkl using pickle
- Encoders and scaler are loaded at runtime to ensure input data matches the training format
- The Telegram bot feeds user input through the same preprocessing pipeline before making a prediction

---

## 🧾 Example Input Format

After starting the bot with `/start`, send a message like this:
mercedes-benz, 2018, petrol, 45000 km, left, black, sedan, excellent, 2.0

![Alt Text](car_price.JPG)
