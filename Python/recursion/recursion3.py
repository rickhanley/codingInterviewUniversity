def combo(days, r, start=0, current_combo=[]):
    if(len(current_combo) == 3):
        yield tuple(current_combo) 
        return
    
    for i in range(start, len(days)):
        # [0], [0, 1], [0, 1, 2]
        current_combo.append(days[i])
        yield from combo(days, r, i + 1, current_combo)
        current_combo.pop()
    
r = 3  # We want combinations of 3 days
days = ['mon','tue','wed','thu','fri']
combinations = list(combo(days, r))
print(combinations)

# call 1  [0]
# call 2  [0, 1]
# call 3  [0, 1, 2] yielded then returned the popped [0, 1]
# call 4  [0, 1, 3] yielded then returned the popped [0, 1]
# call 5  [0, 1, 4] yielded then returned the popped [0, 1] and len(days) met so loop finished i incremenets
# call 6  [1]
# call 7  [1, 2]
# call 8  [1, 2, 3] yielded then returned the popped [1, 2]
# call 9  [1, 2, 4] yielded then returned the popped [1, 2] and len(days) met so loop finished i incremenets
# call 10 [2]
# call 11 [2, 3]
# call 12 [2, 3, 4] yielded then returned the popped [1, 2] and len(days) met so loop finished i incremenets