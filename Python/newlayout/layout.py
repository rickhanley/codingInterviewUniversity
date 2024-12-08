import tkinter as tk
from tkinter import ttk
import renderlist
from ctypes import windll
import helpers
windll.shcore.SetProcessDpiAwareness(1)


root = tk.Tk()
root.geometry("720x1200")
root.minsize(720, 1200)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style()
small_style = ttk.Style()

style.configure("RoundedButton.TButton",
                padding=(20,20),
                relief="flat",
                foreground="BLACK",
                font=("Arial", 20, "bold"))

small_style.configure("SmallButton.TButton",
                padding=(3, 22),  # Adjust padding for the desired this controls the button size in effect
                font=("Arial", 4),  # Smaller font for compact buttons, also controls button size
                relief="flat")



heading = ttk.Label(root, text="QuickTask QT", font=('Arial', 20, "bold"))
heading.grid(row=0)

button_frame = tk.Frame(root, borderwidth=1, relief="solid")
button_frame.grid(column=0, row=1, sticky="ew", padx=10, pady=10)

button_gif = tk.PhotoImage(file="buttons/plus-square.png")
new_btn = ttk.Button(button_frame, image=button_gif, style="RoundedButton.TButton", command= lambda: helpers.create_new_record(root, scroller))
new_btn.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

eye_gif = tk.PhotoImage(file="buttons/funnel.png")
hide_btn = ttk.Button(button_frame, image=eye_gif, style="RoundedButton.TButton")
hide_btn.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

sort_gif = tk.PhotoImage(file="buttons/arrows-down-up.png")
sort_btn = ttk.Button(button_frame, image=sort_gif, style="RoundedButton.TButton")
sort_btn.grid(row=0, column=2, padx=15, pady=15, sticky="ew")

refresh_gif = tk.PhotoImage(file="buttons/arrows-clockwise.png")
refresh_btn = ttk.Button(button_frame, image=refresh_gif, style="RoundedButton.TButton", command= lambda: helpers.refresh_list(root, scroller))
refresh_btn.grid(row=0, column=3, padx=15, pady=15, sticky="ew")

button_frame.grid_columnconfigure(0, weight=1)

label_frame = tk.Frame(root, borderwidth=1, relief="solid", padx=52, pady=15)
label_frame.grid(column=0, row=2, sticky="ew")

done_label = ttk.Label(label_frame, text=f"{u'\u2713'}", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
done_label.grid(row=0, column=0, sticky="ew", padx=2)
description_label = ttk.Label(label_frame, text="Task", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15), anchor="center")
description_label.grid(row=0, column=1, padx=15, sticky="ew")
due_by_label = ttk.Label(label_frame, text="Due By", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
due_by_label.grid(row=0, column=2, sticky="ew")

label_frame.grid_columnconfigure(0, minsize=30)  # Fixed width for checkmark column
label_frame.grid_columnconfigure(1, minsize=400, weight=1)   # Scalable task column
label_frame.grid_columnconfigure(2, weight=0, minsize=65)

content_frame = tk.Frame(root)
content_frame.grid(column=0, row=3, sticky="nsew", padx=20, pady=10)
root.grid_rowconfigure(3, weight=1)  # Allow content_frame to expand vertically

canvas = tk.Canvas(content_frame)
canvas.grid(row=0, column=0, sticky="nsew")  # Make canvas fill the content_frame

content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)# Place scrollbar next to canvas

scroller = tk.Frame(canvas, padx=15, pady=15)
scrollable_window = canvas.create_window((0, 0), window=scroller, anchor="nw")

# This function adjusts the scroll region when content inside scroller changes size
def configure_scroll_region(event):
    bbox = canvas.bbox("all")
    print(f"Scroll region bbox: {bbox}")  # Debug print
    if bbox:
        canvas.configure(scrollregion=bbox)  # Update the scrollregion
  # Update the scrollregion to match the scroller's size

canvas.bind("<Configure>", lambda event: canvas.itemconfig(scrollable_window, width=event.width))  # Ensure the window width follows canvas width
scroller.bind("<Configure>", configure_scroll_region)  # Update scrollregion whenever scroller's size changes

# Configure columns in the scroller (for content layout inside the scroller)
scroller.grid_columnconfigure(0, minsize=30)
scroller.grid_columnconfigure(1, weight=1, minsize=400)
scroller.grid_columnconfigure(2, weight=0, minsize=75)

renderlist.render_list(root, scroller)





root.mainloop()
