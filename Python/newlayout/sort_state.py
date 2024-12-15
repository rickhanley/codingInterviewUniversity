sort_order_dict = {"sort_order": "standard"}

def sort_order_toggle(option):
    """Function returns the state of the sort_order
       Query current state by passing 0 as the option
       Toggle state by passing 1 as the option"""
    if option == 0:
        return sort_order_dict["sort_order"]
    elif option == 1:   
        if sort_order_dict["sort_order"] == "standard":
            sort_order_dict["sort_order"] = "due_date"
            return sort_order_dict["sort_order"]
        elif sort_order_dict["sort_order"] == "due_date":
            sort_order_dict["sort_order"] = "standard"
            return sort_order_dict["sort_order"]
        

    

# print(sort_order_toggle(0))
# print(sort_order_toggle(0))
# print(sort_order_toggle(1))
# print(sort_order_toggle(0))
# print(sort_order_toggle(1))
# print(sort_order_toggle(1))
        

