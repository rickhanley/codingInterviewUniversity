import sqlite3
from tkinter import ttk
import tkinter as tk
import helpers
import sort_state
import os
from helpers import get_database_path

db_path = get_database_path()

# test data for date fields
row_id_map = {}

def update_wrap(event, label, padding_x):
    # Dynamically adjust wraplength based on label width and padding
    label.configure(wraplength=label.winfo_width() - padding_x * 2)

def render_list(root, scroller, hide_state_dict, data_set=None):
    option = 0
    current_state = sort_state.sort_order_toggle(0)
    # Clear any existing widgets
    for widget in scroller.winfo_children():
        widget.destroy()
    # print(f"Remaining widgets: {scroller.winfo_children()}")  # Should be empty
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if data_set == None:
        if option == 0:
            if current_state == "standard":
                query = "SELECT * FROM tasks WHERE complete = 0"
            elif current_state == "due_date":
                query = "SELECT * FROM tasks WHERE complete = 0 ORDER BY due_date ASC"
        elif option == 1:
            if current_state == "standard":
                query = "SELECT * FROM tasks"
            elif current_state == "due_date":
                query = "SELECT * FROM tasks ORDER BY due_date ASC"
        cursor.execute(query)
    elif data_set:
        cursor = data_set
    tasks = cursor.fetchall()
    conn.close()

    style = ttk.Style(root)
    style.configure("Default.TLabel", background="white", font=("Arial", 14), relief="groove", padding=(24, 15))
    style.configure("Toggled.TLabel", background="lightblue", font=("Arial", 14), relief="groove", padding=(24, 15))
    
    
    for i, task in enumerate(tasks):
        
        row_id, creation_date, complete, detail, due_date = task
        padding_x = 50  # Horizontal padding

        # print(f"Placing task {i} at row {i}: {detail}, {due_date}")
        # completed_lbl = ttk.Label(scroller, text="", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
        if complete:
            completed_lbl = ttk.Label(scroller, text=f"\u2714", font=("Arial", 14), borderwidth=1, relief="groove", padding=(17, 15), style="Default.TLabel")
        else:
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
            helpers.open_modal(root, scroller, task_id, due_date, hide_state_dict)
        
        label2.bind("<Button-1>", on_label2_click)

        # Bind event for wrapping the text on resize
        def on_label2_resize(event, label=label2, padding_x=padding_x):
            update_wrap(event, label, padding_x)
        
        label2.bind("<Configure>", on_label2_resize)

        label3 = tk.Label(scroller, text=f"{helpers.date_for_display(due_date)}", borderwidth=1, relief="solid", font=("Arial", 14), pady=16, padx=15, background=f"{helpers.date_label_colour(due_date)}")
        label3.grid(row=i, column=2, pady=3, padx=(16, 6), sticky="ew")
