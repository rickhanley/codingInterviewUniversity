import sqlite3
from tkinter import ttk
import tkinter as tk
import helpers

# test data for date fields
row_id_map = {}



def update_wrap(event, label, padding_x):
    # Dynamically adjust wraplength based on label width and padding
    label.configure(wraplength=label.winfo_width() - padding_x * 2)

def render_list(root, scroller):
    # Clear any existing widgets
    for widget in scroller.winfo_children():
        widget.destroy()
    
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM tasks WHERE complete = 0"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()
    
    for i, task in enumerate(tasks):
        task_id, creation_date, complete, detail, due_date = task
        padding_x = 50  # Horizontal padding

        # completed_btn = ttk.Label(scroller, text="", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
        completed_btn = ttk.Label(scroller, text=f"{u'\u2713'}", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
        completed_btn.grid(row=i, column=0, padx=(16,17), sticky="ew")  # external padding

        label2 = tk.Label(
            scroller,
            text=f"{detail.strip().replace('\n', ' ')[:70]}{'...' if len(detail) > 80 else ''}",
            borderwidth=2,
            relief="groove",
            pady=15,  # Vertical padding
            padx=15,
            justify="left"
        )
        
        row_id_map[label2] = task_id
        
        label2.grid(row=i, column=1, sticky="ew", padx=1)

        # Bind the event to label2 for opening a modal
        def on_label2_click(event, task_id=task_id, due_date=due_date):
            helpers.open_modal(root, scroller, task_id, due_date)
        
        label2.bind("<Button-1>", on_label2_click)

        # Bind event for wrapping the text on resize
        def on_label2_resize(event, label=label2, padding_x=padding_x):
            update_wrap(event, label, padding_x)
        
        label2.bind("<Configure>", on_label2_resize)

        label3 = tk.Label(scroller, text=f"{due_date}", borderwidth=1, relief="solid", pady=15, padx=17, background=f"{helpers.date_label_colour(due_date)}")
        label3.grid(row=i, column=2, pady=15, padx=(15, 0), sticky="ew")
