import json
import tkinter as tk



my_dict = {'Rick': 48}

my_string = json.dumps(my_dict)

print(f"Dicitonary : {my_dict}")
print(f"after json: {my_string}")

my_string = json.loads(my_string)

print(f"Dicitonary : {my_dict}")
print(f"after json: {my_string}")

class MyForm(tk.Frame):
    def __init__(self, parent, label, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = label
        tk.Label(self, text=self.label).grid(sticky='w')
        tk.Entry(self).grid(sticky='we')
        tk.Entry(self).grid()
        tk.Entry(self).grid()
        tk.Entry(self).grid()
        tk.Entry(self).grid()
        tk.Entry(self).grid()
        tk.Entry(self).grid()
    
root = tk.Tk()
root.geometry("400x400")  

form = MyForm(root, "rick")
root.grid_columnconfigure(0, weight=1)
form.grid(sticky='nswe')
        
root.mainloop()
