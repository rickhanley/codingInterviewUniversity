import todolayout
import sqlite3
from tkinter import ttk
import tkinter as tk
import helpers

def render_list():
    
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM tasks WHERE complete = 0"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()
    
    for i, task in enumerate(tasks):
        task_id, creation_date, complete, detail, due_date = task
        padding_x = 15  # Horizontal padding
        

        completed_btn = ttk.Button(scroller, style="SmallButton.TButton", command=helpers.toggle_fill)
        label1 = tk.Label(scroller, text="      ", borderwidth=2, relief="groove", padx=12, pady=15)
        completed_btn.grid(row=i, column=0, padx=15, pady=1, sticky="ew") # external padding

        label2 = tk.Label(
            scroller,
            text=f"{detail}",
            borderwidth=2,
            relief="groove",
            padx=padding_x - 4,
            pady=15,  # Vertical padding
            justify="left"
        )
        
        row_id_map[label2] = task_id
        
        label2.grid(row=i, column=1, sticky="ew")
        label2.bind("<Configure>", lambda event, lbl=label2, pad=padding_x: update_wrap(event, lbl, pad))
        label2.bind("<Button-1>", lambda event, lbl=label2: helpers.open_modal(root, row_id_map[lbl]))

        
        label3 = tk.Label(scroller, text=f"{due_date}", borderwidth=2, relief="groove", padx=20, pady=15, background=f"{helpers.date_label_colour(due_date)}")
        label3.grid(row=i, column=2, padx=15, pady=15, sticky="ew")