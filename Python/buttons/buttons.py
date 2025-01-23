import tkinter as tk
from tkinter import ttk

root = tk.Tk()
btn = ttk.Button(width=2, text=f"{u'\u2713'}", state="disabled")
btn.grid()

root.mainloop()