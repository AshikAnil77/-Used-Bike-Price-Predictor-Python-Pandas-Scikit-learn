import streamlit as st
import joblib
import numpy as np
import pandas as pd

# --- 1. Load All 3 Files ---
model = joblib.load("bike_price_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

# --- 2. Streamlit UI (No Changes) ---
# (Using your hardcoded maps just to populate the dropdowns)
brand_map = {
    'Bajaj': 0, 'Hero': 1, 'Honda': 2, 'Suzuki': 3, 'TVS': 4, 'Yamaha': 5
}
city_map = {
    'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Kolkata': 3, 'Mumbai': 4
}
owner_map = {
    'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2
}
bike_map = {
    'Platina 100cc': 0, 'Splendor': 1, 'CB Shine': 2, 'FZ': 3, 'Apache': 4
}

st.title("🛵 Used Bike Price Predictor")

brand = st.selectbox("Select Brand", list(brand_map.keys()))
bike_name = st.selectbox("Select Bike Name", list(bike_map.keys()))  
city = st.selectbox("Select City", list(city_map.keys()))
owner = st.selectbox("Ownership", list(owner_map.keys()))
kms_driven = st.number_input("Kilometers Driven", min_value=0)
age = st.slider("Bike Age (Years)", 0, 30)
power = st.number_input("Power (BHP)", min_value=1.0, step=0.1)

if st.button("Predict Price"):
    
    # --- 3. Create Input Arrays ---
    # Create separate arrays for categorical and numerical data
    # IMPORTANT: The order MUST match the training script
    
    # Categorical data (as strings, in a 2D array)
    input_categorical = np.array([[brand, bike_name, city, owner]])
    
    # Numerical data (as numbers, in a 2D array)
    input_numerical = np.array([[kms_driven, age, power]])

    # --- 4. Process Inputs ---
    # 4a. Encode categorical data
    input_encoded = encoder.transform(input_categorical)
    
    # 4b. Scale numerical data
    input_scaled = scaler.transform(input_numerical)

    # --- 5. Combine Processed Features ---
    # Use np.hstack to join them horizontally
    # This creates the final 940-feature array
    input_final = np.hstack((input_encoded, input_scaled))

    # --- 6. Predict Price ---
    prediction = model.predict(input_final)
    st.success(f"💰 Estimated Resale Price: ₹{prediction[0]:,.2f}")