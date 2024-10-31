""" Simple database implemention in Python 
    Records have a Main Heading to represent a top task
    and then a list of subtask items to implement the
    overall task completion


"""

# my_list = [x for x in range(1, 101)]

# print(my_list)



database = { 1: {
    1: "Analyse data",
    2: ["Sub 1", "Sub 2"],
    } 
}
# print(database[1][2][0])
# print(len(database))

key = len(database) + 1

new_record = {
    1: "",          # TOp heading
    2:              # due by
    3: []           # subtasks
    }

for i in range (key , 3):
    database[i] = new_record.copy()
    database[i][1] = "Top Task"
    

new_top_task = input("Please enter your top task: ")
new_sub_task = input("Please enter your subtask: ")

database[2][1] = new_top_task
database[2][2].append(new_sub_task)
database[2][2].append(new_sub_task)



print(database)














# print("LENGTH AFTER: ", len(database))
# database[f"{int(key)}"][1] = "New task"
# print(database[2])
# print(database[2][2][0])
# database[len(database)][1] = "Create report"
# database[len(database)][2].append("Email so and so")
# database[len(database)][2].append("Check report")
# database[len(database)][2].append("Call xyz")

# for i in range (4):
#     database[len(database) + 1] = new_record
    
# for i in range (1,len(database)):
#     print("Top level task: ", database[1][1])
#     for j in range (len(database[i][2])):
#         print(f"Subtask {j}: ", database[i][2][j])



