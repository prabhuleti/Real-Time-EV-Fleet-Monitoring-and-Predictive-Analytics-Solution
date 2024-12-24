import sqlite3

def fetch_all_vehicles():
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Retrieve all data
    cursor.execute('SELECT * FROM vehicles')
    vehicles = cursor.fetchall()

    conn.close()
    return vehicles

def update_battery_capacity(registration_number, new_battery_capacity):
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Update the battery capacity for a specific vehicle
    cursor.execute('''
        UPDATE vehicles
        SET battery_capacity = ?
        WHERE registration_number = ?
    ''', (new_battery_capacity, registration_number))

    if cursor.rowcount == 0:
        print("No vehicle found with the given registration number.")
    else:
        print("Battery capacity updated successfully.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Example usage
    data = fetch_all_vehicles()
    for row in data:
        print(row)
    update_battery_capacity("AB123CD", 85.0)
