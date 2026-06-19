import streamlit as st
import joblib

# Page settings
st.set_page_config(
    page_title="House Price Predictor",
    layout="wide"
)

# Load model
model = joblib.load("house_model.pkl")


# Size_sqft,Bedrooms,Bathrooms,Age_years,Distance_city_km,Floor,Price

# Title
st.title("🏠 House Price Prediction")

st.write("Enter house details below")

# Inputs
size_sqft = st.number_input("Size (in sqft):", min_value=100, max_value=10000, value=1000)
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms:", min_value=1, max_value=5, value=2)
age_years = st.number_input("Age of the House (years):", min_value=0, max_value=100, value=10)
distance_city_km = st.number_input("Distance from City Center (km):", min_value=0, max_value=50, value=5)
floor = st.number_input("Floor Number:", min_value=1, max_value=20, value=5)

# Predict button
if st.button("Predict Price"):

    prediction = model.predict(
        [[size_sqft, bedrooms, bathrooms, age_years, distance_city_km, floor]]
    )[0]

    st.success(
        f"Estimated Price: ₹ {prediction:,.0f}"
    )