import sqlite3

def create_database():
    print("called")
    # Step 2: Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')  # This creates a new database file named 'example.db'

    # Step 3: Create a cursor object
    cursor = conn.cursor()

    # Step 4: Execute SQL commands to create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "table" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input TEXT NOT NULL
        )
    ''')
    # Step 5: Commit the changes
    conn.commit()
    # Step 6: Close the connection
    cursor.close()
    conn.close()
    
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    for i in range(100000):
        cursor.execute('INSERT INTO "table" (input) VALUES (?)', (f'{i}',))
    conn.commit()
    conn.close()    
    
create_database()