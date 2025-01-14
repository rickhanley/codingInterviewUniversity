def multiply(factor):
    def base(x): 
        return x * factor
    return base


multiply_by_6 = multiply(8)

answer = multiply_by_6(6)

print(answer)

function_list=[]

for i in range(10):
    function_list.append(multiply(i + 1))
    
for i, func in enumerate(function_list):
    print(f"multiply_by_{i + 1}(5) = {func(5)}")
    
# for i in range(10)
#     answer = f'mulitply_by_{i+1}'(i+1)
#     print(answer) 