import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import sqlite3
import renderlist
# from tkinter import *
from tkcalendar import Calendar


def todays_date_formatted(today_unformatted):
    return today_unformatted.strftime("%d/%m/%y")

def date_picker(parent_modal, date_label, row_id):
    # Create a new Toplevel window for the date picker
    print(f"CGET: {date_label.cget("text")}")
    date_modal = tk.Toplevel(parent_modal)
    date_modal.title("Select Date")
    date_modal.geometry("420x380")  # Adjust the size as needed
    

    # Make the date picker modal (blocks interaction with parent_modal until closed)
    date_modal.transient(parent_modal)
    date_modal.grab_set()

    # Add a Calendar widget to the date modal
    calendar = Calendar(date_modal, date_pattern="dd/mm/yy", font=("Arial", 20))
    calendar.grid(padx=20, pady=20, columnspan=2)

    # Add a button to confirm the date selection
    def confirm_date():
        selected_date = calendar.get_date()
        print(f"Selected Date from confirm date: {selected_date}")
        print(f"row_id: {row_id}")
        try:
            conn = sqlite3.connect("tasks.db")
            cursor = conn.cursor()
            # need to address due_date but for now will be left unchanged
            cursor.execute('UPDATE tasks SET due_date = ? WHERE id = ?', (selected_date, row_id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            
        date_label.config(text=selected_date)  # Update the date_label text
        date_modal.destroy()  # Close the date modal
        # return selected_date

    confirm_button = tk.Button(date_modal, text="Confirm", command=confirm_date, font=("Arial", 20), padx=15, pady=15)
    confirm_button.grid(column=0, row=1, padx=20, pady=10)

    # Add a cancel button to close the date picker without selecting a date
    cancel_button = tk.Button(date_modal, text="Cancel", command=date_modal.destroy, font=("Arial", 20), padx=15, pady=15)
    cancel_button.grid(column=1, row=1, padx=20, pady=10)

def get_row_text(row_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    query = "SELECT detail FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def existing_entry_update(modal_text, root, scroller, row_id, modal):
    print(f"Exisitng entry, ROW_ID: {row_id}")
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    # need to address due_date but for now will be left unchanged
    cursor.execute('UPDATE tasks SET detail = ? WHERE id = ?', (modal_text, row_id))
    conn.commit()
    
    conn.close()
    
    modal.destroy()
    renderlist.render_list(root, scroller)

# def new_entry_save(modal_text, root, scroller, modal):
#     print("New entry save")
#     conn = sqlite3.connect("tasks.db")
#     cursor = conn.cursor()
#     formatted_date = todays_date_formatted(datetime.now())
#     due_date = formatted_date
#     cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, formatted_date, 0, due_date))
#     new_task_id = cursor.lastrowid
#     conn.commit()
#     conn.close()
#     modal.destroy()
#     renderlist.render_list(root, scroller)

def open_modal(root, scroller, row_id, due_date):
    
    if row_id is not None:
        details_text = get_row_text(row_id)
    else:
        details_text = ""
    
    print(f"Row ID: {row_id}")
    """Function to show the modal window to accept task-specific data."""
    
    modal = tk.Toplevel(root)
    modal.title("Task Detail")
    modal.geometry("500x400")
    
    # Make the modal window expandable
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    modal.grid_columnconfigure(1, weight=1)
    modal.grid_columnconfigure(2, weight=1)  # Ensure the third column is weight-adjustable
    
    # Canvas for potential scrolling (currently not used for scrolling)
    modal_scroll_canvas = tk.Canvas(modal, borderwidth=2, relief="solid")
    modal_scroll_canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")  # Span across all 3 columns
    
    # Frame to contain the Text widget
    modal_scroll_frame = tk.Frame(modal_scroll_canvas)
    modal_scroll_frame.grid(sticky="nsew")
    
    # Make the frame expandable
    modal_scroll_canvas.grid_rowconfigure(0, weight=1)
    modal_scroll_canvas.grid_columnconfigure(0, weight=1)
    
    # Text widget that expands with the window
    modal_text = tk.Text(modal_scroll_frame, height=12, width=35, font=("Arial", 16))
    modal_text.grid(row=0, column=0, columnspan=3, padx=15, pady=15, sticky="nsew")
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    modal.grid_columnconfigure(1, weight=1)
    modal.grid_columnconfigure(2, weight=1)  # Add weight for column 2 as well
    
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
    
    # Save button
    save_btn = tk.Button(modal, text="Save", font=("Arial", 20), command= lambda: existing_entry_update(modal_text.get('1.0', 'end').strip(), root, scroller, row_id, modal), padx=15, pady=15)
    save_btn.grid(row=1, column=0, padx=30, pady=30)
    date_label = tk.Button(modal, text=f"{due_date}", font=("Arial", 20), command= lambda: date_picker(modal, date_label, row_id), padx=15, pady=15)
    date_label.grid(row=1, column=1, padx=30, pady=30)
    delete_button = tk.Button(modal, text="Delete", font=("Arial", 20), command= lambda: delete_entry(row_id, root, scroller, modal), padx=15, pady=15)
    delete_button.grid(row=1, column=2, padx=30, pady=30)
        
        
    def on_close(details_text):
        if details_text == '':
            print("On close")
            # Call the delete_record method to remove the blank record
            delete_entry(row_id, root, scroller, modal)
            modal.destroy()
        else:
            modal.destroy()
    modal.protocol("WM_DELETE_WINDOW", lambda: on_close(details_text))
    # Make the modal window modal
    modal.grab_set()

    
def date_label_colour(due_date_str):
    """Function to determine the colour coding of the data labels
       > 5 days to due date colour is green
       3, 4 or 5 days colour is orange
       <3 days is red"""
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
    print("create new")
    modal_text=''
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    due_date = todays_date_formatted(datetime.now())
    formatted_date = due_date
    cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, formatted_date, 0, due_date))
    conn.commit()
    new_task_id = cursor.lastrowid
    print(f"last row: {new_task_id}")
    conn.close()
    open_modal(root, scroller, new_task_id, due_date)
    
def delete_entry(row_id, root, scroller, modal):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    conn.commit()
    conn.close()
    refresh_list(root,scroller)
    modal.destroy()
    
def hide_complete():
    pass
def sort_list():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    query = "SELECT * FROM tasks WHERE complete = 0 ORDER BY due_date ASC"
    cursor.execute(query)
    tasks = cursor.fetchall()
    conn.close()
    return tasks



import sqlite3

def toggle_fill(event, lbl, style, row_id):
    """Toggle the fill of the label to indicate done and update the DB."""
    print("toggle fill clicked")
    print(f"row_id: {row_id}")
    
    # Toggle the style of the label
    current_style = lbl.cget("style")
    new_style = "Toggled.TLabel" if current_style == "Default.TLabel" else "Default.TLabel"
    lbl.configure(style=new_style)

    try:
        # Connect to the database
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        
        # Fetch the current 'complete' value
        cursor.execute('SELECT complete FROM tasks WHERE id = ?', (row_id,))
        result = cursor.fetchone()
        
        if result is not None:
            current_value = result[0]
    # Toggle the value of 'complete'
            toggle = 0 if current_value == 1 else 1
            # Toggle the value of 'complete'
            
            # Update the 'complete' value in the database
            cursor.execute('UPDATE tasks SET complete = ? WHERE id = ?', (toggle, row_id))
            print(f"Rowd id: {row_id} updated")
            conn.commit()
        else:
            print(f"No task found with row_id {row_id}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Always close the connection
        conn.close()

       
    pass
def refresh_list(root, scroller):
    print("REFRESH called")
    renderlist.render_list(root, scroller)