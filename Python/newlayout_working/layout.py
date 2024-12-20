import tkinter as tk
from tkinter import ttk
import renderlist
from ctypes import windll
import helpers
windll.shcore.SetProcessDpiAwareness(1)


root = tk.Tk()
root.tk.call('tk', 'scaling', 1)
root.resizable(True, True)
root.geometry("681x950")
root.minsize(681, 950)
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



heading = ttk.Label(root, text="QuickTask (QT)", font=('Arial', 36, "bold"))
heading.grid(row=0, pady=(20, 0))

button_frame = tk.Frame(root, borderwidth=1, height=10)
button_frame.grid(column=0, row=1, sticky="ew", padx=36, pady=10)

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

label_frame = tk.Frame(root)
# label_frame = tk.Frame(root, borderwidth=2, relief="solid")
label_frame.grid(column=0, row=2, sticky="nsew", padx=(52, 55), pady=15)

done_label = ttk.Label(label_frame, text=f"{u'\u2713'}", font=("Arial", 16, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
done_label.grid(row=0, column=0, sticky="ew")
description_label = ttk.Label(label_frame, text="Task", font=("Arial", 16, "bold"), borderwidth=1, relief="groove", padding=(15, 15), anchor="center")
description_label.grid(row=0, column=1, padx=15, sticky="ew")
due_by_label = ttk.Label(label_frame, text="Due By", font=("Arial", 16, "bold"), borderwidth=1, relief="groove", padding=(15, 15))
due_by_label.grid(row=0, column=2, sticky="ew")

# label_frame.grid_columnconfigure(0, minsize=30)  # Fixed width for checkmark column
label_frame.grid_columnconfigure(1, minsize=430, weight=1)   # Scalable task column
# label_frame.grid_columnconfigure(2, weight=0, minsize=65)

# content_frame = tk.Frame(root, borderwidth=2, relief="solid")
content_frame = tk.Frame(root)
content_frame.grid(column=0, row=3, sticky="nsew", padx=20)
root.grid_rowconfigure(3, weight=1)  # Allow content_frame to expand vertically

canvas = tk.Canvas(content_frame)

canvas.grid(row=0, column=0, sticky="nsew")  # Make canvas fill the content_frame

content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1, minsize=402)

scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

(f"Scrollregion: {canvas.cget('scrollregion')}")
canvas.configure(yscrollcommand=scrollbar.set)# Place scrollbar next to canvas

scroller = tk.Frame(canvas, padx=15)
scroller.grid(sticky="nsew")
scrollbar.config(command=scroller.yview)

scrollable_window = canvas.create_window((0, 0), window=scroller, anchor="nw")

# This function adjusts the scroll region when content inside scroller changes size
def configure_scroll_region(event=None):
    bbox = canvas.bbox("all")  # Get the bounding box of all items in the canvas
    if bbox:
        content_height = bbox[3] - bbox[1]  # Total height of the scroller's content
        canvas_height = canvas.winfo_height()  # Visible height of the canvas

        if content_height > canvas_height:
            # Enable scrolling
            canvas.configure(scrollregion=bbox)
            scrollbar.grid()  # Ensure scrollbar is visible
        else:
            # Disable scrolling
            canvas.configure(scrollregion=(0, 0, canvas.winfo_width(), canvas_height))
            scrollbar.grid_remove()  # Hide scrollbar

  # Update the scrollregion to match the scroller's size

canvas.bind("<Configure>", lambda event: canvas.itemconfig(scrollable_window, width=event.width))  # Ensure the window width follows canvas width
scroller.bind("<Configure>", configure_scroll_region)  # Update scrollregion whenever scroller's size changes

# Configure columns in the scroller (for content layout inside the scroller)
scroller.grid_columnconfigure(0, minsize=30, weight=0)
scroller.grid_columnconfigure(1, weight=10, minsize=402)
scroller.grid_columnconfigure(2, weight=0, minsize=75)

renderlist.render_list(root, scroller)
configure_scroll_region(None)
root.update_idletasks()
root.mainloop()
