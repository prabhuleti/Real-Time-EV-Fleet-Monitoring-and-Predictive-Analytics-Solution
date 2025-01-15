import joblib

def battery_status_prediction(input_data):
    # Define the mapping of prediction output to battery status
    battery_status_map = {
        0: 'Excellent',
        1: 'Fair',
        2: 'Good',
        3: 'Needs Replacement'
    }

    # Load the model
    model_file = "battery_status_model.pkl"
    model = joblib.load(model_file)

    # Make the prediction
    prediction = model.predict([input_data])  # Ensure input_data is a list of features

    # Map the prediction to the corresponding battery status
    battery_status = battery_status_map.get(prediction[0], "Unknown Status")

    return battery_status


# Example input data
input_data = [4500,78,300,3.9,38,120]

# Call the function and print the result
status = battery_status_prediction(input_data)
print("Battery Status:", status)