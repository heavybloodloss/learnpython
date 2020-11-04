#
# inventory = ["apple", "banana"]
# if "apple" in inventory:
#     print "It's there"
# else:
#     print "nada my dude"
#
# inventory = []
#
# print "You arrive at an impassible wall in the forest. This stone "
# print "wall has a wooden door, which you check. It's locked, but"
# print "you notice an iron key in the lock. What do you do?"
#
# action = raw_input("> ")
# list_action = []
# unlock_keywords = ["unlock", "turn", "key", "door"]
#
# if action in unlock_keywords:
#     print "Door Unlocked"
# else:
#     print "you're stuck"

# class Action:
#     def __init__(self):
#         self.action = raw_input("> ")
#         self.action.lower = action
#         return action
#
#
#     elif "red" in action() and Red.locked:
#         # go to red door and get key
#     elif "blue" in action() and Blue.locked:
#         # go to blue door and get key
#     elif "yellow" in action() and Yellow.locked:
#         # go to yellow door and get key
#     elif "green" in action() and Green.locked:
#         # go to green door and get key
#
# Action.action(self)
#
# print Action

def decision():
    print "Which of the remaining doors do you want to inspect?"
    decision = raw_input("> ")
    decision = decision.capitalize()
    if decision.find("inventory"):
        print (', '.join(Me.inventory))
    elif decision in remaining_rooms:
        print "This is a test"

decision()