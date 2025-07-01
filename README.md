# Car_Price_Prediction
This project is a machine learning solution for classifying the price range of used cars based on key parameters. The model takes into account various features that influence a car's value and predicts its price category.

## This task is based on a Kaggle competition dataset. All data was preprocessed and cleaned before training.

## Features:
- model
- year
- motor_type
- running
- wheel
- color
- type
- status
- motor_volume

## ⚙️ How It Works
- The user sends car details.
- The input is preprocessed and transformed into numerical features using saved encoders.
- Trained neural network model analyzes these features and predicts the most likely price.

## 🛠️ Setup Guide

## 1. Clone the repository
Open your environment and clone the repository
```bash
https://github.com/SammSM/Car_Price_Prediction.git
```
## 2. Change to Car_Price_Prediction directory
```bash
cd Car_Price_Prediction
```

## 4. Create a virtual environment and activate it

- ### Create a virtual environment
On Windows:
```bash
python -m venv venv
```
On macOS / Linux:
```bash
python3 -m venv venv
```
- ### Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```
On macOS / Linux:
```bash
source venv/bin/activate
```

## 5. Install PIP package manager for Python
```bash
py -m pip install --upgrade pip
```
### Or
```bash
python -m pip install --upgrade pip
```

## 6. Install requirements
```bash
pip install -r requirements.txt
```
