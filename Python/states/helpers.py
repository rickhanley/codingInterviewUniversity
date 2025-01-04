def info(input):
    return print(input)
    # print("Hello")

def hello():
    return print("Hello")

def view_toggle(state_dict):
    if(state_dict["viewtype"] == "ordered"):
        state_dict["viewtype"] = "unordered"
    else:
        state_dict["viewtype"] = "ordered"
    return print(state_dict["viewtype"])