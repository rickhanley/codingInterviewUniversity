import sqlite3
from datetime import datetime

# Get today's date
today = datetime.now()

# Format the date as dd-mm-yyyy
formatted_date = today.strftime("%d-%m-%Y")

# Print the formatted date
print(formatted_date)

# Store the date in a variable
date_variable = formatted_date

def create_database():
    # Step 2: Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')  # This creates a new database file named 'example.db'

    # Step 3: Create a cursor object
    cursor = conn.cursor()

    # Step 4: Execute SQL commands to create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS headings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heading TEXT NOT NULL,
            done INTEGER NOT NULL,
            due_date TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subtasks (
            heading_id,
            subtask TEXT NOT NULL,
            FOREIGN KEY (heading_id) REFERENCES headings (id) ON DELETE CASCADE
        )
    ''')

    # Step 5: Commit the changes
    conn.commit()

    # Step 6: Close the connection
    cursor.close()
    conn.close()
    
def insert_heading(heading, done, due_date):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO headings (heading, done, due_date) VALUES (?, ?, ?)", (heading, done, due_date))
    conn.commit()
    cursor.close()
    conn.close()

def insert_subtask(heading_id, subtask):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subtasks (heading_id, subtask) VALUES (?, ?)", (heading_id, subtask))
    conn.commit()
    cursor.close()
    conn.close()
    

# Call the function to create the database and table
create_database()

for i in range(1, 16):
    insert_heading(f"Task Heading {i}", 0, "3-11-2024")  # Adding a heading

# Assuming the ID of 'Project A' is 1 (the first entry), add subtasks for it

insert_subtask(1, 'Subtask for Project 1')
insert_subtask(1, 'Subtask for Project 1')

# Assuming the ID of 'Project B' is 2 (the second entry), add subtasks for it
insert_subtask(2, 'Subtask 1 for Project 2')
insert_subtask(2, 'Subtask 2 for Project 2')
insert_subtask(2, 'Subtask 3 for Project 2')
insert_subtask(2, 'Subtask 4 for Project 2')
insert_subtask(2, 'Subtask 5 for Project 2')
