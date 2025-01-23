import tkinter as tk
from tkinter import ttk
import helpers
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

    # Configure the grid layout
    menu_modal.columnconfigure(0, weight=1)
    menu_modal.rowconfigure(0, weight=1)
    menu_modal.rowconfigure(1, weight=0)

    # Placeholder content to demonstrate grid behavior
    placeholder = ttk.Label(menu_modal, text="Settings Content Here", anchor="center")
    placeholder.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Save button at the bottom-right
    save_btn = ttk.Button(menu_modal, style="ListButton.TButton", text="Save",
                          command=lambda: helpers.menu_save())
    save_btn.grid(row=1, column=0, padx=20, pady=20, sticky="e")

    
    menu_modal.grab_set()