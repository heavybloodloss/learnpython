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

# def decision():
#     print "Which of the remaining doors do you want to inspect?"
#     decision = raw_input("> ")
#     decision = decision.capitalize()
#     if decision.find("inventory"):
#         print (', '.join(Me.inventory))
#     elif decision in remaining_rooms:
#         print "This is a test"
# 
# decision()
# my game

from sys import exit
from ex45_classes import *

# 
def action():
    user_input = raw_input("> ")
    user_input = user_input.lower()
    if "yes" or "no" in user_input:
        return user_input
    elif "inventory" in user_input:
        print (', '.join(Me.inventory))
    else:
        print "invalid response"
        exit(1)
# changed the names of the rooms to strings vs variables       
remaining_rooms = ['Red', 'Blue', 'Yellow', 'Green']

for doors in remaining_rooms:
    # i = 0
    print "%r" % doors
    index = remaining_rooms.index(doors)
    print ("the index of X is: ", index)
    print (", ".join(remaining_rooms[index]))
    # i += 1

# able to find the index of the color i'm looking for
index = remaining_rooms.index('Red')
print ("the index of Red is: ", index)

# trying to make the index callable so i can find the color and get the right room
# for doors in remaining_rooms.index():
#     current_room = doors
#     print "Would you like to go to the %s Door?" % current_room.color
#     if action() == "yes":
#         print "You have unlocked the %s Room. " % current_room.color
#         print "Upon inspection, you notice a glowing %s on the floor, " % current_room.treasure
#         print "will you pick it up?"
#         if action() == "yes":
#             current_room.locked = False
#             print "You have picked up the %s." % current_room.treasure
#             Me.inventory.append(current_room.treasure)
#             current_room.treasure = "nothing"
#             print "There is %s on the floor." % current_room.treasure
#             print "You have the following keys on you..."
#             print (', '.join(Me.inventory))
#         else:
#         	print "You hallucinate and leave the room, wandering until you die."
#         	exit(1)
#     else:
#         print "You continue to wander in the darkness."
#         exit(1)

# 
# lists all the colored rooms that you need keys from
# remaining_rooms = [0:'Red', 1:'Blue', 2:'Yellow', 3:'Green']
# 
# all doors have to be unlocked for final door to reveal itself, 'gold door'
# AnyDoorsLocked = 0.is_locked or 1.is_locked or 2.is_locked or 3.is_locked

# lists all the colored rooms that you need keys from

# del remaining_rooms[Red]
# 
# print remaining_rooms[0].color
# 
# print Red.treasure
