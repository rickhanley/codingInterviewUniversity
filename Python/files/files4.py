with open("10.txt", "r") as file:
    # for line in file:
    #     print(line, end="")
        
    content = file.readlines()

    # print(content)
    for i in range(len(content)):
        print(content[i], end="")