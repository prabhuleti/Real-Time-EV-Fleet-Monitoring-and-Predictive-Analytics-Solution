import sqlite3
from datetime import datetime

def insert_vehicle(vehicle_name, vehicle_model, registration_number, battery_health, status, entry_time):
    try:
        conn = sqlite3.connect('vehicle_data.db')
        cursor = conn.cursor()

        # Get current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert vehicle data with timestamp
        cursor.execute('''
            INSERT INTO vehicles (vehicle_name, vehicle_model, registration_number, battery_health, status, entry_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (vehicle_name, vehicle_model, registration_number, battery_health, status, current_time))

        conn.commit()
        print(f"Vehicle '{vehicle_name}' with registration '{registration_number}' inserted successfully at {current_time}.")
    
    except sqlite3.IntegrityError:
        print(f"Error: Vehicle with registration '{registration_number}' already exists.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        conn.close()


if __name__ == "__main__":

    # Get current timestamp
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Example vehicle data to insert
    vehicle_data = [
        ('Tesla Model 3', '2023', 'EV12345', 80.0, 'charging', current_time),
        ('Nissan Leaf', '2022', 'EV67890', 45.0, 'available', current_time),
        ('Chevrolet Bolt', '2021', 'EV13579', 60.0, 'in_service', current_time),
        ('Hyundai Kona', '2024', 'EV24680', 30.0, 'charging', current_time)
    ]

    # Insert each vehicle
    for vehicle in vehicle_data:
        insert_vehicle(*vehicle)
