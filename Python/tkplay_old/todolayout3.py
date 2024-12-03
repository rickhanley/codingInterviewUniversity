import tkinter as tk
from tkinter import ttk
from ctypes import windll

# DPI Awareness
try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def create_new_record():
    pass

def hide_complete():
    pass

def sort_list():
    pass

# Main window setup
root = tk.Tk()
root.title("QuickTask QT")
root.geometry("700x1200")

# Configure root grid to make everything resizable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=1)

# Style configuration
style = ttk.Style()
style.configure("RoundedButton.TButton",
                padding=(20,20),
                relief="flat",
                foreground="BLACK",
                font=("Arial", 12, "bold"))

# Top label
top_label = ttk.Label(root, text="QuickTask QT", font=('Arial', 20, "bold"))
top_label.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

# Button frame
button_frame = tk.Frame(root, 
                        highlightbackground="#bbbbbb",  
                        highlightthickness=1)
button_frame.grid(row=1, column=0, pady=15, padx=15, sticky="ew")

# Ensure buttons expand equally
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

# Buttons
new_btn = ttk.Button(button_frame, text="New", style="RoundedButton.TButton", command=create_new_record)
new_btn.grid(row=0, column=0, padx=5, pady=15, sticky="ew")

hide_btn = ttk.Button(button_frame, text="Show / Hide", style="RoundedButton.TButton", command=hide_complete)
hide_btn.grid(row=0, column=1, padx=5, pady=15, sticky="ew")

sort_btn = ttk.Button(button_frame, text="Sort", style="RoundedButton.TButton", command=sort_list)
sort_btn.grid(row=0, column=2, padx=5, pady=15, sticky="ew")

# Create the canvas and scrollbar
canvas = tk.Canvas(root, highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

# Create a frame inside the canvas
scroller = tk.Frame(canvas)

# Configure the canvas
canvas_window = canvas.create_window((0, 0), window=scroller, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Configure scroller columns
# Column 0 and 2 are fixed width, column 1 is flexible
scroller.grid_columnconfigure(0, weight=0, minsize=10)    # Checkmark column - fixed width
scroller.grid_columnconfigure(1, weight=1)                # Description column - flexible
scroller.grid_columnconfigure(2, weight=0, minsize=10)   # Due date column - fixed width

# Header labels
headers = [f"{u'\u2713'}", "Task", "Due By"]
for col, header in enumerate(headers):
    label = ttk.Label(scroller, text=header, 
              font=("Arial", 12, "bold"), 
              borderwidth=1, 
              width=3 if col in [0, 2] else 20,  # Narrow width for first and last columns
              relief="groove", 
              padding=(15, 15))
    
    # Set specific width for first and last columns
    if col in [0, 2]:
        label.configure(width=6 if col == 0 else 15)
    
    label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

# Add sample tasks
for i in range(1, 12):
    # Checkmark column
    ttk.Label(scroller, text="", 
              borderwidth=2, relief="groove", 
              width=10,
              padding=(15, 15)).grid(row=i, column=0, padx=5, pady=5, sticky="nsew")
    
    # Task description column
    ttk.Label(scroller, text=f"Top task heading {i}", 
              borderwidth=2, relief="groove", 
              padding=(15, 15)).grid(row=i, column=1, padx=5, pady=5, sticky="nsew")
    
    # Due date column
    ttk.Label(scroller, text=f"{i}/11/24", 
              borderwidth=2, relief="groove", 
              width=15,
              padding=(15, 15)).grid(row=i, column=2, padx=5, pady=5, sticky="nsew")

# Grid the canvas and scrollbar
canvas.grid(row=3, column=0, sticky="nsew", padx=15, pady=15)
scrollbar.grid(row=3, column=1, sticky="ns")

# Update scroll region and canvas size
def on_configure(event):
    # Update scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Resize canvas window to match canvas width
    canvas_width = canvas.winfo_width()
    canvas.itemconfig(canvas_window, width=canvas_width)

# Bind the configure event
scroller.bind("<Configure>", on_configure)

# Bind canvas resize event
def on_canvas_resize(event):
    canvas_width = event.width
    canvas.itemconfig(canvas_window, width=canvas_width)

canvas.bind("<Configure>", on_canvas_resize)

root.mainloop()