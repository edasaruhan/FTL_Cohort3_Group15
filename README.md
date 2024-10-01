# CO2 Emissions Vehicle Prediction App 🌍🚗💨

![Climate Action](climate action.png)

This is a web application that predicts vehicle CO2 emissions based on various vehicle specifications using an **XGBoost regressor** model. The app is built using **Streamlit** and allows users to input vehicle details to receive CO2 emission predictions.

## Features 🌟
- **Predict CO2 Emissions**: Get emissions predictions for vehicles based on specifications like engine size, cylinders, and fuel consumption.
- **High Emission Tracking**: Visualize locations of vehicles with high emissions on an interactive map using Folium.
- **Basic Login Authentication**: Secure access to the app's functionality.
- **Real-time Predictions**: Input your vehicle specs and get immediate CO2 emissions predictions.
- **User-Friendly Interface**: Built with Streamlit for a clean and intuitive user experience.

## Frameworks and Libraries Used 🛠️
- **Streamlit**: For building the web app.
- **XGBoost**: For machine learning predictions (XGBoost regressor).
- **pandas**: For data manipulation and handling.
- **joblib**: For model loading and serialization.
- **Folium**: For creating interactive maps to track high emission vehicles.

## Installation 🖥️

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/app.git
    cd app
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and navigate to the displayed local URL (usually `http://localhost:8501`).

## Authentication 🔐

This app requires login credentials to access the CO2 emissions prediction tool.

### Login Credentials:
- **Username**: `admin`
- **Password**: `password123`

Upon logging in with these credentials, you can access the prediction functionality.

## Usage 🚀

1. After logging in, input the vehicle specifications in the fields provided.
2. Press the **Predict CO2 Emissions** button.
3. The app will display the predicted CO2 emissions in grams per kilometer (g/km).
4. If your vehicle's emissions exceed 108.1 g/km, the app will recommend considering a replacement to reduce emissions.
5. Vehicles with high emissions will be displayed on an interactive map, indicating their locations.

## File Structure 📁

├── app.py # The main app file ├── best_xgb_model.pkl # Pre-trained XGBoost regressor model ├── co2vehicle.JPEG # Image displayed in the app ├── climate action.png # Climate action image ├── requirements.txt # List of dependencies └── README.md 

## Model Details 

The **XGBoost regressor** model used in this app has been trained on vehicle data with various features, including:
- Engine size
- Number of cylinders
- Fuel consumption in the city and on the highway
- Fuel types
- Vehicle class types

The model predicts the CO2 emissions of vehicles based on these input features.