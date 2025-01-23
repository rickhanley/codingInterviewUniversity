import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import sqlite3
import renderlist
# from tkinter import *
from tkcalendar import Calendar
from sort_state import sort_order_toggle
from sort_state import sort_order_dict
import os, shutil, sys
from pathlib import Path


def menu_save():
    pass

def get_database_path():
    """Determine the correct database path based on the environment."""
    # Check if running as a PyInstaller bundle
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Running as a bundled app
        base_dir = sys._MEIPASS  # Temp directory created by PyInstaller
    else:
        # Running in development
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # In development, return the existing database path
    db_path = os.path.join(base_dir, "data", "tasks.db")

    # In production, ensure the database is writable
    if getattr(sys, 'frozen', False):
        # Use the user's writable application data directory
        app_data_dir = Path.home() / ".quicktask"
        app_data_dir.mkdir(parents=True, exist_ok=True)
        writable_db_path = app_data_dir / "tasks.db"
        # If the database doesn't exist, copy it from the bundled directory
        if not writable_db_path.exists():
            shutil.copy(db_path, writable_db_path)
        return str(writable_db_path)
    return db_path
db_path = get_database_path()

def date_for_saving(date_string):
    """Take in string of fromat dd/mm/yy and change to formater YYYY/mm/yy"""
    date_object = datetime.strptime(date_string, "%d/%m/%y")
    date_for_saving = date_object.strftime("%Y/%m/%d")
    return date_for_saving

def date_for_display(date_string):
    """Take in string of format YYYY/mm/dd and change to formater dd/mm/yy"""
    date_object = datetime.strptime(date_string, "%Y/%m/%d")
    date_for_display = date_object.strftime("%d/%m/%y")
    return date_for_display

def todays_date_formatted(today_unformatted):
    # print(f"todays_date_formatted input is: {today_unformatted}")
    today_formatted = today_unformatted.strftime("%Y/%m/%d")
    # print(f"todays_date_formatted input after conversion is: {today_formatted}")
    return today_formatted

def date_picker(parent_modal, date_label, row_id):
    # Create a new Toplevel window for the date picker
    
    print(f"CGET: {date_label.cget("text")}")    
    date_modal = tk.Toplevel(parent_modal)
    date_modal.title("Select Date")
    date_modal.geometry("420x380")  # Adjust the size as needed
    root_x = parent_modal.winfo_x()
    root_y = parent_modal.winfo_y()
    root_width = parent_modal.winfo_width()
    root_height = parent_modal.winfo_height()
    modal_width = 415
    modal_height = 400
    position_right = root_x + 300
    position_down = root_y + -150

    date_modal.geometry(f"{modal_width}x{modal_height}+{position_right}+{position_down}")

    # Make the date picker modal (blocks interaction with parent_modal until closed)
    date_modal.transient(parent_modal)
    date_modal.grab_set()

    # Add a Calendar widget to the date modal
    calendar = Calendar(date_modal, date_pattern="dd/mm/yy", font=("Arial", 22), showweeknumbers=False)
    calendar.config(background="lightblue", foreground="black")
    calendar.grid(padx=20, pady=20, columnspan=2)

    # Add a button to confirm the date selection
    def confirm_date():
        """"""
        selected_date = calendar.get_date()
        # print(f"Selected Date from confirm date: {selected_date}")
        # print(f"row_id: {row_id}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # need to address due_date but for now will be left unchanged
            cursor.execute('UPDATE tasks SET due_date = ? WHERE id = ?', (date_for_saving(selected_date), row_id))
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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT detail FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def existing_entry_update(modal_text, root, scroller, row_id, modal, hide_state_dict):
    if not modal_text:
        # print("Text box empty - deleting")
        delete_entry(row_id, root, scroller, modal, hide_state_dict)
    # print(f"Modal text print: {modal_text}")
    # print(f"Exisitng entry, ROW_ID: {row_id}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # need to address due_date but for now will be left unchanged
    cursor.execute('UPDATE tasks SET detail = ? WHERE id = ?', (modal_text, row_id))
    conn.commit()
    conn.close()
    modal.destroy()
    renderlist.render_list(root, scroller, hide_state_dict)

# def new_entry_save(modal_text, root, scroller, modal):
#     print("New entry save")
#     conn = sqlite3.connect("db_path")
#     cursor = conn.cursor()
#     formatted_date = todays_date_formatted(datetime.now())
#     due_date = formatted_date
#     cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, formatted_date, 0, due_date))
#     new_task_id = cursor.lastrowid
#     conn.commit()
#     conn.close()
#     modal.destroy()
#     renderlist.render_list(root, scroller)

def open_modal(root, scroller, row_id, due_date, hide_state_dict):
    """ open modal creates a modal text input window to accept
        data from the user that will be saved into the database.
        It includes the buttons and date picker required to
        make the modal functional."""
    
    # Get existing text or initialize an empty string
    details_text = get_row_text(row_id) if row_id is not None else ""

    # Create the modal window
    modal = tk.Toplevel(root)
    modal.title("Task Detail")
    modal.geometry("500x400")

    # Position modal relative to the main window
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    modal_width = 500
    modal_height = 400

    position_right = root_x + (root_width // 2) - (modal_width // 2)
    position_down = root_y + (root_height // 2) - (modal_height // 2)

    modal.geometry(f"{modal_width}x{modal_height}+{position_right}+{position_down}")

    # Bind events
    modal.bind("<Control-s>", lambda event: existing_entry_update(
        modal_text.get('1.0', 'end').strip(), root, scroller, row_id, modal, hide_state_dict))
    modal.bind("<Escape>", lambda event: on_close(details_text, hide_state_dict))
    modal.focus_set()

    # Configure grid
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure((0, 1, 2), weight=1)

    # Create a text input area
    modal_text = tk.Text(modal, height=12, width=35, font=("Roboto", 16), wrap="word")
    modal_text.grid(row=0, column=0, columnspan=3, padx=15, pady=15, sticky="nsew")
    scrollbar = tk.Scrollbar(modal, command=modal_text.yview)
    scrollbar.grid(row=0, column=3, sticky="ns")
    modal_text.config(yscrollcommand=scrollbar.set)

    if details_text:
        modal_text.insert("1.0", details_text)
        modal_text.mark_set("insert", "end")
        modal_text.focus_set()
        modal_text.see("insert")

    # Add buttons
    save_btn = ttk.Button(modal, text="Save", style="ListButton.TButton", command=lambda: existing_entry_update(
        modal_text.get('1.0', 'end').strip(), root, scroller, row_id, modal, hide_state_dict))
    save_btn.grid(row=1, column=0, padx=20, pady=20)

    date_label = ttk.Button(modal, text=f"{date_for_display(due_date)}", style="ListButton.TButton", command=lambda: date_picker(modal, date_label, row_id))
    date_label.grid(row=1, column=1, padx=20, pady=20)

    delete_button = ttk.Button(modal, text="Delete", style="ListButton.TButton", command=lambda: delete_entry(row_id, root, scroller, modal, sort_order_dict, "standard"))
    delete_button.grid(row=1, column=2, padx=20, pady=20)

    # On close handling
    def on_close(details_text, hide_state_dict):
        if details_text == '':
            delete_entry(row_id, root, scroller, modal, hide_state_dict)
        modal.destroy()

    modal.protocol("WM_DELETE_WINDOW", lambda: on_close(details_text, hide_state_dict))
    modal.grab_set()


    
def date_label_colour(due_date_str):
    """Function to determine the colour coding of the data labels
       > 5 days to due date colour is green
       3, 4 or 5 days colour is orange
       <3 days is red"""
    
    # Convert due_date_str (string) into a datetime object and then get the date part
    due_date = datetime.strptime(due_date_str, "%Y/%m/%d").date()  # Update format to %Y/%m/%d for yyyy/mm/dd
    today = date.today()  # Get today's date
    
    # Calculate the difference in days
    days_diff = (due_date - today).days
    
    # Color coding based on the days difference
    if days_diff < 3:  # Past due
        return "#e2738c"
    elif 0 <= days_diff <= 5:  # Due today or within 3 days
        return "#f6b26b"
    else:  # Due in more than 3 days
        return "#43aa8b"
    
def create_new_record(root, scroller, hide_state_dict):
    print("create new")
    modal_text=''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    due_date = todays_date_formatted(datetime.today())
    creation_date = due_date
    cursor.execute('INSERT INTO tasks (detail, creation_date, complete, due_date) VALUES (?, ?, ?, ?)', (modal_text, creation_date, 0, due_date))
    conn.commit()
    new_task_id = cursor.lastrowid
    # print(f"last row: {new_task_id}")
    conn.close()
    open_modal(root, scroller, new_task_id, due_date, hide_state_dict)
    
def delete_entry(row_id, root, scroller, modal, hide_state_dict, sort_order=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE id = ?"
    cursor.execute(query, (row_id,))
    conn.commit()
    conn.close()
    modal.destroy()
    refresh_list(root,scroller, hide_state_dict)
    
def hide_complete(root, scroller, hide_state_dict):
    print(f"{hide_state_dict}")
    # print(f"hide complete called. show is: {show}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if(hide_state_dict["hide_state"] == 1):
        query = "SELECT * FROM tasks WHERE complete = 1 ORDER BY creation_date ASC"
        hide_state_dict["hide_state"] = 0
        print(f"Hide complete if Contents: {hide_state_dict} TYPE: {type(hide_state_dict)}")
    else:
        query = "SELECT * FROM tasks WHERE complete = 0 ORDER BY creation_date ASC"
        hide_state_dict["hide_state"] = 1
        print(f"Hide complete else : {hide_state_dict} TYPE: {type(hide_state_dict)}")
    cursor.execute(query)
    
    # print("query processed")
    renderlist.render_list(root, scroller, hide_state_dict, cursor)
    conn.close()
    
def toggle_fill(event, lbl, style, row_id):
    """Toggle the fill of the label to indicate done and update the DB."""
    # print("toggle fill clicked")
    # print(f"row_id: {row_id}")
    
    # Toggle the style of the label
    if lbl.cget("text") == "":
        lbl.configure(text="\u2714", padding=(17, 15))
    else:
        lbl.configure(text="", padding=(24,15))
        
    # current_style = lbl.cget("style")
    # lbl.configure(text="\u2713", padding=(17, 15))
    # new_style = "Toggled.TLabel" if current_style == "Default.TLabel" else "Default.TLabel"
    # lbl.configure(style=new_style)

    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
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
        
def sort_list(root, scroller, hide_state_dict):
    print("Sort called")
    hide_state_dict["hide_state"] = 1
    print(f"Sort list: {hide_state_dict} TYPE: {type(hide_state_dict)}")
    current_state = sort_order_toggle(0)
    print(f"current_state: {current_state}")
    # print(f"sort called with: {sort_order}")
    if current_state == "standard":
        current_state = sort_order_toggle(1)
        # print(f" (IF) sort order changed to: {current_state}")
    elif current_state == "due_date":
        current_state = sort_order_toggle(1)
        # print(f"(ELIF) sort order changed to: {current_state}")
    
    # Call render_list with updated sort_order
    renderlist.render_list(root, scroller, hide_state_dict)

def refresh_list(root, scroller, hide_state_dict):
    print(f"Top of refresh list: {hide_state_dict} TYPE: {type(hide_state_dict)}")
    # print(f"REFRESH called with {sort_state.sort_order_toggle(0)}")
    renderlist.render_list(root, scroller, hide_state_dict)
    print(f"Contents: {hide_state_dict} TYPE: {type(hide_state_dict)}")
    hide_state_dict["hide_state"] = 0
    sort_order_dict["sort_order"] = 'standard'
    hide_complete(root, scroller, hide_state_dict)