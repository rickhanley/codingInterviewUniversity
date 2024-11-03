'''Banana survey program'''
# ____________________________________tkinter__________________________________
# 1. You have one main winowd root or window.Tk()
# 2. Set up with .geometry to set window size
# 3. use.resizeable() as appropriate
# 4. define lables and text fields etc. Remember to attach each to the part of
#    the app required. i.e. label = tk.Label(root, text="Hello", 
#    font=('Arial 16 bold'))
# 5. display widgets using pack or grid layouts
# 6. use the control variables to have variables more easily register changes
#    to the variable and widget
# 7. Remember to use get() and set() appropriately and not assign directly
#    to the control variable - this will overwrite it incorrectly
# 8. root.mainloop() to run program usually very last line of code
# 9. Remember to use sticky within containers if required
# 10.Remember the hierarchy of items. 1 main window. Any number of widgets.
#    Widgets can be added to frames to group them
# 11.Remember to add control variables correctly to widgets StringVars are
#    textvariables when passed in to an .Entry() for example

import tkinter as tk
from ctypes import windll

# have gthe app display sharply by setting dpi awareness
windll.shcore.SetProcessDpiAwareness(1)

# create root window for app
root = tk.Tk()

# 
root.title('Banana interest survey')
root.geometry('640x560+300+300')
root.resizable(False, False) # window will be fixed size in both axes


title = tk.Label(root,
                 text='Please take the survey',
                 font=('Arial 16 bold'),
                 bg='brown',
                 fg='#ff0'
)

# ______________________tk control vars_________________________
#
# remember tk has built in vars that provide adiditonal
# functionality over standard vars. 4 types:
#
# StringVar
# IntVar
# DoubleVar
# BoolVar
#
# these vars when implememnted will create a 2 WAY BINDING meaning
# if the variable is changed in a widget and displayed elsewhere
# the display will update automaotically. Also, if the variable is
# changed directly the widget will update. 

name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name?")
name_inp = tk.Entry(root, textvariable=name_var, borderwidth=3, relief=tk.FLAT)

eater_var = tk.BooleanVar()

eater_inp = tk.Checkbutton(
    root,
    variable = eater_var,
    text='Check this box if you eat bananas'
)

num_var = tk.IntVar(value=3)
num_label = tk.Label(root,
                     text='How many bananas do you eat per day?'
)
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)

colour_var = tk.StringVar(value='Any')
colour_label = tk.Label(
    root, 
    text='What is the best colour for a banana?'
)

colour_choices = (
    'Any', 'Green', 'Green-Yellow',
    'Yellow', 'Brown-Spotted', 'Black'
)
# OptionMenu
# takes positional argumnets:
# parent, control var, option 1, option 2 ... option N)
# NOTE use of * against colour_choices tuple. This will
# automatically provide all the items as arguments

colour_inp = tk.OptionMenu(
    root, colour_var, *colour_choices
)

    
plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)

plantain_var = tk.BooleanVar()
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes', value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewww, no!', value=False, variable=plantain_var)

banana_haiku_label = tk.Label(
    root,
    text='Write a haiku about bananas'
)
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text='Submit Survey')

output_var = tk.StringVar(value='')
output_line = tk.Label(root, text='', textvariable=output_var, anchor='w', justify='left')
# ___________________________________ Layout___________________________________
#
# using grid (zero indexed)
#    columns  0  1  2  3  4
# row 0:     [0][1][2][3][4]
# row 1:     [0][1][2][3][4]
#                   etc...
# 
# sticky dictates how the widget fits in the container. Takes a string.
# we means west and east, and means to stetche to fit right and left 
# to the row 2 and 2 column width specified
# tk.W, tk.E, tk.N, tk.S are build in constants - often better to use

title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row=2,columnspan=2, sticky='we')

num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

colour_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
colour_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x',ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)

banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

def on_submit():
    """To be run when user submits the form"""
    name = name_var.get()
    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000

    colour = colour_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()

    # the arbguments to get mean
    # 1 start on line 1
    # .0 start at zeroth character so, line 1, 0 char (1st char)
    # tk.END collect through to the end
    
    haiku = banana_haiku_inp.get('1.0', tk.END)
    
    message = f'Thanks for taking the survey, {name}.\n'
    
    if not banana_eater:
        message += "Sorry you don't like bananas.\n"
    else:
        message += f'Enjoy you {number} {colour} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else: 
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku: {haiku}'
        
        
    output_var.set(message)
    
    
submit_btn.configure(command=on_submit)

root.mainloop()