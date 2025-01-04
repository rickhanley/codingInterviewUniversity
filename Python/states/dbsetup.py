import sqlite3
from datetime import datetime
from helpers import todays_date_formatted


# Format the date as dd-mm-yyyy
formatted_date = todays_date_formatted(datetime.now())

def create_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            creation_date TEXT NOT NULL,
            complete INTEGER NOT NULL,
            detail TEXT,
            due_date TEXT
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    
create_database()

creation_date = "14/12/24"
complete = 0
due_date = "25/01/25"
detail="First task goes here..."



def insert_data(creation_date, complete, due_date, detail):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (creation_date, complete, due_date, detail) VALUES (?, ?, ?, ?)", (creation_date, complete, due_date, detail))
    conn.commit()
    cursor.close()
    conn.close()
    
def sample_data():
    insert_data(creation_date, complete, due_date, detail)
        
sample_data()