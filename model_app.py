from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("ada.pkl")  

app = FastAPI()

# Define request body
class InsuranceInput(BaseModel):
    Gender: str
    Age: int
    Driving_License: int
    Previously_Insured: int
    Vehicle_Age: str
    Vehicle_Damage: str
    Annual_Premium: float
    Vintage: int

def preprocess(data: InsuranceInput):
    # Convert categorical features to numerical (Example Encoding)
    gender_mapping = {"Male": 0, "Female": 1}
    vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
    vehicle_damage_mapping = {"Yes": 1, "No": 0}

    return np.array([
        gender_mapping[data.Gender],
        data.Age,
        data.Driving_License,
        data.Previously_Insured,
        vehicle_age_mapping[data.Vehicle_Age],
        vehicle_damage_mapping[data.Vehicle_Damage],
        data.Annual_Premium,
        data.Vintage
    ]).reshape(1, -1)

@app.post("/predict")
def predict(input_data: InsuranceInput):
    processed_data = preprocess(input_data)
    prediction = model.predict(processed_data)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  