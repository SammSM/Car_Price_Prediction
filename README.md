# 🚗 Car Price Prediction Telegram Bot

This project is a Telegram bot that predicts car prices based on a trained machine learning model. Users provide car specifications through a chat interface, and the bot returns an estimated price.

---

## 🤖 Features

- Predicts car prices using a trained neural network
- Accepts natural text input with car details
- Handles preprocessing (label encoding, scaling) dynamically

---

## 🧠 How the ML Model Works

The model is trained on real car listing data with features like:

- `model`, `year`, `motor_type`, `running`, `color`, `type`, `status`, `motor_volume`

It includes:

- Preprocessing with `LabelEncoder` and `StandardScaler`
- Keras-based neural network saved as `.pkl` (via `pickle`)
- Inference-ready pipeline used in real-time inside the bot

---

## 🧾 Example Input Format

After starting the bot with `/start`, send a message like this:
mercedes-benz, 2018, petrol, 45000 km, left, black, sedan, excellent, 2.0
![Alt Text](car_price.jpg)
