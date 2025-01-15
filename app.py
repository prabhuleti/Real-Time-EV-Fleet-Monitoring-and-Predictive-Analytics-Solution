from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle
import random
from datetime import datetime
import requests
from users_db import create_user, get_user
from insert_data import insert_vehicle
from retrieve_data import fetch_all_vehicles, delete_vehicle_by_id
import numpy as np
import pandas as pd
import csv
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Needed for flash messages

# Load the trained battery status prediction model
with open(r"C:\Users\anant_1kqfc\OneDrive\Desktop\Real-Time-EV-Monitoring-And-Predictive-Analytics-Solution\models\battery_health_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
    
# Load the dataset from the pickle file
data_file = r"C:\Users\anant_1kqfc\OneDrive\Desktop\Real-Time-EV-Monitoring-And-Predictive-Analytics-Solution\models\Tamilnadu_EV_Stations.pkl"
ev_stations = pd.read_pickle(data_file)

# Initialize the geocoder
geolocator = Nominatim(user_agent="ev_station_locator")

@app.route("/")
def index():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = get_user(email, password)  # Pass both email and password
        
        if user:
            return render_template('login.html', message='Login successful', success=True, redirect_url='/histogram.html')
        else:
            return render_template('login.html', message='Invalid credentials', success=False)

    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    if password != confirm_password:
        return render_template('login.html', message='Passwords do not match', success=False)
    
    if create_user(email, password):
        return render_template('login.html', message='Signup successful', success=True)
    else:
        return render_template('login.html', message='Signup failed', success=False)
    
    return render_template('login.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route("/Battery Health Status Section.html")
def Battery_Health_Status_Section():
    return render_template("Battery Health Status Section.html")

@app.route("/Cost and Energy Consumption.html")
def Cost_and_Energy_Consumption():
    return render_template("Cost and Energy Consumption.html")

@app.route("/cost and energy trends.html")
def cost_and_energy_trends():
    return render_template("cost and energy trends.html")

@app.route("/Display Behavior Analysis and Alerts.html")
def Display_Behavior_Analysis_and_Alerts():
    return render_template("Display Behavior Analysis and Alerts.html")

@app.route("/Driver Behavior and Maintenance Alerts.html")
def Driver_Behavior_and_Maintenance_Alerts():
    return render_template("Driver Behavior and Maintenance Alerts.html")


@app.route("/vehicle_registration.html")
def vehicle_registration():
    return render_template("vehicle_registration.html")

@app.route("/Vehicle List.html")
def vehicle_list():
    return render_template("Vehicle List.html")

@app.route("/histogram.html")
def histogram():
    return render_template("histogram.html")

@app.route('/register_vehicle', methods=['POST'])
def register_vehicle():
    data = request.json
    try:
        insert_vehicle(
            data['vehicle_name'],
            data['vehicle_model'],
            data['registration_number'],
            data['battery_health'],
            data['status_data']
        )
        return jsonify({"message": "Vehicle registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    vehicles = fetch_all_vehicles()
    return jsonify(vehicles), 200

@app.route('/remove_vehicle/<int:vehicle_id>', methods=['DELETE'])
def remove_vehicle(vehicle_id):
    try:
        # called the function from retrieve_data.py to delete the vehicle
        delete_vehicle_by_id(vehicle_id)
        return jsonify({"message": "Vehicle removed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/battery_health_status', methods=['POST'])
def battery_health_status():
    try:
        # Get form inputs
        capacity = float(request.form['capacity'])
        cycle_count = int(request.form['cycle_count'])
        voltage = float(request.form['voltage'])
        temperature = float(request.form['temperature'])
        resistance = float(request.form['resistance'])
        
        # Create feature array for prediction
        features = np.array([[capacity, cycle_count, voltage, temperature, resistance]])
        
        # Make prediction
        prediction = model.predict(features)
        health_percentage = prediction[0]
        
        # Categorize battery health based on predicted percentage
        if health_percentage >= 90:
            health_status = "Excellent"
        elif 80 <= health_percentage < 90:
            health_status = "Good"
        elif 60 <= health_percentage < 80:
            health_status = "Fair"
        else:
            health_status = "Needs Replacement"
        
        # Return the result with the health status
        return render_template('Battery Health Status Section.html', prediction_text=f"Predicted Battery Health: {health_percentage:.2f}% - {health_status}")
    except Exception as e:
        return render_template('Battery Health Status Section.html', prediction_text=f"Error: {e}")

@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    # Get source and destination from the form
    source_city = request.form.get('source_city')
    dest_city = request.form.get('dest_city')

    # Get coordinates for the source and destination cities
    source_location = geolocator.geocode(source_city)
    dest_location = geolocator.geocode(dest_city)

    if not source_location or not dest_location:
        return render_template('optimize_route.html', error="Could not find the location. Please check the city names.")

    source_coords = (source_location.latitude, source_location.longitude)
    destination_coords = (dest_location.latitude, dest_location.longitude)

    # Filter EV stations within 10 km of the source or destination
    stations_near_route = []
    for _, row in ev_stations.iterrows():
        station_coords = (row['Latitude'], row['Longitude'])
        if geodesic(source_coords, station_coords).km <= 10 or geodesic(destination_coords, station_coords).km <= 10:
            stations_near_route.append({
                "name": row['Station Name'],
                "address": row['Address'],
                "capacity": row['Charging Capacity'],
                "facilities": row['Facilities'],
                "latitude": row['Latitude'],
                "longitude": row['Longitude']
            })

    return render_template('optimize_route.html', stations=stations_near_route)

@app.route('/optimize_route')
def optimize_route1():
    return render_template('optimize_route.html')


@app.route("/Report Generation.html")
def Report_Generation():
    vehicles = fetch_all_vehicles()

    vehicle_list = []
    for vehicle in vehicles:
        vehicle_data = {
            'id': vehicle[0],  # Vehicle ID
            'vehicle_name': vehicle[1],  # Vehicle Name
            'vehicle_model': vehicle[2],  # Vehicle Model
            'registration_number': vehicle[3],  # Registration Number
            'battery_health': vehicle[4],  # Battery Health
            'status': vehicle[5],  # Status
            'entry_date': vehicle[6],  # Entry Date
            }
        
        vehicle_list.append(vehicle_data)

    # Calculate Insights
    total_vehicles = len(vehicles)
    healthy_battery = sum(1 for v in vehicle_list if v['battery_health'] >= 50)
    degrade_battery = total_vehicles - healthy_battery

    status_counts = {
        'available': sum(1 for v in vehicle_list if v['status'] == 'available'),
        'in_service': sum(1 for v in vehicle_list if v['status'] == 'in_service'),
        'charging': sum(1 for v in vehicle_list if v['status'] == 'charging')
    }
    return render_template(
        "Report Generation.html",
        vehicles=vehicle_list, 
        total_vehicles=total_vehicles, 
        healthy_battery=healthy_battery, 
        degrade_battery=degrade_battery, 
        status_counts=status_counts)

    
if __name__ == "__main__":
    # Run the app with debugging enabled
    app.run(port=5000, debug=True)
