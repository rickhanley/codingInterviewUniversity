import sqlite3

def create_database():
    # Step 2: Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('tw.db')  # This creates a new database file named 'example.db'

    # Step 3: Create a cursor object
    cursor = conn.cursor()

    # Step 4: Execute SQL commands to create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry TEXT NOT NULL
        )
    ''')

    # Step 5: Commit the changes
    conn.commit()

    # Step 6: Close the connection
    cursor.close()
    conn.close()
    
create_database()