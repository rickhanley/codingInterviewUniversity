import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import sqlite3


def todays_date_formatted(today_unformatted):
    return today_unformatted.strftime("%d/%m/%y")

def get_row_text(row_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    query = "SELECT detail FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def new_entry_save(modal_text):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    formatted_date = todays_date_formatted(datetime.now())
    due_date = formatted_date
    cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, formatted_date, 0, due_date))
    conn.commit()
    conn.close()
    # render_list()

# Close the connection



def open_modal(root, row_id):
    """Function to show the modal window to accept task specific data."""
    details_text = get_row_text(row_id)
    modal = tk.Toplevel(root)
    modal.title("Task Detail")
    modal.geometry("500x400")
    
    # Make the modal window expandable
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    
    # Canvas for potential scrolling (currently not used for scrolling)
    modal_scroll_canvas = tk.Canvas(modal, borderwidth=2, relief="solid")
    modal_scroll_canvas.grid(row=0, column=0, sticky="nsew")
    
    # Frame to contain the Text widget
    modal_scroll_frame = tk.Frame(modal_scroll_canvas)
    modal_scroll_frame.grid(sticky="nsew")
    
    # Make the frame expandable
    modal_scroll_canvas.grid_rowconfigure(0, weight=1)
    modal_scroll_canvas.grid_columnconfigure(0, weight=1)
    
    # Text widget that expands with the window
    modal_text = tk.Text(modal_scroll_frame, height=12, width=35)
    modal_text.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
    
    if details_text:  # Ensure there is content to insert
        modal_text.insert("1.0", details_text)
        modal_text.mark_set("insert", "end")
        modal_text.focus_set()  
        modal_text.see("insert")
    # Make the Text widget's frame expandable
    modal_scroll_frame.grid_rowconfigure(0, weight=1)
    modal_scroll_frame.grid_columnconfigure(0, weight=1)
    
    # Save button (not expandable)
    save_btn = tk.Button(modal, text="Save", font=("Arial", 16), command= lambda: new_entry_save(modal_text.get('1.0', 'end').strip()))
    save_btn.grid(row=1, column=0, padx=30, pady=30)
    
    # Make the modal window modal
    modal.grab_set()
    
def date_label_colour(due_date_str):
    """Function to determine the colour coding of the data labels"""
    due_date = datetime.strptime(due_date_str, "%d/%m/%y").date()
    today = date.today()
    days_diff = (due_date - today).days
    if days_diff < 3:  # Past due
        return "#e2738c"
    elif 0 <= days_diff <= 5:  # Due today or within 3 days
        return "#f6b26b"
    else:  # Due in more than 3 days
        return "#43aa8b"
    
def create_new_record(root):
    open_modal(root, None)

def hide_complete():
    pass
def sort_list():
    pass
def toggle_fill():
    pass
def refresh_list():
    pass