import streamlit as st
import joblib
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set up the app's visual appearance
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Display an image at the top of the app
st.image('co2vehicle.JPEG',width= 400)

# Simple username and password authentication
def authenticate(username, password):
    return username == "admin" and password == "password123"

# Input fields for authentication
st.title("Predict  and Tracker CO2 Emissions from Vehicles ")
st.write("Please log in to access the prediction app.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Authenticate the user
if authenticate(username, password):
    st.success("You have successfully logged in!")

    # Load the trained model
    model = joblib.load('best_xgb_model.pkl')

    # Streamlit app content after successful login
    st.write("Predict CO2 emissions based on vehicle specifications.")
    st.image('climate action.png', width=400)
    # CSV file upload for batch processing
    uploaded_file = st.file_uploader("Upload CSV with vehicle specifications and geospatial data", type="csv")
    
    if uploaded_file:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Ensure the CSV contains all required columns
        required_columns = [
            'Engine_Size_L', 'Cylinders', 'Fuel_Consumption_City', 'Fuel_Consumption_Hwy',
            'Fuel_Consumption_Comb', 'Fuel_Consumption_Comb_mpg', 'Fuel Type_E', 'Fuel Type_N', 
            'Fuel Type_X', 'Fuel Type_Z', 'Make_Type_Luxury', 'Make_Type_Premium', 'Make_Type_Sports', 
            'Vehicle_Class_Type_SUV', 'Vehicle_Class_Type_Sedan', 'Vehicle_Class_Type_Truck', 
            'Latitude', 'Longitude'
        ]
        
        # Check for missing required columns
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"The uploaded CSV is missing the following required columns: {', '.join(missing_columns)}")
        else:
            # Predict CO2 emissions for the uploaded data
            df['Predicted_CO2_Emissions'] = model.predict(df[required_columns[:-2]])

            # Display the data with predictions
            st.write(df[['Engine_Size_L', 'Cylinders', 'Fuel_Consumption_City', 'Predicted_CO2_Emissions']].head())

            # Filter data where emissions exceed 108.1 g/km
            high_emission_vehicles = df[df['Predicted_CO2_Emissions'] > 108.1]

            if not high_emission_vehicles.empty:
                st.warning(f"There are {len(high_emission_vehicles)} vehicles exceeding 108.1 g CO2/km. Please replace the Car ")

                # Create a map with Folium centered around the average latitude and longitude
                map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
                map = folium.Map(location=map_center, zoom_start=5)

                # Add markers for high emission vehicles
                for _, row in high_emission_vehicles.iterrows():
                    folium.Marker(
                        location=[row['Latitude'], row['Longitude']],
                        popup=f"CO2: {row['Predicted_CO2_Emissions']:.2f} g/km\nEngine Size: {row['Engine_Size_L']}L",
                        icon=folium.Icon(color="red")
                    ).add_to(map)

                # Display the map in Streamlit
                st_folium(map, width=2000, height=700)

                # Allow users to download the high emission vehicles data
                csv = high_emission_vehicles.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download High Emission Vehicles Data",
                    data=csv,
                    file_name='high_emission_vehicles.csv',
                    mime='text/csv'
                )
            else:
                st.success("All vehicles have emissions within an acceptable range.")
                
else:
    st.error("Invalid credentials. Please try again.")
