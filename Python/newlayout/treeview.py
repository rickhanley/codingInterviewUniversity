import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.geometry("700x400")

# Frame for the Treeview and scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create a Treeview widget
columns = ("Task", "Due Date", "Status")
tree = ttk.Treeview(frame, columns=columns, show="headings")

# Define headings and column properties
tree.heading("Task", text="Task")
tree.column("Task", anchor="w", width=200)
tree.heading("Due Date", text="Due Date")
tree.column("Due Date", anchor="center", width=100)
tree.heading("Status", text="Status")
tree.column("Status", anchor="center", width=100)

# Add some sample data
sample_data = [
    ("Complete project proposal", "2024-12-15", "Pending"),
    ("Prepare meeting agenda", "2024-12-10", "Done"),
    ("Submit grant application", "2024-12-20", "In Progress"),
]

for task, due_date, status in sample_data:
    tree.insert("", "end", values=(task, due_date, status))

# Add Treeview to the frame
tree.pack(side="left", fill="both", expand=True)

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

root.mainloop()
