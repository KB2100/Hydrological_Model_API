from fastapi import FastAPI
import joblib
import numpy as np

# Load the trained model
model = joblib.load("hydrological_model.pkl")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hydrological Model API is running!"}

@app.post("/predict/")
def predict(features: list):
    # Convert input data to numpy array
    features_array = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features_array)
    
    return {"prediction": prediction.tolist()}
