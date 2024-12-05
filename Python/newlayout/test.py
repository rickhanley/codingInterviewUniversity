import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
cal = Calendar(root, selectmode='day', year=2024, month=12, day=5)
cal.pack(pady=20)
root.mainloop()