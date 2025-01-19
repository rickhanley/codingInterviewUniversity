def numbers(*args, **kwargs):
    for i in range(len(args)):
        print(args[i] * 2)
    for key, value in kwargs["my_dict"].items():
        print(f"{key}: {value}")    

my_dict = {"Rick" : 47}

numbers(3,1,2, my_dict=my_dict)