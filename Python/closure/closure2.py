def create_incrementer():
    counter = 0  # This variable will be remembered between calls

    def increment():
        nonlocal counter  # Access the outer function's variable
        counter += 1
        return counter  # Return the incremented value


    def decrement():
        nonlocal counter
        counter -= 1
        return counter
    return increment, decrement

increase, decrease = create_incrementer()


print(increase())  # Output: 1
print(decrease())  # Output: 0
