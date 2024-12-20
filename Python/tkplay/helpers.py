import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import sqlite3
import renderlist
from tkinter import *
from tkcalendar import Calendar

def todays_date_formatted(today_unformatted):
    return today_unformatted.strftime("%d/%m/%y")

def date_picker(parent_modal):
    # Create a new Toplevel window for the date picker
    date_modal = tk.Toplevel(parent_modal)
    date_modal.title("Select Date")
    date_modal.geometry("400x400")  # Adjust the size as needed
    
    # Make the date picker modal (blocks interaction with parent_modal until closed)
    date_modal.transient(parent_modal)
    date_modal.grab_set()

    # Add a Calendar widget to the date modal
    calendar = Calendar(date_modal, date_pattern="dd/mm/yy", showweeknumbers=False)
    calendar.grid(padx=20, pady=20)

    # Add a button to confirm the date selection
    def confirm_date():
        selected_date = calendar.get_date()
        print(f"Selected Date: {selected_date}")
        # I think the code to update the date should go here
        # and the selected_date needs to be returned to where the button is rendered 
        # ^^ That is the label in open_modal()
        # Close the date picker modal
        date_modal.destroy()
        # Optionally, update the parent modal or perform further actions with the selected date

    confirm_button = tk.Button(date_modal, text="Confirm", command=confirm_date)
    confirm_button.grid(padx=20, pady=10)

    # Add a cancel button to close the date picker without selecting a date
    cancel_button = tk.Button(date_modal, text="Cancel", command=date_modal.destroy)
    cancel_button.grid(padx=20, pady=10)

def get_row_text(row_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    query = "SELECT detail FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def existing_entry_update(modal_text, root, scroller, row_id, modal):
    print(row_id)
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    # need to address due_date but for now will be left unchanged
    cursor.execute('UPDATE tasks SET detail = ? WHERE id = ?', (modal_text, row_id))
    conn.commit()
    conn.close()
    modal.destroy()
    renderlist.render_list(root, scroller)

def new_entry_save(modal_text, root, scroller, modal):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    formatted_date = todays_date_formatted(datetime.now())
    due_date = formatted_date
    cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, formatted_date, 0, due_date))
    conn.commit()
    conn.close()
    modal.destroy()
    renderlist.render_list(root, scroller)

def open_modal(root, scroller, row_id, due_date):
    update = False
    
    if row_id is not None:
        details_text = get_row_text(row_id)
        update = True
        
    else:
        details_text = ""
    
    print(f"Row ID: {row_id}")
    """Function to show the modal window to accept task specific data."""
    
    modal = tk.Toplevel(root)
    modal.title("Task Detail")
    modal.geometry("500x400")
    
    # Make the modal window expandable
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    
    # Canvas for potential scrolling (currently not used for scrolling)
    modal_scroll_canvas = tk.Canvas(modal, borderwidth=2, relief="solid")
    modal_scroll_canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    # Frame to contain the Text widget
    modal_scroll_frame = tk.Frame(modal_scroll_canvas)
    modal_scroll_frame.grid(sticky="nsew")
    
    # Make the frame expandable
    modal_scroll_canvas.grid_rowconfigure(0, weight=1)
    modal_scroll_canvas.grid_columnconfigure(0, weight=1)
    
    # Text widget that expands with the window
    modal_text = tk.Text(modal_scroll_frame, height=12, width=35)
    modal_text.grid(row=0, column=0, columnspan=2, padx=15, pady=15, sticky="nsew")
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    modal.grid_columnconfigure(1, weight=1)  # Add weight for column 1 as well
    scrollbar = tk.Scrollbar(modal_scroll_frame, command=modal_text.yview)
    scrollbar.grid(sticky="ns", column=1, row=0)

    # Link the scrollbar to the Text widget
    modal_text.config(yscrollcommand=scrollbar.set)
    
    if details_text:  # Ensure there is content to insert
        modal_text.insert("1.0", details_text)
        modal_text.mark_set("insert", "end")
        modal_text.focus_set()  
        modal_text.see("insert")
    # Make the Text widget's frame expandable
    modal_scroll_frame.grid_rowconfigure(0, weight=1)
    modal_scroll_frame.grid_columnconfigure(0, weight=1)
    
    # Save button (not expandable)
    if update == True:
        save_btn = tk.Button(modal, text="Save", font=("Arial", 16), command= lambda: existing_entry_update(modal_text.get('1.0', 'end').strip(), root, scroller, row_id, modal))
        save_btn.grid(row=1, column=0, padx=30, pady=30)
    else:
        save_btn = tk.Button(modal, text="Save", font=("Arial", 16), command= lambda: new_entry_save(modal_text.get('1.0', 'end').strip(), root, scroller, modal))
        save_btn.grid(row=1, column=0, padx=30, pady=30)
        
    date_label = tk.Button(modal, text=f"{due_date}", font=("Arial", 16), command= lambda: date_picker(modal, due_date))
    date_label.grid(row=1, column=1, padx=30, pady=30)
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
    
def create_new_record(root, scroller):
    open_modal(root, scroller, None)
    
def hide_complete():
    pass
def sort_list():
    pass
def toggle_fill():
    pass
def refresh_list(root, scroller):
    renderlist.render_list(root, scroller)