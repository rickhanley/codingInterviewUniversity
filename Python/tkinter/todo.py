import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from tkinter import ttk
from ctypes import windll
from PIL import Image, ImageTk
import datetime# Make sure to install Pillow for image handling

# Set DPI awareness for better display on high-DPI screens
windll.shcore.SetProcessDpiAwareness(1)

today = datetime.datetime.now()

# ----------------------- Modal setup ----------------------------------

def open_modal(heading_id):
    modal = tk.Toplevel(window)
    modal.title("Subtasks")
    modal.geometry("400x300")

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM headings JOIN subtasks ON subtasks.heading_id = headings.id WHERE headings.id =  ?", (heading_id,))
    results_set = cursor.fetchall()
    
    if results_set:
        # heading = tk.Label(modal, text=f"{}")
        entry = tk.Entry(modal)
        entry.insert(0, results_set[0][1])
        entry.pack(pady=5)
        
        # heading.pack(pady=5)
        subtask_list = [row[5] for row in results_set]  # Collect all subtask names
        for index, subtask in enumerate(subtask_list):
            label = tk.Label(modal, text=f"Step {index + 1}")
            label.pack(pady=5)
            entry = tk.Entry(modal)
            entry.insert(0, subtask)
            entry.pack(pady=5)
        
        plus_button = tk.Button(modal, text="+", font=("Helvetica", 16, "bold"), padx=20, pady=2)
        plus_button.pack(pady=10)
        save_button = tk.Button(modal, text="Save", command=lambda: save_subtasks(results_set, modal))
        save_button.pack(pady=10)

        conn.close()
                
def save_subtasks(results_set, modal):
    # Placeholder for saving logic
    for subtask in results_set:
        print(f"Saving subtask ID: {subtask[0]} with new value: [Text Field Value Here]")
    modal.destroy()  # Close the modal after saving

# Create the main window
window = tk.Tk()
window.geometry("800x1000")
font_style = tkFont.Font(family="Arial", size=12, weight="normal")
window.configure(bg="#000000")

# Create a canvas with a scrollbar
canvas = tk.Canvas(window, bg="white")
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the scrollbar and canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to hold the labels
frame = tk.Frame(canvas, bg="#bbbbbb", pady=20)
canvas.create_window((20, 20), window=frame, anchor="nw")

# Function to update scroll region when frame changes
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", update_scrollregion)

# ------------------- Render the task list ---------------------
def render_tasks():
# Connect to the SQLite database and fetch headings
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM headings")
    rows = cursor.fetchall()
    
    top_frame = tk.Frame(frame, background="white")
    top_frame.pack(pady=5)

    # ------------------------------- BUTTON BAR ------------------------------
    addNewLabel = tk.Label(top_frame, text="New task", pady=5, font=font_style, height=1, width="12", background="#b9e1fa")
    refreshLabel = tk.Label(top_frame, text="Refresh", pady=5, font=font_style, height=1, width="12", background="#B4F0C3")
    hideLabel = tk.Label(top_frame, text="Hide", pady=5, font=font_style, height=1, width="12", background="#dddddd")
    addNewLabel.pack(side="left", pady=20, padx=15)
    refreshLabel.pack(side="left", pady=20, padx=15)
    hideLabel.pack(side="left", pady=20, padx=15)
    

    unchecked_img = Image.open("emptycheck.png").resize((50, 50))  # Resize image
    checked_img = Image.open("greencheck.png").resize((50, 50))      # Resize image

    unchecked_photo = ImageTk.PhotoImage(unchecked_img)
    checked_photo = ImageTk.PhotoImage(checked_img)

    date_colour = '#000000'

    # Create labels for each heading and bind the click event
    for index, data in enumerate(rows):
        label_text = data[1]
        label_text = label_text[:60] + "..."  # Truncate and add ellipsis
        due_date_str = data[3]  # Assuming data[3] is the due date
        due_date = datetime.datetime.strptime(due_date_str, '%d-%m-%Y')
        print("Due date: ", due_date)
        difference = (due_date - today).days
        
        if difference > 5:
            date_colour = "#00A389"
        elif difference > 3:
            date_colour = "#FF6A6A"
        elif difference == 0 or difference < 3:
            date_colour = "#FF6A6A"
        # Create a frame for each label
        label_frame = tk.Frame(frame, background="white")
        label_frame.pack(pady=10, padx=20)

        # Checkbox variable (keep it inside the loop to have separate state)
        check_var = tk.BooleanVar()  # Variable to track the checkbox state
        
        # Define the toggle function that accesses the specific check_var
        def toggle_checkbox(var, checkbox):
            # Toggle the checkbox state
            var.set(not var.get())
            checkbox.config(image=checked_photo if var.get() else unchecked_photo)
            
        # def hide_toggle():

        # Checkbox (Image-based checkbox)
        checkbox = tk.Label(label_frame, image=unchecked_photo, background="white", cursor="hand2")
        
        # Bind the toggle function using the specific check_var
        checkbox.bind("<Button-1>", lambda e, var=check_var, cb=checkbox: toggle_checkbox(var, cb))
        checkbox.pack(side="left", padx=10)  # Add horizontal padding

        # Main text label
        main_label = tk.Label(label_frame, text=label_text, font=font_style,
                            wraplength=450, padx=20, pady=20, background="white", justify="left")
        main_label.pack(side="left")  # Pack to the left

        # Due date label
        due_date_label = tk.Label(label_frame, text=f"{due_date.date()}", font=font_style,
                                background="white", fg=f"{date_colour}")
        due_date_label.pack(side="right", padx=20)  # Pack to the right

        # Bind the click event to the main label
        main_label.bind("<Button-1>", lambda e, heading_id=data[0]: open_modal(heading_id))

        # Optionally, you can track the checkbox state by using check_var.get()
    conn.close()


render_tasks()
window.mainloop()
