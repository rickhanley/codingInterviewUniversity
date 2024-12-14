from datetime import datetime, date

today = date.today()

print("Today's date:", today)

# String representing a date
date_string = "2024-12-14"

# Parse the string into a datetime object
date_object = datetime.strptime(date_string, "%Y-%m-%d")

# Print the result
print("Datetime object:", date_object)

def date_for_saving(date_string):
    date_object = datetime.strptime(date_string, "%d/%m/%y")
    date_for_saving = date_object.strftime("%Y/%m/%d")
    return print(date_for_saving)

def date_for_display(date_string):
    date_object = datetime.strptime(date_string, "%Y/%m/%d")
    date_for_display = date_object.strftime("%d/%m/%y")
    return (print(date_for_display))
    
date_for_saving("12/12/24")
date_for_display("2024/12/14")