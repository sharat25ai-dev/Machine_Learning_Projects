import pickle
import pandas as pd
import uvicorn
from typing import Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing_extensions import Annotated
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fitness-api")

class Customer(BaseModel):
    age: Annotated[float, Field(ge=1, le=100)]
    height_cm: Annotated[float, Field(ge=100, le=250)]
    weight_kg: Annotated[float, Field(ge=30, le=250)]
    heart_rate: Annotated[float, Field(ge=45, le=150)]
    blood_pressure: Annotated[float, Field(ge=75, le=250)]
    sleep_hours: Annotated[float | None, Field(ge=1, le=24)] = None
    nutrition_quality: Annotated[float, Field(ge=0, le=10)]
    activity_index: Annotated[float, Field(ge=1, le=5)]
    smokes: Literal[0, 1]
    is_male: Literal[0, 1]

class PredictResponse(BaseModel):
    fitness_probability: float
    is_fit: bool

# -------------------
# Initialize app
# -------------------
app = FastAPI(title="Fitness Prediction API")

# -------------------
# Load model
# -------------------
with open("model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)
logger.info("Model loaded successfully")

# -------------------
# Root endpoint
# -------------------
@app.get("/")
def read_root():
    return {"message": "Fitness Prediction API is running!"}

# -------------------
# Prediction logic
# -------------------
def predict_single(customer_dict):
    """Convert dict to DataFrame and return fitness probability"""
    df = pd.DataFrame([customer_dict])
    result = pipeline.predict_proba(df)[0, 1]
    return float(result)

# -------------------
# Prediction endpoint
# -------------------
@app.post("/predict", response_model=PredictResponse)
def predict(customer: Customer):
    customer_dict = customer.model_dump()
    logger.info(f"Received prediction request: {customer_dict}")

    prob = predict_single(customer_dict)
    is_fit = prob >= 0.5

    logger.info(f"Prediction result: probability={prob}, is_fit={is_fit}")
    return PredictResponse(
        fitness_probability=prob,
        is_fit=is_fit
    )

# -------------------
# Run server
# -------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
