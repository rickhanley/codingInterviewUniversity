# imports
import tkinter as tk
from tkinter import ttk
from ctypes import windll
from PIL import Image, ImageTk
import helpers
import sqlite3

windll.shcore.SetProcessDpiAwareness(1) # correct fuzzy rendering of app

# test data for date fields
dates = ['26/11/24', '18/12/24', '29/11/24', '03/12/24', '12/02/25']
row_id_map = {}
# print(helpers.date_label_colour("15/12/24"))

root = tk.Tk() # main tkinter app window
root.geometry("600x1000")
root.minsize(width=600, height=1000)

# Create the canvas and scrollbar
canvas = tk.Canvas(root)

spacer = tk.Frame(canvas, height=20, borderwidth=2, relief="solid")  # 20px padding
spacer.grid()


scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroller = tk.Frame(canvas, padx=15, pady=15, borderwidth=2, relief="solid")
scroller.grid(column=0, pady=15, padx=15, sticky="ew")

canvas.configure(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 0))
scrollable_window = canvas.create_window((0, 0), window=scroller, anchor="nw")

def configure_scroll_region(event):
    # Update the scroll region based on the content size
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(scrollable_window, width=canvas.winfo_width())

canvas.bind("<Configure>", lambda event: canvas.itemconfig(scrollable_window, width=event.width))
# Bind the configure event to update scroll region when content is resized
scroller.bind("<Configure>", configure_scroll_region)

# Grid the canvas
canvas.grid_rowconfigure(0, weight=1)
# for i in range(3):
#     canvas.grid_columnconfigure(i, weight=1)
canvas.grid(row=3, column=0, sticky="nsew")

scroller.grid_columnconfigure(0, weight=0, minsize=1)
scroller.grid_columnconfigure(1, weight = 1)
scroller.grid_columnconfigure(2, weight=0, minsize=75)

# Grid the scrollbar
scrollbar.grid(row=3, column=3, sticky="nsew")

# Configure the root's grid
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=1)  # Make sure the row for canvas is resizable
root.grid_columnconfigure(0, weight=1)  # Make sure the first column (canvas) is resizable
root.grid_columnconfigure(3, weight=0)  # Column for scrollbar doesn't need to be resizable

style = ttk.Style()
small_style = ttk.Style()
# Define a custom style for the button
style.configure("RoundedButton.TButton",
                padding=(20,20),
                relief="flat",
                foreground="BLACK",
                font=("Arial", 20, "bold"))

small_style.configure(
    "SmallButton.TButton",
    padding=(3, 22),  # Adjust padding for the desired this controls the button size in effect
    font=("Arial", 4),  # Smaller font for compact buttons, also controls button size
    relief="flat",
)

# Top label
top_label = ttk.Label(root, text="QuickTask QT", font=('Arial', 20, "bold"))
top_label.grid(row=0, column=0, columnspan=1, padx=15, pady=15, sticky="ew")

# Button frame
button_frame = tk.Frame(root, 
                        highlightbackground="#bbbbbb",  # Border color
                        highlightthickness=1,        # Border thickness
                        highlightcolor="#999999")
button_frame.grid(row=1, column=0, columnspan=3, pady=15, padx=15, sticky="ew")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)


button_gif = tk.PhotoImage(file="buttons/plus-square.png")
new_btn = ttk.Button(button_frame, image=button_gif, style="RoundedButton.TButton", command=lambda: helpers.create_new_record(root))
new_btn.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

eye_gif = tk.PhotoImage(file="buttons/funnel.png")
hide_btn = ttk.Button(button_frame, image=eye_gif, style="RoundedButton.TButton", command=helpers.hide_complete)
hide_btn.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

sort_gif = tk.PhotoImage(file="buttons/arrows-down-up.png")
sort_btn = ttk.Button(button_frame, image=sort_gif, style="RoundedButton.TButton", command=helpers.sort_list)
sort_btn.grid(row=0, column=2, padx=15, pady=15, sticky="ew")

refresh_gif = tk.PhotoImage(file="buttons/arrows-clockwise.png")
refresh_btn = ttk.Button(button_frame, image=refresh_gif, style="RoundedButton.TButton", command=helpers.refresh_list)
refresh_btn.grid(row=0, column=3, padx=15, pady=15, sticky="ew")


label_frame = tk.Frame(root, padx=15, pady=15)
label_frame.grid(row=2, column=0, columnspan=3, padx=15, sticky="ew")

label_frame.grid_columnconfigure(0, minsize=30)  # Fixed width for checkmark column
label_frame.grid_columnconfigure(1, weight=1)   # Scalable task column
label_frame.grid_columnconfigure(2, minsize=30)

done_label = ttk.Label(label_frame, text=f"{u'\u2713'}", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
done_label.grid(row=1, column=0, sticky="ew")
description_label = ttk.Label(label_frame, text="Task", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15), anchor="center")
description_label.grid(row=1, column=1, padx=15, sticky="ew")
due_by_label = ttk.Label(label_frame, text="Due By", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
due_by_label.grid(row=1, column=2, sticky="ew")

# Configure the scroller frame's grid to allow stretching

# canvas.grid_rowconfigure(3, weight=1)  # Ensure row 3 (canvas) stretches
# canvas.grid_columnconfigure(0, weight=1)  # Ensure column 0 (canvas) stretches horizontally

# Add labels to the scroller

def update_wrap(event, label, padding_x):
    # Dynamically adjust wraplength based on label width and padding
    label.configure(wraplength=label.winfo_width() - padding_x * 2)
    
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
        label2.bind("<Button-1>", lambda event: helpers.open_modal(root, row_id_map[label2]))
        
        label3 = tk.Label(scroller, text=f"{due_date}", borderwidth=2, relief="groove", padx=20, pady=15, background=f"{helpers.date_label_colour(due_date)}")
        label3.grid(row=i, column=2, padx=15, pady=15, sticky="ew")

render_list()
root.mainloop()
