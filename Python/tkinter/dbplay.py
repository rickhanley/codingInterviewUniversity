import sqlite3
import tkinter as tk


def add_subtask(heading_id, subtask):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO subtasks (heading_id, subtask) VALUES (?, ?)", (heading_id, subtask))
    conn.commit()
    conn.close()
    print(f"Subtask '{subtask}' added successfully under heading ID {heading_id}.")

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

heading_id = 1
new_subtask = "New subtask"
# add_subtask(heading_id, new_subtask)

cursor.execute("SELECT * FROM headings JOIN subtasks ON subtasks.heading_id = headings.id")

results_set = cursor.fetchall()
print(f"Length of set: {len(results_set)}")

conn.close()

# for i in range(len(results_set)):
#     for j in range(len(results_set[0])):
#         print(results_set[i][j])

def add_entry(entry):
    print(entry)
    conn = sqlite3.connect('tw.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO entries (entry) VALUES (?)", (entry,))
    conn.commit()
    conn.close()
    
conn = sqlite3.connect('tw.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM entries")

results_set = cursor.fetchall()
print(f"Length of set: {len(results_set)}")

    

root = tk.Tk()

text_input = tk.Entry(root)
text_input.pack()

def get_text():
    text_content = text_input.get()
    add_entry(text_content)
    
get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack()

root.mainloop()