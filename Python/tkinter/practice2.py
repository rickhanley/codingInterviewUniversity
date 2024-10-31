from tkinter import Tk, Text, Scrollbar

root = Tk() # the main window

# create a text widget linked to root from Text()
text_widget = Text(root, wrap="word") 

# create a scrollbar from Scrollbar() linked to root
scroller = Scrollbar(root, orient="vertical", command=text_widget.yview)
# set the scroller inside the widget
text_widget.configure(yscrollcommand=scroller.set)
# pack both in
text_widget.pack(side="left", fill="both", expand=True)
scroller.pack(side="right", fill="y")

root.mainloop()