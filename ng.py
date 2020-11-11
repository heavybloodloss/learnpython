# new game design 

from ex45_classes import *
from sys import exit

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
        
# lists all the colored rooms that you need keys from
remaining_rooms = [Red, Blue, Yellow, Green]


# remaining_rooms.pop(0)

print "see main door, enter?"

if action() == "yes":
    print "You enter a dark room and see four glowing door silhoettes, "
    print "Red, Blue, Green, and Yellow."
    print "You also notice a glowing red object in front of you on the floor."
    print "Do you pick up the glowing red object?"

if action() == "yes":
    print "You have picked up the %s." % Main.treasure
    Me.inventory.append(Main.treasure)
    print "You have the following keys on you..."
    print (', '.join(Me.inventory))

while AnyKeysLeft == False:    
	for doors in remaining_rooms:
		current_room = doors
		print "Would you like to go to the %s Door?" % current_room.color
		if action() == "yes":
			print "You have unlocked the %s Room. " % current_room.color
			current_room.barred = False
			print "Upon inspection, you notice a glowing %s on the floor, " % current_room.treasure
			print "will you pick it up?"
			if action() == "yes":
				print "You have picked up the %s." % current_room.treasure
				Me.inventory.append(current_room.treasure)
				current_room.treasure = "nothing"
				print "There is %s on the floor." % current_room.treasure
				print "You have the following keys on you..."
				print (', '.join(Me.inventory))
	#             del remaining_rooms[0]
			else:
				print "You hallucinate and leave the room, wandering until you die."
				exit(1)
		else:
			print "You continue to wander in the darkness."
			exit(1)
