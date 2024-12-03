import tkinter as tk
from tkinter import ttk
import sys


root = tk.Tk()
root.geometry("300x200")  # Set an initial window size

# Create the canvas and scrollbar
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")  # Allow canvas to expand
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")  # Attach scrollbar to the right

# Create a frame inside the canvas
canvas_frame = tk.Frame(canvas, borderwidth=2, relief="solid")
scrollable_window = canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Configure canvas scrolling
canvas.configure(yscrollcommand=scrollbar.set)

# Adjust scroll region and dynamic width of the frame
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(scrollable_window, width=canvas.winfo_width())

canvas.bind("<Configure>", lambda event: canvas.itemconfig(scrollable_window, width=event.width))
canvas_frame.bind("<Configure>", configure_scroll_region)


# Configure canvas_frame columns to stretch
for i in range(3):  # Assuming 3 columns based on your code
    canvas_frame.grid_columnconfigure(i, weight=1)  # Enable column stretching

canvas_frame.grid_columnconfigure(0, weight=0, minsize=100)
canvas_frame.grid_columnconfigure(1, weight=0, minsize=80)
canvas_frame.grid_columnconfigure(2, weight=0, minsize=130)
# Add some labels to the frame
for i in range(20):  # Add enough labels to make the frame scrollable
    for j in range(3):
        label = tk.Label(canvas_frame, text=f"Label {i + 1}", borderwidth=1, relief="solid")
        label.grid(row=i, column=j % 3, padx=5, pady=5, sticky="ew")  # Expand labels horizontally
    canvas_frame.grid_rowconfigure(i, minsize=label.winfo_reqheight())
# Configure root grid to allow resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
