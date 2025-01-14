import tkinter as tk
from tkinter import ttk
import sqlite3

def save_column_names():
    # Collect the user input from all text fields
    column_names = [entry.get() for entry in entry_fields]
    return column_names
    print("Column Names:", column_names)  # You can save or process these names as needed.
    
db_names = []
output_string = ''
    
def get_db_table_names():
    names = [entry.get() for entry in db_names]
    return names
    print(names)

def generate(output_string):
    column_names = save_column_names()
    top_level_names = get_db_table_names()
    execute_string = string_builder(top_level_names, column_names, selected_options, output_string)
    conn = sqlite3.connect(f'{top_level_names[0]}.db')
    cursor = conn.cursor()
    cursor.execute(f'{execute_string}')
    conn.commit()
    cursor.close()
    conn.close()
    print("Db created sucessfully!")
    status_update(output_string)

    # for i in range(len(entry_fields)):
    #     print(selected_options[i].get())
    
    
    
def string_builder(top_level_names, column_names, selected_options, output_string):
    starter_string = f'''CREATE TABLE IF NOT EXISTS {top_level_names[1]} (
        id INTEGER PRIMARY KEY AUTOINCREMENT'''
    for i in range(len(entry_fields)):
        if column_names[i] != '':
            starter_string += f', {column_names[i]} {selected_options[i].get()} NOT NULL'
        # code goes here to add in int columns
            
    starter_string += ')'
    print(starter_string)
    output_string = starter_string
    print(output_string)
    return starter_string
    
def clear():
    print("clear clicked")
    
    
def status_update(output_string):
    status.config(text=f"DB created: {output_string}")
    

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Column Name Entry")
root.geometry("1200x400")

top_frame = ttk.Frame(root, padding=10)
top_frame.grid(row=0, column=0, sticky="nsew")

top_label = ttk.Label(top_frame, text="DB Generator", font=("Arial", 20))
top_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

db_name_label = ttk.Label(top_frame, text=f"DB name", font=("Arial", 12))
db_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Create and place the entry field
db_name_entry = ttk.Entry(top_frame, font=("Arial", 12), width=10)
db_name_entry.grid(row=2, column=0, padx=10, pady=5, sticky="w")
db_names.append(db_name_entry)

db_name_label = ttk.Label(top_frame, text=f"DB Table Name", font=("Arial", 12))
db_name_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Create and place the entry field
db_table_name_entry = ttk.Entry(top_frame, font=("Arial", 12), width=10)
db_table_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
db_names.append(db_table_name_entry)
# Create a frame to organize the widgets


frame = ttk.Frame(root, padding=10)
frame.grid(row=10, column=0, sticky="nsew")

# List to store text entry fields
entry_fields = []

options = ["TEXT", "INTEGER", "REAL", "BLOB", "NULL"]
selected_options = []

def create_dropdown(row, options, i):
    selected_var = tk.StringVar()
    selected_var.set(options[0])
    dropdown = tk.OptionMenu(frame, selected_var, *options)
    dropdown.grid(row=row, column=i, padx=10, pady=5)
    selected_options.append(selected_var)

# Generate 10 labels and corresponding entry fields
for i in range(10):
    # Create and place the label
    label = ttk.Label(frame, text=f"Column {i+1}", font=("Arial", 12))
    label.grid(row=0, column=i, padx=10, pady=5, sticky="w")
    
    # Create and place the entry field
    entry = ttk.Entry(frame, font=("Arial", 12), width=10)
    entry.grid(row=1, column=i, padx=10, pady=5, sticky="w")
    create_dropdown(2, options, i)
    
    # Add the entry field to the list for later reference
    entry_fields.append(entry)

# Add a button to save the column names
save_button = ttk.Button(frame, text="Generate", command=generate)
save_button.grid(row=10, column=0, pady=20)

clear_button = ttk.Button(frame, text="Clear", command=clear)
clear_button.grid(row=10, column=1, pady=20)

status = ttk.Label(frame, text=f"Status", font=("Arial", 12))
status.grid(row=11, column=0, padx=10, pady=5, sticky="w")

# Start the Tkinter event loop
root.mainloop()
