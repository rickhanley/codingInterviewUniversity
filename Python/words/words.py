words = ['hello', 'goodbye']

for i in range(len(words)):
    print(len(words[i]))
    
with open("words.txt", "r") as file:
    for word in file:
        print(len(word))