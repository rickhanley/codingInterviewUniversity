people = {
    "Rick": "Mignonne",
    "David": "Vince",
    "Dori": "Dani",
    "Ellie": "Farai"
}
anchor = {
    "Mignonne": "Wednesday",
    "Vince": "Tuesday",
    "Dani": "Wednesday",
    "Farai": "Tuesday"}


constraint = {
    "Rick": ["Tuesday", "Thursday"],
    "Ellie": ["Tuesday", "Friday"],
    "Dori": ["Wednesday", "Friday"]
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
patterns = [[1,2,4],[2,3,5],[1,3,5], [2,4,5], [1,3,4]]

for person in people:
    anchor_clash = []

for person in people:
    available_days = [day for day in days if day not in constraint.get(person,[])]
    print(f"{person}'s available days: {available_days}")
# list_comp = [person for person in people if person not in not_people]

print(people.get("Rick"))

# print(list_comp)