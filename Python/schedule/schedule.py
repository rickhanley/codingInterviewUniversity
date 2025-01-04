people = ["Alice", "Bob"]
constraints = {
    "Alice": ["Monday", "Wednesday"],
    "Bob": ["Friday"]
}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for person in people:
    available_days = [day for day in days if day not in constraints.get(person, [])]
    print(f"{person}'s available days: {available_days}")
