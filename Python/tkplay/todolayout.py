import tkinter as tk
from tkinter import ttk
from ctypes import windll
import datetime

windll.shcore.SetProcessDpiAwareness(1)

def create_new_record():
    pass
def hide_complete():
    pass
def sort_list():
    pass

root = tk.Tk()
root.geometry("700x1200")

# Create the canvas and scrollbar
canvas = tk.Canvas(root, borderwidth=2, relief="solid")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroller = tk.Frame(canvas, borderwidth=2, relief="solid")
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
canvas.grid_columnconfigure(0, weight=1)
canvas.grid(row=3, column=0, columnspan=3, pady=15, padx=15, sticky="nsew")

# Grid the scrollbar
scrollbar.grid(row=3, column=3, sticky="ns")

# Configure the root's grid
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=1)  # Make sure the row for canvas is resizable
root.grid_columnconfigure(0, weight=1)  # Make sure the first column (canvas) is resizable
root.grid_columnconfigure(3, weight=0)  # Column for scrollbar doesn't need to be resizable

style = ttk.Style()
# Define a custom style for the button
style.configure("RoundedButton.TButton",
                padding=(20,20),
                relief="flat",
                foreground="BLACK",
                font=("Arial", 12, "bold"))

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

new_btn = ttk.Button(button_frame, text="New", style="RoundedButton.TButton", command=create_new_record)
new_btn.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

hide_btn = ttk.Button(button_frame, text="Show / Hide", style="RoundedButton.TButton", command=hide_complete)
hide_btn.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

sort_btn = ttk.Button(button_frame, text="Sort", style="RoundedButton.TButton", command=sort_list)
sort_btn.grid(row=0, column=2, padx=15, pady=15, sticky="ew")


label_frame = tk.Frame(root)
label_frame.grid(row=2, column=0, columnspan=3, padx=15, pady=15, sticky="ew")

label_frame.grid_columnconfigure(0, minsize=30)  # Fixed width for checkmark column
label_frame.grid_columnconfigure(1, weight=1)   # Scalable task column
label_frame.grid_columnconfigure(2, minsize=30)

done_label = ttk.Label(label_frame, text=f"{u'\u2713'}", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
done_label.grid(row=1, column=0, padx=15, sticky="ew")
description_label = ttk.Label(label_frame, text="Task", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
description_label.grid(row=1, column=1, padx=15, sticky="ew")
due_by_label = ttk.Label(label_frame, text="Due By", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
due_by_label.grid(row=1, column=2, padx=15, sticky="ew")

# Configure the scroller frame's grid to allow stretching
scroller.grid_rowconfigure(0, weight=1)
scroller.grid_columnconfigure(0, weight=1)  # Ensure column 0 expands
scroller.grid_columnconfigure(1, weight=1)  # Ensure column 1 expands
scroller.grid_columnconfigure(2, weight=1)  # Ensure column 2 expands
# canvas.grid_rowconfigure(3, weight=1)  # Ensure row 3 (canvas) stretches
# canvas.grid_columnconfigure(0, weight=1)  # Ensure column 0 (canvas) stretches horizontally

# Add labels to the scroller
label1 = tk.Label(scroller, text="      ", borderwidth=2, relief="groove", padx=15, pady=15)
label1.grid(row=0, column=10, padx=15, pady=15, sticky="ew")

label2 = tk.Label(scroller, text="      ", borderwidth=2, relief="groove", padx=15, pady=15)
label2.grid(row=1, column=1, padx=15, pady=15, sticky="ew")

label3 = tk.Label(scroller, text="      ", borderwidth=2, relief="groove", padx=15, pady=15)
label3.grid(row=2, column=2, padx=15, pady=15, sticky="ew")

root.mainloop()
