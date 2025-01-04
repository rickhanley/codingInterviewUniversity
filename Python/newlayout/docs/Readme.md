# Quicktask

### The problem
I was fed up of using Excel as my to-do list app and I just wanted
something to make things a bit more organised and easier.

One thing I was keen to avoid was the to-do list app becoming a job in itself to manage. The app had to be simple, offer a few quality of life improvements over a basic list in Excel, be quick and responsive, have a robust data store and be operational offline. 

### Understanding the various options
Initially I wanted this to run in a browser given how realtively easy it is to create forms and interfaces with HTML, CSS and JS. However, it seemed really tricky to implememnt any kind of database that would live safely on the users machine. Most options wanted to run on servers which brought speed concerns and would mean the app wouldn't be usable offline. Other options that did save a local database locally seemed didn't feel as secure and I was worried about a user deleting their task list on a routine browser clearout.

I went back to looking at python as it has sqlite3 within, and given that the performance would be more than adequate for this app I felt this was the way to go. Tkinter seemed like the right choice of GUI framework as I only needed basic functionality which tkinter could provide. 

### App plan
The app needed to cover the CRUD operations. The DB schema to store this was ralatively simple:

1. A unique ID for each task
2. A creation date for the task
3. A flag to indicate a complete task
4. A free text area for the user to write the task detail
5. A due date

I had intended the app as a dekstop companion that would sit to the side of the screen so would be full height but not full screen width. Like a notepad. It would need a few buttons to function but the main part should be the list of tasks to display.

