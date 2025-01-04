def counter(x):
    for i in range (x):
        yield i
    
    
print(list(counter(5)))