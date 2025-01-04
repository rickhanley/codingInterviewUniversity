from itertools import combinations

# Define the days of the week (0: Monday, ..., 4: Friday)
days = [0, 1, 2, 3, 4]

# Generate all combinations of 3 days
all_combinations = list(combinations(days, 3))

# Filter combinations to satisfy the "no more than 1 day off consecutively" constraint
valid_schedules = []
for comb in all_combinations:
    # Create a full 5-day schedule with 1 for office and 0 for off
    schedule = [1 if i in comb else 0 for i in range(5)]
    
    # Check for no more than 1 consecutive day off, including Friday-Monday
    schedule_str = "".join(map(str, schedule))  # Convert schedule to string
    if "00" not in schedule_str and not (schedule[4] == 0 and schedule[0] == 0):
        valid_schedules.append(schedule)

# Output results
print("Valid schedules (as binary vectors):")
for schedule in valid_schedules:
    print(schedule)

print(f"Total valid schedules: {len(valid_schedules)}")
