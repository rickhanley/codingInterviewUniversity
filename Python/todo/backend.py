import sqlite3
from datetime import datetime

print("Hello")

def create_database_connection():
    try:
        conn = sqlite3.connect('userdb.db')
        return conn
    except sqlite3.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def create_tasks_table():
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS top_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                top_task TEXT NOT NULL,
                done INTEGER NOT NULL,
                due_date TEXT
            )
        ''')
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS subtasks (
                heading_id INTEGER,
                subtask TEXT NOT NULL,
                FOREIGN KEY (heading_id) REFERENCES top_tasks (id) ON DELETE CASCADE
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating tasks table: {err}")

def execute_query(query, params=None):
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    except sqlite3.Error as err:
        print(f"Error executing query: {err}")
        return []

def create_note(top_task='', due_date=None):
    insert_query = "INSERT INTO top_tasks (top_task, done, due_date) VALUES (?, ?, ?)"
    params = (top_task, 0, due_date)  # Assume done is 0 by default
    execute_query(insert_query, params)
    print("Note created successfully.")   

def get_note(note_id):
    select_query = "SELECT * FROM top_tasks WHERE id = ?"
    params = (note_id,)
    results = execute_query(select_query, params)
    if len(results) == 1:
        print(f"Retrieved note {note_id} successfully.")
        result = results[0]
    else:
        print(f"Note {note_id} not found.")
        result = None
    return result

def get_all_notes():
    select_query = "SELECT * FROM top_tasks ORDER BY due_date DESC"
    results = execute_query(select_query)
    print(f"Retrieved {len(results)} note(s) successfully.")
    return results

def update_note(note_id, new_top_task, done_status, due_date):
    update_query = "UPDATE top_tasks SET top_task = ?, done = ?, due_date = ? WHERE id = ?"
    params = (new_top_task, done_status, due_date, note_id)
    execute_query(update_query, params)
    print(f"Updated note {note_id} successfully.")

def delete_note(note_id):
    delete_query = "DELETE FROM top_tasks WHERE id = ?"
    params = (note_id,)
    execute_query(delete_query, params)
    print(f"Deleted note {note_id} successfully.")

def get_last_note_id():
    select_query = "SELECT * FROM top_tasks ORDER BY due_date DESC LIMIT 1"
    results = execute_query(select_query)
    if results:
        note = results[0]
        note_id = note[0]
        print(f"Retrieved most recently updated top_task successfully.")
        return note_id
    else:
        print("No notes found.")
        return None
