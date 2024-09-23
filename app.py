import streamlit as st
import joblib
import pandas as pd



st.markdown("""
            
<style>
body{
    background-color:black;
    color:black;
            }
</style>
            """,
            unsafe_allow_html=True)

st.image('co2vehicle.JPEG')

# Simple username and password authentication
def authenticate(username, password):
    # Replace these with your desired credentials
    return username == "admin" and password == "password123"

# Input fields for authentication
st.title("CO2 Emissions Vehicle Prediction App")
st.write("Please log in to access the prediction app.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Authenticate the user
if authenticate(username, password):
    st.success("You have successfully logged in!")

    # Load the trained Ridge regression model
    model = joblib.load('best_ridge_model.pkl')

    # Streamlit app content after successful login
    st.write("Predict CO2 emissions based on vehicle specifications.")
    

    # Input fields for numeric features
    engine_size = st.number_input("Engine Size (L)", min_value=0.0, step=0.1, format="%.1f")
    cylinders = st.number_input("Cylinders", min_value=1, step=1)
    fuel_city = st.number_input("Fuel Consumption City (L/100km)", min_value=0.0, step=0.1, format="%.1f")
    fuel_hwy = st.number_input("Fuel Consumption Hwy (L/100km)", min_value=0.0, step=0.1, format="%.1f")
    fuel_comb = st.number_input("Fuel Consumption Comb (L/100km)", min_value=0.0, step=0.1, format="%.1f")
    fuel_comb_mpg = st.number_input("Fuel Consumption Comb (mpg)", min_value=0, step=1)

    # Input fields for boolean features (Fuel Types)
    fuel_type_e = st.checkbox("Fuel Type E")
    fuel_type_n = st.checkbox("Fuel Type N")
    fuel_type_x = st.checkbox("Fuel Type X")
    fuel_type_z = st.checkbox("Fuel Type Z")

    # Input fields for boolean features (Transmissions)
    transmission_options = {
        "Transmission A4": st.checkbox("Transmission A4"),
        "Transmission A5": st.checkbox("Transmission A5"),
        "Transmission A6": st.checkbox("Transmission A6"),
        "Transmission A7": st.checkbox("Transmission A7"),
        "Transmission A8": st.checkbox("Transmission A8"),
        "Transmission A9": st.checkbox("Transmission A9"),
        "Transmission AM5": st.checkbox("Transmission AM5"),
        "Transmission AM6": st.checkbox("Transmission AM6"),
        "Transmission AM7": st.checkbox("Transmission AM7"),
        "Transmission AM8": st.checkbox("Transmission AM8"),
        "Transmission AM9": st.checkbox("Transmission AM9"),
        "Transmission AS10": st.checkbox("Transmission AS10"),
        "Transmission AS4": st.checkbox("Transmission AS4"),
        "Transmission AS5": st.checkbox("Transmission AS5"),
        "Transmission AS6": st.checkbox("Transmission AS6"),
        "Transmission AS7": st.checkbox("Transmission AS7"),
        "Transmission AS8": st.checkbox("Transmission AS8"),
        "Transmission AS9": st.checkbox("Transmission AS9"),
        "Transmission AV": st.checkbox("Transmission AV"),
        "Transmission AV10": st.checkbox("Transmission AV10"),
        "Transmission AV6": st.checkbox("Transmission AV6"),
        "Transmission AV7": st.checkbox("Transmission AV7"),
        "Transmission AV8": st.checkbox("Transmission AV8"),
        "Transmission M5": st.checkbox("Transmission M5"),
        "Transmission M6": st.checkbox("Transmission M6"),
        "Transmission M7": st.checkbox("Transmission M7")
    }

    # Input fields for Make Types
    make_type_luxury = st.checkbox("Make Type Luxury")
    make_type_premium = st.checkbox("Make Type Premium")
    make_type_sports = st.checkbox("Make Type Sports")

    # Input fields for Vehicle Class Types
    vehicle_class_suv = st.checkbox("Vehicle Class SUV")
    vehicle_class_sedan = st.checkbox("Vehicle Class Sedan")
    vehicle_class_truck = st.checkbox("Vehicle Class Truck")

    # Compile input data into a DataFrame for prediction
    input_data = pd.DataFrame([[
        engine_size, cylinders, fuel_city, fuel_hwy, fuel_comb, fuel_comb_mpg,
        fuel_type_e, fuel_type_n, fuel_type_x, fuel_type_z,
        *transmission_options.values(),
        make_type_luxury, make_type_premium, make_type_sports,
        vehicle_class_suv, vehicle_class_sedan, vehicle_class_truck
    ]], columns=[
        'Engine_Size_L', 'Cylinders', 'Fuel_Consumption_City', 'Fuel_Consumption_Hwy',
        'Fuel_Consumption_Comb', 'Fuel_Consumption_Comb_mpg', 'Fuel Type_E', 'Fuel Type_N',
        'Fuel Type_X', 'Fuel Type_Z', 'Transmission_A4', 'Transmission_A5', 'Transmission_A6',
        'Transmission_A7', 'Transmission_A8', 'Transmission_A9', 'Transmission_AM5',
        'Transmission_AM6', 'Transmission_AM7', 'Transmission_AM8', 'Transmission_AM9',
        'Transmission_AS10', 'Transmission_AS4', 'Transmission_AS5', 'Transmission_AS6',
        'Transmission_AS7', 'Transmission_AS8', 'Transmission_AS9', 'Transmission_AV',
        'Transmission_AV10', 'Transmission_AV6', 'Transmission_AV7', 'Transmission_AV8',
        'Transmission_M5', 'Transmission_M6', 'Transmission_M7', 'Make_Type_Luxury',
        'Make_Type_Premium', 'Make_Type_Sports', 'Vehicle_Class_Type_SUV',
        'Vehicle_Class_Type_Sedan', 'Vehicle_Class_Type_Truck'
    ])

    # Predict CO2 emissions
    if st.button("Predict CO2 Emissions"):
        prediction = model.predict(input_data)
        st.write(f"Predicted CO2 Emissions: {prediction[0]:.2f} g/km")

    # Recommendation based on emissions
    if prediction > 108.1:
        st.warning("Recommendation: Your car emits over 108.1 g CO2/km. Consider replacing the car to reduce emissions.")
    else:
        st.success("Your car's emissions are within an acceptable range.")

else:
    st.error("Invalid credentials. Please try again.")
