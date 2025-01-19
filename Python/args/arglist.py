# lets say I have 5 variables or lists or dicts I need to pass around


variables_pack = {
    "country_list": ['Argentina', 'Brazil', 'China', 'Djubuti','England'],
    "traveller":  ['Rick', 'Nat', 'Finn', 'Lachlan', 'Millie', 'Bob'],
    "visited": {'Rick': ['Argentina', 'China'],
           'Nat' : ['Argentina', 'Brazil', 'China', 'Djubuti','England'],
           'Finn': ['Brazil'],
           'Lachlan': ['Djubuti'],
           'Millie': ['Romania'],
           'Bob': ['England']}
    }

def do_stuff(variables_pack):
    for value in variables_pack["country_list"]:
        print(value)
    for value in variables_pack["traveller"]:
        print(value)
    visited = variables_pack["visited"]
    for key, value in visited.items():
        print(value)


do_stuff(variables_pack)