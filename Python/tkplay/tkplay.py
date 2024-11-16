import tkinter as tk

root = tk.Tk()

root.geometry("400x400")


for i in range(10):
    my_label = tk.Label(root, text='Rick', relief='solid', borderwidth=2)
    my_entry = tk.Entry(root)
    my_label.grid(column=0, sticky='w')
    my_entry.grid(column=1, row=i, sticky='w')
   
# Create a label
# my_label = tk.Label(root, text='Rick')

# Place the label in the grid at column 0, aligned to the right
# my_label.grid(sticky='e')

# Configure the column to stretch across the entire window
root.grid_columnconfigure(0, weight=1, uniform="equal")
root.grid_columnconfigure(1, weight=5, uniform="equal")
root.grid_columnconfigure(2, weight=2, uniform="equal")

new_label = tk.Label(text="column 3", relief='solid', borderwidth=2)
new_label.grid(column=2)

root.mainloop()
