from fastapi import FastAPI
import joblib
from app.schema import InputData

app = FastAPI()

# Load trained model
model = joblib.load("model/trained_model.pkl")

@app.get("/")
def home():
    return {"message": "ML2API is running 🚀"}

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([[data.experience]])
    return {
        "experience": data.experience,
        "predicted_salary": float(prediction[0])
    }