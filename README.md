# 🌾 Indian Crop Prediction – Flask App

🚀 **Indian Crop Prediction Web App** built with Flask and Machine Learning.  
This project uses a **Random Forest Classifier** to recommend the most suitable crop for given inputs such as soil nutrients (NPK), weather conditions, pH level, rainfall, and crop price.  

---

## ✨ Features
- 🤖 **Machine Learning Model:** Trained on Indian crop dataset  
- 🎨 **Beautiful UI:** Glassmorphic, responsive form for easy inputs  
- 🌍 **State-based Predictions:** Considers state-specific factors  
- ⚡ **Fast & Lightweight:** Flask backend with joblib for model loading  
- 🚀 **Deployment Ready:** Compatible with GitHub, Render, Railway hosting  

---

## 🛠️ Tech Stack
- **Python** (Flask, scikit-learn, joblib, numpy, pandas)  
- **Frontend:** HTML, CSS (Glassmorphic design)  
- **Machine Learning:** Random Forest Classifier  
- **Dataset:** Indian Crop Dataset (`indiancrop_dataset.xlsx`)  

---

## 📂 Project Structure

```
Crop Prediction Flask App/
│── app.py
│── requirements.txt
│── crop_prediction_model.pkl
│── scaler.pkl
│── state_encoder.pkl
│── crop_encoder.pkl
│── indiancrop_dataset.xlsx
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Prethyenkha/Crop-Prediction-Flask-App.git
cd Crop-Prediction-Flask-App
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate   # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python app.py
```

### 5️⃣ Open in browser
```
http://127.0.0.1:5000
```

## 🧠 Machine Learning Model
- Algorithm: **Random Forest Classifier**  
- Features: N, P, K, Temperature, Humidity, pH, Rainfall, State, Crop Price  
- Target: Crop type  
- Encoders: `LabelEncoder` for states and crops  
- Scaling: StandardScaler  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License
This project is open-source and available under the **MIT License**.
