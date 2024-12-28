import tkinter as tk
from tkinter import ttk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def on_label_click(event, idx):
    contents = label.cget("text")
    print(contents, idx)
    
root = tk.Tk()
root.geometry("400x400")

for i in range(10):
    label = ttk.Label(text="Hello", border=55, relief ="solid", padding=(10, 10))
    label.grid(column=i, row=0, padx=10, pady=10)
    label.bind("<Button-1>", lambda event, idx=i: on_label_click(event, idx))
# label2 = ttk.Label(text="Hello", border=55, relief ="solid", padding=(10, 10))
# label2.grid(column=1, row=0, padx=10, pady=10)




    

root.mainloop()
