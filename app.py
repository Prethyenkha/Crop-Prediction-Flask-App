from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load("crop_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")
le_crop = joblib.load("crop_encoder.pkl")
le_state = joblib.load("state_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    
    if request.method == "POST":
        # Get form data
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])
        state_name = request.form["state"]
        crop_price = float(request.form["crop_price"])
        
        # Encode state
        state_encoded = le_state.transform([state_name])[0]
        
        # Prepare features
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall, state_encoded, crop_price]])
        features_scaled = scaler.transform(features)
        
        # Predict
        crop_encoded = model.predict(features_scaled)[0]
        prediction = le_crop.inverse_transform([crop_encoded])[0]
    
    states = le_state.classes_  # List of states for dropdown
    return render_template("index.html", prediction=prediction, states=states)

if __name__ == "__main__":
    app.run(debug=True)
