def combinations_recursive(pool, r, start=0, current_combination=[]):
    print(f"called with start: {start} c_c{current_combination} ")
    # Base case: if we've selected 'r' elements, yield the combination
    if len(current_combination) == r:
        yield tuple(current_combination)
        return
        

    # Recursive case: for each element starting from 'start', recursively generate combinations
    for i in range(start, len(pool)):
        # Include pool[i] in the current combination
        current_combination.append(pool[i])
        # Recursively generate combinations with the remaining elements
        yield from combinations_recursive(pool, r, i + 1, current_combination)

        # Backtrack: remove the last element to explore other combinations
        current_combination.pop()

# Example usage
days = [0, 1, 2, 3, 4]  # 5 days (0, 1, 2, 3, 4)
r = 3  # We want combinations of 3 days

combinations = list(combinations_recursive(days, r))
print(combinations)
