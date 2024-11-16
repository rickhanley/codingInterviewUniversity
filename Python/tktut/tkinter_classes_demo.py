import tkinter as tk
import json

# define JSONVar class and extend tk.StringVar
# We're only using JSON because the clasee we're extending takes text as an argument
# and we're passing around dicitonaries, lists and tuples. So we need a way of 
# getting the argument as a string 
class JSONVar(tk.StringVar):
    def __init__(self, *args, **kwargs): # def __init__
        kwargs['value'] = json.dumps(kwargs.get('value')) # get the "value" argument from kwargs
        super().__init__(*args, **kwargs) #call super
    
    # over-ride set by converting the 'value' passed in to a string
    # with JSON dumps. set is called on the super class passing in 
    # the value of string 
    
    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)
    
    # over-ride get
    # string gets the value from superclass get i.e the value field
    # from StringVar. Our version of get then returns the string
    # transfored back into it's correct type
    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return json.loads(string)
        
    

# var1 = JSONVar(root, value=[1, 2, 3])
# var1.set([1])
# var2 = JSONVar(root, value={'a': 10, 'b': 15})

# print("Var1: ", var1.get()[1])
# print("Var2: ", var2.get()['b'])

class LabelInput(tk.Frame):
    """A label and input combined together"""
    def __init__(
        self, parent, label, inp_cls,
        inp_args, *args, **kwargs
        ):
        super().__init__(parent, *args, **kwargs)
        
        self.label = tk.Label(self, text=label, anchor='w')
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(0, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(sticky=tk.E + tk.W)
        
# class MyForm extends tk.Frame
class MyForm(tk.Frame):
    # __init__ method declares the parent, and a data_var (our new JSON class)
    # so we can pass informationa round
    def __init__(self, parent, data_var, *args, **kwargs):
        # super().__init__ is called passing the parent and *args + **kwargs
        super().__init__(parent, *args, **kwargs)
        # create instance vaiable of data_var
        self.data_var = data_var
        # create instance variable of _vars (for this methodonly and is protected)
        self._vars = {
            'name': tk.StringVar(self), # self here is the GUI element we're attaching to i.e. the FRAME
                                        # remeber we're in the super(). so self here refers to the 
                                        # superclass and that'#s what we're attaching to
            'age': tk.IntVar(self, value=2)
        }
        LabelInput(
            self, 'Name', tk.Entry,
            {'textvariable': self._vars['name']}
        ).grid(sticky=tk.E + tk.W)
        LabelInput(self, 'Age', tk.Spinbox,
            {'textvariable': self._vars['age'], 'from_': 10, 'to': 150}
        ).grid(sticky=tk.E + tk.W)
        
        tk.Button(self, text='Submit', command=self._on_submit).grid()
                
    def _on_submit(self):
        data = {key: var.get() for key, var in self._vars.items()}
        self.data_var.set(data)
            
class Application(tk.Tk):
    """A simple forms application"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jsonvar = JSONVar(self) # self her is refering to Tk - the main window
        self.output_var = tk.StringVar(self) # as above
        
        tk.Label(self, text='Please fill the form').grid(sticky='ew')
        MyForm(self, self.jsonvar).grid(sticky='nsew')
        tk.Label(self, textvariable=self.output_var).grid(sticky='ew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.jsonvar.trace_add('write', self._on_data_change)
        
    def _on_data_change(self, *args, **kwargs):
        data = self.jsonvar.get()
        output = ''.join([
            f'{key} = {value}\n'
            for key, value in data.items()
        ])
        self.output_var.set(output)

# li1 = LabelInput(root, 'Name', tk.Entry, {'bg': 'red'})
# li1.grid()

# age_var = tk.IntVar(root, value=21)
# li2 = LabelInput(root, 'Age', tk.Spinbox, {'textvariable': 'age_var', 'from': 10, 'to': 150})
# li2.grid()

if __name__ == "__main__":
    app = Application()
    app.mainloop()

# help(tk.StringVar)