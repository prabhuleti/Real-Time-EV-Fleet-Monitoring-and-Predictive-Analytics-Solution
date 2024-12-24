import sqlite3

def insert_vehicle(vehicle_name, vehicle_model, registration_number, battery_capacity):
    try:
        conn = sqlite3.connect('vehicle_data.db')
        cursor = conn.cursor()

        # Insert vehicle data
        cursor.execute('''
            INSERT INTO vehicles (vehicle_name, vehicle_model, registration_number, battery_capacity)
            VALUES (?, ?, ?, ?)
        ''', (vehicle_name, vehicle_model, registration_number, battery_capacity))

        conn.commit()
        print("Vehicle registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Registration number must be unique.")
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage
    insert_vehicle("Tesla", "Model 3", "AB123CD", 75.0)
