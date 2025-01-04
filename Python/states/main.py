import states
import helpers
import classes

if __name__ == "__main__":
    helpers.info(states.state_dict)
    helpers.hello()

# helpers.view_toggle(states.state_dict)
# helpers.view_toggle(states.state_dict)
# helpers.view_toggle(states.state_dict)

# print(states.state_dict)

# states.state_dict["display"] = "lightmode"
# print(states.state_dict)

taskmanager = classes.Taskmanager()

# taskmanager.increment()
# taskmanager.increment()
# taskmanager.increment()
# taskmanager.print_info()
# taskmanager.retrieve_data()
# taskmanager.create_db()
# taskmanager.add_item("Rick", "Hanley", "1976/02/16")
# taskmanager.add_item("Natalie", "Crawford", "1977/06/15")
taskmanager.view_items()
# taskmanager.delete()