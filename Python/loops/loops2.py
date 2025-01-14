input = [1,2,3,4,5,6,7,8,9,10]
output = []
sub = []

for i in range(len(input) - 2):
    sub = []
    for j in range(i, i + 3):
        sub.append(input[j])
    output.append(sub)
print(output)


