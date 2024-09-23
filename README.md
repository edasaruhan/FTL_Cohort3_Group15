# CO2 Emissions Vehicle Prediction App

This is a web application that predicts vehicle CO2 emissions based on various vehicle specifications using a Ridge regression model. The app is built using **Streamlit** and allows users to input vehicle details to receive CO2 emission predictions.

## Features
- Predict CO2 emissions for vehicles based on specifications like engine size, cylinders, and fuel consumption.
- Basic login authentication for app access.
- Real-time input with immediate predictions.
- User-friendly interface built with Streamlit.

## Frameworks and Libraries Used
- **Streamlit**: For building the web app.
- **scikit-learn**: For machine learning (Ridge regression).
- **pandas**: For data manipulation.
- **joblib**: For model loading and serialization.

## Installation

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

## Authentication

This app requires login credentials to access the CO2 emissions prediction tool.

### Login Credentials:
- **Username**: `admin`
- **Password**: `password123`

Upon logging in with these credentials, you can access the prediction functionality.

## Usage

1. After logging in, input the vehicle specifications in the fields provided.
2. Press the **Predict CO2 Emissions** button.
3. The app will display the predicted CO2 emissions in grams per kilometer (g/km).
4. If your vehicle's emissions exceed 108.1 g/km, the app will recommend considering a replacement to reduce emissions.

## File Structure

├── app.py # The main app file ├── best_ridge_model.pkl # Pre-trained Ridge regression model ├── co2vehicle.JPEG # Image displayed in the app ├── requirements.txt # List of dependencies └── README.md

## Model Details

The Ridge regression model used in this app has been trained on vehicle data with various features, including:
- Engine size
- Number of cylinders
- Fuel consumption in the city and on the highway
- Fuel types
- Transmission types
- Vehicle class types

The model predicts the CO2 emissions of vehicles based on these input features.
