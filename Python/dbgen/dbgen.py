import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.geometry("800x150")
def generate_db():
    try:
        conn = sqlite3.connect('yournewdb.db')
        cursor = conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dataset (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datapoint TEXT NOT NULL
                    )
                    ''')
        conn.commit()
        conn.close()
        print("clicked")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    

gen_btn = tk.Button(
    root,
    text="Generate",
    font=("Arial", 20),  # Font is supported
    padx=20,             # Horizontal padding
    pady=20,             # Vertical padding
    command=generate_db  # Lambda is unnecessary if no arguments are passed
)
gen_btn.grid(padx=20, pady=20)

root.mainloop()