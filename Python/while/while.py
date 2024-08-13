i = 0

while(i < 1000000):
    if(i % 381 == 0):
        print(f"divisible by 381 {(int) (i / 381)} times!")
    i = i + 1
print(f"Done!: {i}")
 
# for i in range(1000000000):
#     pass
# print(f"Done!: {i}")
