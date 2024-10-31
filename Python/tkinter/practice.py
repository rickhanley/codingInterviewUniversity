from tkinter import Tk, Text, Scrollbar

# Initialize main window
root = Tk()

# Create a Text widget and a Scrollbar
text_widget = Text(root, wrap="word")
scroller = Scrollbar(root, orient="vertical", command=text_widget.yview)
text_widget.config(yscrollcommand=scroller.set)

# Pack both Text and Scrollbar into the window
text_widget.pack(side="left", fill="both", expand=True)
scroller.pack(side="right", fill="y")

# Start the main loop
root.mainloop()