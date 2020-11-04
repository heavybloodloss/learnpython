# my game

from sys import exit
from ex45_classes import *

# inventory = []
Me = Player()

Main = Room("Main", "red key", False)

Red = Room("Red", "blue key", True)

Yellow = Room("Yellow", "green key", True)

Blue = Room("Blue", "yellow key", True)

Green = Room("Green", "gold key", True)

Gold = Room("Gold", "freedom", False)

remaining_rooms = [Red, Blue, Yellow, Green]

# all doors have to be unlocked for final door to reveal itself, 'gold door'
AnyDoorsLocked = Green.locked or Red.locked or Blue.locked or Yellow.locked

print "You arrive at an impassible wall in the forest. This stone "
print "wall has a wooden door, which you check. It's locked, but"
print "you notice an iron key in the lock. Will you unlock the door?"


# takes user input, yes or no, and returns in lower case
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


if action() == "yes":
    print "You enter a dark room and see four glowing door silhoettes, "
    print "Red, Blue, Green, and Yellow."
    print "You also notice a glowing red object in front of you on the floor."
else:
    print "You head back the way you came."
    exit(1)

print "Do you pick up the glowing red object?"

if action() == "yes":
    print "You have picked up the %s." % Main.treasure
    Me.inventory.append(Main.treasure)
    print "You have the following keys on you..."
    print (', '.join(Me.inventory))
else:
    print "You continue to wander in the darkness."
    exit(1)

for doors in remaining_rooms:
    current_room = doors
    print "Would you like to go to the %s Door?" % current_room.color
    if action() == "yes":
        print "You have unlocked the %s Room. " % current_room.color
        print "Upon inspection, you notice a glowing %s on the floor, " % current_room.treasure
        print "will you pick it up?"
        if action() == "yes":
            current_room.locked = False
            print "You have picked up the %s." % current_room.treasure
            Me.inventory.append(current_room.treasure)
            current_room.treasure = "nothing"
            print "There is %s on the floor." % current_room.treasure
            print "You have the following keys on you..."
            print (', '.join(Me.inventory))
    else:
        print "You continue to wander in the darkness."
        exit(1)

print "As you pick up the Gold key, you hear faint harp music in the background"
print " and you check the Main Hallway. A Gold door has appeared. As you approach"
print " the key and door begin to glow brighter. Do you unlock the door?"
if action() == "yes":
    print "You have gained %s. from this place, go forth!" % Gold.treasure
else:
    print "You were so close, why quit now!?"
    exit(1)
