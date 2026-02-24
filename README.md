# 🌊 Flood Risk Prediction Web App

A web-based flood risk prediction system built using **Flask** and **Machine Learning (Random Forest)**.  
This application predicts flood risk levels (**AMAN, WASPADA, BAHAYA**) based on environmental parameters.

---

## 🚀 Features

- 🔍 Flood risk prediction using Machine Learning
- 🌧️ Input environmental parameters via web form
- 📊 Classification into 3 risk levels
- 🌐 Deployed on PythonAnywhere
- 📦 Model trained with scikit-learn (RandomForestClassifier)

---

## 🧠 Model Information

- Algorithm: **Random Forest Classifier**
- Output Classes:
  - `0` → AMAN
  - `1` → WASPADA
  - `2` → BAHAYA
- Trained using synthetic environmental data

---

## 🧾 Input Parameters

| Parameter    | Description            |
| ------------ | ---------------------- |
| curah_hujan  | Rainfall intensity     |
| jarak_sungai | Distance to river      |
| ketinggian   | Elevation level        |
| drainase     | Drainage quality (0–1) |
| kepadatan    | Area density (0–1)     |

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn
- **Numerical Computing**: NumPy
- **Model Serialization**: joblib
- **Deployment**: PythonAnywhere

---

## 📁 Project Structure
# SIBAN-Sibanjir-AI
