import tkinter as tk
from tkinter import ttk
from ctypes import windll

def create_new_record():
    pass
def hide_complete():
    pass
def sort_list():
    pass

root = tk.Tk()
root.geometry("700x1200")

canvas = tk.Canvas(root, borderwidth=3, relief="solid")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroller = ttk.Frame(canvas)
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_window = canvas.create_window((0,0), window=scroller, anchor="nw")

def configure_scroll_region(event):
    # Update the scroll region based on the content size
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the configure event to update scroll region when content is resized
scroller.bind("<Configure>", configure_scroll_region)

# Grid the canvas
canvas.grid(row=3, column=0, columnspan=3, pady=0, padx=0, sticky="nsew")

# Grid the scrollbar
scrollbar.grid(row=2, column=3, sticky="ns")

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=0)  # Make sure the row for canvas is resizable
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

top_label.grid(row=0, column=0, columnspan=1, padx=0, sticky="ew")

button_frame = tk.Frame(root, 
                        highlightbackground="#bbbbbb",  # Border color
                        highlightthickness=1,        # Border thickness
                        highlightcolor="#999999")
button_frame.grid(row=1, column=0, columnspan=3, padx=0, sticky="ew")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

new_btn = ttk.Button(button_frame, text="New", style="RoundedButton.TButton", command=create_new_record)
new_btn.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

hide_btn = ttk.Button(button_frame, text="Show / Hide", style="RoundedButton.TButton", command=hide_complete)
hide_btn.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

sort_btn = ttk.Button(button_frame, text="Sort", style="RoundedButton.TButton", command=sort_list)
sort_btn.grid(row=0, column=2, padx=0, pady=0, sticky="ew")



root.mainloop()