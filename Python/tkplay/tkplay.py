import tkinter as tk

root = tk.Tk()

root.geometry("400x400")

myFrame = tk.Frame(root)

my_label = tk.Label(myFrame, text="Rick")
my_label.grid()


myFrame.grid()

root.mainloop()
