import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World!")
button = tk.Button(root, text="Button me up right nice")

label.pack()
button.pack()

root.mainloop()