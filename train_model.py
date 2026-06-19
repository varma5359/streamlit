import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv(r"C:\Users\ravik\OneDrive\Desktop\House_price.csv")
X = df[
    [
        "Size_sqft",
        "Bedrooms",
        "Bathrooms",
        "Age_years",
        "Distance_city_km",
        "Floor"
    ]
]

y = df["Price"]
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_model.pkl")

print("Model saved!")