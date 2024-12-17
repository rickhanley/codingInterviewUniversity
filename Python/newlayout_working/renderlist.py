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
    
    style = ttk.Style(root)
    style.configure("Default.TLabel", background="white", font=("Arial", 14), relief="groove", padding=(24, 15))
    style.configure("Toggled.TLabel", background="lightblue", font=("Arial", 14), relief="groove", padding=(24, 15))
    
    
    for i, task in enumerate(tasks):
        row_id, creation_date, complete, detail, due_date = task
        padding_x = 50  # Horizontal padding

        # completed_lbl = ttk.Label(scroller, text="", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
        completed_lbl = ttk.Label(scroller, text=f"", font=("Arial", 14), borderwidth=1, relief="groove", padding=(24, 15), style="Default.TLabel")
        completed_lbl.grid(row=i, column=0, padx=(15,15), sticky="ew")  # external padding
        completed_lbl.bind("<Button-1>", lambda e, lbl=completed_lbl, row_id = row_id: helpers.toggle_fill(e, lbl, style, row_id))

        label2 = tk.Label(
            scroller,
            text=f"{detail.strip().replace('\n', ' ')[:70]}{'...' if len(detail) > 70 else ''}",
            borderwidth=2,
            relief="groove",
            pady=15,
            padx=5,# Vertical padding
            justify="left",
            font=("Arial", 14)
        )
        
        row_id_map[label2] = row_id
        
        label2.grid(row=i, column=1, sticky="ew")

        # Bind the event to label2 for opening a modal
        def on_label2_click(event, task_id=row_id, due_date=due_date): 
            helpers.open_modal(root, scroller, task_id, due_date)
        
        label2.bind("<Button-1>", on_label2_click)

        # Bind event for wrapping the text on resize
        def on_label2_resize(event, label=label2, padding_x=padding_x):
            update_wrap(event, label, padding_x)
        
        label2.bind("<Configure>", on_label2_resize)

        label3 = tk.Label(scroller, text=f"{due_date}", borderwidth=1, relief="solid", font=("Arial", 14), pady=16, padx=15, background=f"{helpers.date_label_colour(due_date)}")
        label3.grid(row=i, column=2, pady=15, padx=(16, 6), sticky="ew")
