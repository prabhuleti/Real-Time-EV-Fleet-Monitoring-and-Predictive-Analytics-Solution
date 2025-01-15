import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Create a table for vehicle registrations with additional fields for fleet monitoring
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_name TEXT NOT NULL,
            vehicle_model TEXT NOT NULL,
            registration_number TEXT UNIQUE NOT NULL,
            battery_health REAL NOT NULL,
            status TEXT CHECK(status IN ('available', 'charging', 'in_service')) DEFAULT 'available',
            entry_time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and table for vehicle monitoring created successfully.")
