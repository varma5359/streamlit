from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI(
    Title="House Price Prediction API",
    description="API to predict house prices based on various features",

)

class House(BaseModel):
    size_sqft: float 
    bedrooms: int
    bathrooms: int
    age_years: int
    distance_city_km: float
    floor: int

def load_model():
    try:
        model = joblib.load("house_model.pkl")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model loading failed: {str(e)}")
    return model

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API!"}    

@app.post("/predict/")
def predict_price(house: House):
    model = load_model()
    try:
        prediction = model.predict(
            [[
                house.size_sqft,
                house.bedrooms,
                house.bathrooms,
                house.age_years,
                house.distance_city_km,
                house.floor
            ]]
        )[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
    
    return {"predicted_price": prediction}



    
