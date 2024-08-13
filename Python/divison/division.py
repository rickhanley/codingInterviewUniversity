number = 12

if(number % 2 == 0):
    print("Number divisible by 2")
if(number % 3 == 0):
    print("Number divisible by 3")
elif(number % 2 == 0):
    if(number % 3 == 0):
        print("Number divisible by 2 and 3")
