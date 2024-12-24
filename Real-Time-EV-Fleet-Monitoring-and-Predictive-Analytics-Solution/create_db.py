import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Create a table for vehicle registrations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_name TEXT NOT NULL,
            vehicle_model TEXT NOT NULL,
            registration_number TEXT UNIQUE NOT NULL,
            battery_capacity REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and table created successfully.")
