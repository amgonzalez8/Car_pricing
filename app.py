import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Car Pricing Prediction")
st.write("This web app will help you to predict the selling price for your car. Please enter the values ​​to continue:")

model = pickle.load(open('model_car.pkl', 'rb'))
feature_columns = pickle.load(open('feature_columns.pkl', 'rb'))

year = st.number_input('Year of Manufacture', min_value=1990, max_value=2024, step=1)
km_driven = st.number_input('Kilometers Driven')
fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual', 'Trustmark Dealer'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owners = st.selectbox('Number of Owners', [
    "First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"
])


user_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],  # Se ajusta al nombre correcto
    'fuel_Diesel': [1 if fuel_type == 'Diesel' else 0],
    'fuel_Petrol': [1 if fuel_type == 'Petrol' else 0],
    'fuel_CNG': [1 if fuel_type == 'CNG' else 0],
    'fuel_LPG': [1 if fuel_type == 'LPG' else 0],
    'fuel_Electric': [1 if fuel_type == 'Electric' else 0],
    'seller_type_Individual': [1 if seller_type == 'Individual' else 0],
    'seller_type_Trustmark Dealer': [1 if seller_type == 'Trustmark Dealer' else 0],
    'transmission_Manual': [1 if transmission == 'Manual' else 0],
    'owner_First Owner': [1 if owners == "First Owner" else 0],
    'owner_Second Owner': [1 if owners == "Second Owner" else 0],
    'owner_Third Owner': [1 if owners == "Third Owner" else 0],
    'owner_Fourth & Above Owner': [1 if owners == "Fourth & Above Owner" else 0],
    'owner_Test Drive Car': [1 if owners == "Test Drive Car" else 0]
})


for col in feature_columns:
    if col not in user_data.columns:
        user_data[col] = 0 

user_data = user_data[feature_columns]

prediction = model.predict(user_data)

if st.button('Predict'):
    st.write(f'The predicted selling price of the car is ${prediction[0]:,.2f}')