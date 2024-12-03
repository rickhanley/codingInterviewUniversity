import tkinter as tk

root = tk.Tk()

label_frame = tk.Frame(root)
label_frame.grid()

label1 = tk.Label(label_frame, text="lable_1")
label1.grid(column=0, row=0)
label2 = tk.Label(label_frame, text="lable_2")
label2.grid(column=1, row=0)

canvas = tk.Canvas(root)
canvas.grid()

canvas_frame = tk.Frame(canvas)
canvas_frame.grid()

label3 = tk.Label(canvas_frame, text="lable_3")
label3.grid(column=0, row=0)
label4 = tk.Label(canvas_frame, text="lable_4")
label4.grid(column=1, row=0)


root.mainloop()
