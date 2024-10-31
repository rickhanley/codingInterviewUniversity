print([c for c in '4 and 20 blackbirds. \n' if c !=' ' and c != '\n'])

print([c for c in '4 and 20 blackbirds. \n' if not c.isspace()])


new_array = [1,2,3,4,5,6,7,8,9]



print([str(c) for c in new_array])

print([x ** 3 for x in range(10, 21)])

my_var = 1

if isinstance(my_var, int):
    print("An int")
