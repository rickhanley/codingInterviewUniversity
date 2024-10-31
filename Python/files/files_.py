import os

def file_writer(length, collection):
    for i in range(len(collection)):
        with open(f"{length}.txt", "a") as file:
            file.write(collection[i].strip() + "\n")

def list_appender(word):
    length = len(word.strip())  # Strip spaces and newlines from word before measuring length
    if length in my_dict:
        my_dict[length].append(word.strip())
    else:
        my_dict[length] = [word.strip()]

# Rename min and max to avoid shadowing Python built-ins
min_length = float('inf')  # Initialize with a large value
max_length = 0

# First pass: determine min and max word lengths
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

# Initialize dictionary to store lists based on word lengths
my_dict = {}

# Second pass: assign words to lists based on their lengths
with open("wordlist.txt", "r") as file:
    for line in file:
        list_appender(line)

# Write each list to its corresponding file based on word length
for length in range(min_length, max_length + 1):
    if length in my_dict:
        with open(f"{length}.txt", "w") as file:
            for word in my_dict[length]:
                file.write(f"{word}\n")

print("Files created successfully.")
