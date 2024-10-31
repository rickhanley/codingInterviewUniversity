temp = 0
swaps = False

my_array = [4,1,3,2,5]

for x in range(len(my_array)):
    for y in range (len(my_array) - 1 - x):
        if (my_array[y] > my_array[y + 1]):
            temp = my_array[y + 1]
            my_array[y + 1] = my_array[y]
            my_array[y] = temp
            swaps = True
    if (swaps == False):
        break

for x in range (len(my_array)):
    print(x)