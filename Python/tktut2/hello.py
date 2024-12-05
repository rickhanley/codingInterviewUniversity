import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text="Hello World!")
label.grid(column=0)

label2 = tk.Label(root, text="row 0 column 0", borderwidth=2, relief="solid", padx=10, pady=10)
label2.grid(column=1, padx=10)

label3 = tk.Label(root, text="row 1 column 2")
label3.grid(row = 1, column=2)

root.grid_columnconfigure(0, minsize=100)
root.grid_columnconfigure(1, minsize=150, weight=1)
root.grid_columnconfigure(2, minsize=200, weight=2)
root.rowconfigure(0,pad=40)
root.rowconfigure(1,pad=20)
root.rowconfigure(2,pad=10)
root.mainloop()

