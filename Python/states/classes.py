
import sqlite3

class Taskmanager:
    def __init__(self):
        self.tasks = []
        self.counter = 0
       
    def increment(self):
        self.tasks.append(self.counter)
        self.counter += 1
        
    def print_info(self):
        print(f"Self tasks{self.tasks}")
        
    def retrieve_data(self):
        conn = sqlite3.connect("../tasks.db")
        # cursor = conn.cursor()
        # conn.commit()
        conn.close()
        print("DB opended and closed")
        
    def create_db(self):
        conn = sqlite3.connect('test.db')
        print("Connected")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                forename TEXT NOT NULL,
                surname TEXT NOT NULL,
                dob TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        
    def add_item(self, forename, surname, dob):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (forename, surname, dob) VALUES (?, ?, ?)', (forename,surname, dob))
        conn.commit()
        cursor.close()
        conn.close()
        
    def view_items(self):
        print("view self")
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        for task in tasks:
            print("in for")
            row_id, creation_date, complete, detail, due_date = task
            print(f"id: {row_id}  Creation: {creation_date}  complete: {complete}  due: {due_date}")
        cursor.close()
        conn.close()
        
    def delete(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id > ?',(2, ))
        conn.commit()
        cursor.close()
        conn.close()
        
        
        