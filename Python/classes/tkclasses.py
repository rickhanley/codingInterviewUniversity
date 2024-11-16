import tkinter as tk

from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()

label = tk.Label(text="LABEL")
label.pack()

# when using args and kwargs
# remember to UNPACK the variables you need in your __init__
# and be aware of positional assignments
class MyLabel(tk.Label):
    # so we're passing in the name of the label as label_name &
    # args (in this case bg colour). Any other args i.e. explicit
    # declarations of string based arguments would be grouped in
    # the args as a TUPLE. If you pass 1 arg. you can simply assign args
    # if there are more than 1, you need to assign args[n]
    # Then font and font_size as key value pairs
    # the key value pairs are collectively scooped up in the kwargs argument
    # So remember whatever you set up in __init__ is what you need to receive
    # You'll need to unpack stuff before calling the super() most likely
    def __init__(self, label_name, *args, **kwargs):
        self.label_name = label_name
        if len(args) > 1:
            self.bg = args[1]
        else:
            self.bg = args
        self.font = kwargs.get('font')
        self.font_size = kwargs.get('font_size')
        super().__init__(text=label_name, bg=self.bg, font=(self.font, self.font_size))

classLabel = MyLabel("ClassLabel", "red", "blue", font='Courier', font_size=40)

# classLabel.pack() 

class LabelBtn(MyLabel):
    def __init__(self, btn_name, *args, **kwargs):
        super().__init__(btn_name, *args, **kwargs)
        print(self.bg)
        print(self.label_name)
        self.pack()
        
        self.button = tk.Button(root, text=btn_name)
        self.button.pack()
        
MyLabelButton = LabelBtn("ClassLabel", "red", "blue", font='Arial', font_size=40)
            
MyLabelButton.pack()

root.mainloop()

# Calling super():

# When you call super().__init__(), it’s not returning a new instance; instead, 
# it’s calling the __init__ method of the superclass (MyLabel) on the current 
# instance (self), which is still an instance of LabelBtn.

# No New Object:

# super() doesn’t create or return a separate MyLabel object. Instead, it 
# allows the LabelBtn instance (i.e., self) to initialize with 
# MyLabel’s __init__ method, effectively adding the properties and 
# behaviors defined in MyLabel to the LabelBtn instance.
# So, super().__init__() is just executing MyLabel's __init__ code on 
# self, enriching self with attributes and methods from MyLabel.
# Extending, Not Replacing:

# LabelBtn remains a single instance, enriched by MyLabel’s initialization 
# code. The super() call essentially lets LabelBtn leverage MyLabel's 
# setup without duplicating code or creating a separate MyLabel object.
# In short, super() does not return a separate MyLabel object; it simply 
# sets up self (the LabelBtn instance) with MyLabel's initialization logic.