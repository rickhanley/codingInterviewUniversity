import os, time, sys
from PIL import Image

# print(sys.path)

def list_appender(word):
    length = len(word.strip())
    if length in my_dict:
        my_dict[length]. append(word.strip())
    else:
        my_dict[length] = [word.strip()]


# list_appender("grove", 6)

min_length = 100
max_length = 0

with open("wordlist.txt", "r") as file:
    for line in file:
        word = line.strip()
        word_len = len(word)
        if min_length > word_len:
            min_length = word_len
        if max_length < word_len:
            max_length = word_len
            
print("Min length:", min_length)
print("Max length:", max_length)

my_dict = {}
for i in range(min_length, max_length):
    my_dict[f"{i - 1}"] = []
    
with open("wordlist.txt", "r") as file:
    for line in file:
        list_appender(line)
        
for length in range(min_length, max_length + 1):
    if length in my_dict:
        with open(f"{length}.txt", "w") as file:
            for word in my_dict[length]:
                file.write(f"{word}\n")
        
# print(my_dict)
    
# print("my_lists", my_dict)
            
# for i in range(min, max):
#     with open(f"{i}.txt", "w") as file:
#         file.write(f"_{i}")
                
    
# for i in range(line_count):
#     buffer = file.readline()
        
# print(min, max)


# print(f"Total number of lines: {line_count}")

# if not os.path.exists("Sample.txt"):
#     with open("Sample.txt", "w") as file:
#         print("opened")   
# else:
#     with open("Sample.txt", "r") as file:
#         for i in range(10000):
#             file.write("File opened\n")

# start_time_1 = time.time()
# with open("wordlist.txt", "r") as file:
#     buffer = file.readline()
#     while buffer != '':
#         buffer = file.readline()
#         print(buffer.strip())
# end_time_1 = time.time()
# elapsed_time_1 = end_time_1 - start_time_1
    
# start_time_2 = time.time()
# with open("wordlist.txt", "r") as file:
#     for line in file:
#         print(line.strip())
# end_time_2 = time.time()
# elapsed_time_2 = end_time_2 - start_time_2
# print(f"Loop completed in {elapsed_time_1:.6f} seconds")
# print(f"Loop completed in {elapsed_time_2:.6f} seconds")

# image = Image.open("Bob1.bmp")

# image.show()