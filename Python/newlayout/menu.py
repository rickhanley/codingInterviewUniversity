import tkinter as tk
from root_conf import root

def menu():
    print("Menu called")
    menu_modal = tk.Toplevel(root)
    menu_modal.title("Settings Menu")
    menu_modal.geometry("500x500")
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    modal_width = 500
    modal_height = 400

    position_right = root_x + (root_width // 2) - (modal_width // 2)
    position_down = root_y + (root_height // 2) - (modal_height // 2)
    menu_modal.geometry(f"{modal_width}x{modal_height}+{position_right}+{position_down}")
    
    menu_modal.grab_set()