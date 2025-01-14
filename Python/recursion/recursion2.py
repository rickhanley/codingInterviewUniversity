def fib(x, sequence=[0,1,1]):
    accumulator = 0
    
    if len(sequence) == x:
        return print(sequence)
    for i in range(len(sequence) -1 ,len(sequence)):
        accumulator += (sequence[len(sequence) - 2])  + sequence[len(sequence) - 1]
        sequence.append(accumulator)
        fib(x, sequence)

fib(20)