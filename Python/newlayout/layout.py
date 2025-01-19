"""Layout.py
   Deasl with the alyout of widgets in the main tk root window"""


import tkinter as tk
from tkinter import ttk
import renderlist, os, sys
from ctypes import windll
import helpers
import menu
from root_conf import root
windll.shcore.SetProcessDpiAwareness(1)

# root = tk.Tk() # root app window
root.tk.call('tk', 'scaling', 1) # set scaling for current resolution
root.resizable(True, True) # re-sizeable on x and y axis

root.geometry("681x950") # window size 
root.minsize(681, 950)
root.grid_columnconfigure(0, weight=1) # one master column for the app. Everything site within this

# fucntion to get paths for cross-platform compatibility 
def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# global dict to hold the sort order
sort_order_dict = {"sort_order": "standard"}
hide_state_dict = {"hide_state": 1}
print(f"From layout: {hide_state_dict} TYPE: {type(hide_state_dict)}")

style = ttk.Style()
small_style = ttk.Style()
list_style = ttk.Style()


# style.theme_use("clam")

style.configure("RoundedButton.TButton",
                padding=(20,20),
                relief="flat",
                foreground="BLACK",
                font=("Arial", 20, "bold"))

small_style.configure("SmallButton.TButton",
                padding=(3, 22),  # Adjust padding for the desired this controls the button size in effect
                font=("Arial", 4),  # Smaller font for compact buttons, also controls button size
                relief="flat")

list_style.configure("ListButton.TButton",
                     padding=(10,10)),


# sort_order = "standard"
top_level_frame = ttk.Frame(root, borderwidth=1)
top_level_frame.grid(sticky="ew", )

top_level_frame.grid_columnconfigure(0, weight=1)  # Make column 0 expand to take up extra space.
top_level_frame.grid_columnconfigure(1, weight=0)  # Keep column 1 as is for the button.

heading = ttk.Label(top_level_frame, text="QuickTask (QT)", font=('Arial', 36), padding=(50,0))
heading.grid(row=0, sticky="w", pady=0)

list_button_gif = tk.PhotoImage(file=get_resource_path("buttons/list.png")) # create gif
list_button = ttk.Button(top_level_frame, image=list_button_gif, style="ListButton.TButton",
                      command=lambda: menu.menu())
list_button.grid(row=0, column=1, padx=52, pady=(15,0), sticky="e")

status_frame = tk.Frame(root)
status_frame.grid(sticky="ew", row=2)
# status_label = ttk.Label(status_frame, text="Status:")
status_label = ttk.Label(status_frame, text=f"Status: ", font=("Arial", 12, "bold"), borderwidth=1, relief="groove", padding=(5, 5))
status_label.grid(row=0)


button_frame = tk.Frame(root, borderwidth=1, height=10)
button_frame.grid(column=0, row=1, sticky="ew", padx=36)

plus_button_gif = tk.PhotoImage(file=get_resource_path("buttons/plus-square.png"))
plus_btn = ttk.Button(button_frame, image=plus_button_gif, style="RoundedButton.TButton",
                      command=lambda: helpers.create_new_record(root, scroller, hide_state_dict))
plus_btn.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

funnel_gif = tk.PhotoImage(file=get_resource_path("buttons/funnel.png"))
funnel_btn = ttk.Button(button_frame, image=funnel_gif, style="RoundedButton.TButton",
                        command=lambda: helpers.hide_complete(root, scroller, hide_state_dict))
funnel_btn.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

sort_gif = tk.PhotoImage(file=get_resource_path("buttons/arrows-down-up.png"))
sort_btn = ttk.Button(button_frame, image=sort_gif, style="RoundedButton.TButton",
                      command=lambda: helpers.sort_list(root, scroller, hide_state_dict))
sort_btn.grid(row=0, column=2, padx=15, pady=15, sticky="ew")

refresh_gif = tk.PhotoImage(file=get_resource_path("buttons/arrows-clockwise.png"))
refresh_btn = ttk.Button(button_frame, image=refresh_gif, style="RoundedButton.TButton",
                         command=lambda: helpers.refresh_list(root, scroller, hide_state_dict))
refresh_btn.grid(row=0, column=3, padx=15, pady=15, sticky="ew")

button_frame.grid_columnconfigure(0, weight=1)

label_frame = tk.Frame(root)
# label_frame = tk.Frame(root, borderwidth=2, relief="solid")
label_frame.grid(column=0, row=3, sticky="nsew", padx=(52, 55), pady=15)

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
content_frame.grid(column=0, row=4, sticky="nsew", padx=20)
root.grid_rowconfigure(4, weight=1)  # Allow content_frame to expand vertically

canvas = tk.Canvas(content_frame)

canvas.grid(row=0, column=0, sticky="nsew")  # Make canvas fill the content_frame

content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1, minsize=402)

scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)# Place scrollbar next to canvas

scroller = tk.Frame(canvas, padx=15)
scroller.grid(sticky="nsew")

scrollable_window = canvas.create_window((0, 0), window=scroller, anchor="nw")

# This function adjusts the scroll region when content inside scroller changes size
def configure_scroll_region(event):
    bbox = canvas.bbox("all")
    # print(f"Scroll region bbox: {bbox}")  # Debug print
    # print(f"Canvas size: {canvas.winfo_width()}x{canvas.winfo_height()}")
    if bbox:
        canvas.configure(scrollregion=bbox)
        scroller.update_idletasks()
        canvas_height = canvas.winfo_height()
        content_height = bbox[3]

        # Prevent scrolling if content fits within the canvas
        if content_height <= canvas_height:
            canvas.yview_moveto(0)  # Reset scroll to the top# Update the scrollregion
  # Update the scrollregion to match the scroller's size

canvas.bind("<Configure>", lambda event: canvas.itemconfig(scrollable_window, width=event.width))  # Ensure the window width follows canvas width
scroller.bind("<Configure>", configure_scroll_region)  # Update scrollregion whenever scroller's size changes
canvas.update_idletasks()
# Configure columns in the scroller (for content layout inside the scroller)
scroller.grid_columnconfigure(0, minsize=30, weight=0)
scroller.grid_columnconfigure(1, weight=10, minsize=402)
scroller.grid_columnconfigure(2, weight=0, minsize=75)

renderlist.render_list(root, scroller, hide_state_dict)
root.update_idletasks()
root.mainloop()
