"""Creating a scrollable window"""
# This requires a few steps to acomplish.
# root <-- canvas   <-- scrollable_frame <-- label
#   ^          
# scrollbar
#          


# 1. Create the root window
# 2. create a scrollbar: ttk.Scrollbar (root, orient="vertical", command=canvas.yview)
# 3. Create a frame inside the canvas: scroller = ttk.Frame(canvas)
# 4. Create a window inside the canvas for the scrollable frame
#    scrollable_window = canvas.create_window((0,0), window=scroller, anchor="nw")
# 5. Add content to frame:
#    for i in range(50):
#        label = ttk.Label(scroller, text=f"{   i     }").grid(row=i, column=0, sticky="w")
# 6. Configure scrolling behavious:
#    def configure_scroll_region(event):
#        canvas.configure(scrollregion=canvas.bbox("all"))

# 7. Bind the frame's resize event to adjust the scroll region
#    scrollable_frame.bind("<Configure>", configure_scroll_region)

# 8. Bind the canvas and scrollbar to handle mouse scrolling
#    def on_mousewheel(event):
#        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

#    canvas.bind_all("<MouseWheel>", on_mousewheel)

# 9. Pack the widgets
#    canvas.pack(side="left", fill="both", expand=True)
#    scrollbar.pack(side="right", fill="y")



# import tkinter & ttk
import tkinter as tk
from tkinter import ttk

# declare root as normal
root = tk.Tk()

#Decalre a root size
root.geometry("400x400")

# create a canvas to hold our scrollable content window
canvas = tk.Canvas(root)
# create a scrollbar instance and attach to the root. This is an independant widget
# that is linked to the window it is to control via a callback yview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

# create a frame to place within the canvas to show the scrollable content
scroller = ttk.Frame(canvas)
# scrollbar.set updates the scrollbar thumb position. 
canvas.configure(yscrollcommand=scrollbar.set)
# create a scrollable_window on the canvas and attach our frame (called scroller) to it
scrollable_window = canvas.create_window((0,0), window=scroller, anchor="nw")

for i in range(50):
    label = ttk.Label(scroller, text=f"{   i   }").grid(row=i, column=0, sticky="w")

# declare function which takes an event
def configure_scroll_region(event):
    # when called it updates the scrollregion with the results from the call to bbox
    # so this is concerned with re-sizing the window when it is changes by the user
    canvas.configure(scrollregion=canvas.bbox("all"))
    
# <Configure> is a type of event in Tkinter
# so this listens for configure events (re-sizing events) and calls configure_scroll_region
scroller.bind("<Configure>", configure_scroll_region)
    
# def on_mouseWheel(event):
#     canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
# canvas.bind_all("<MouseWheel>", on_mouseWheel)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
    
# frame.grid(canvas)

root.mainloop()