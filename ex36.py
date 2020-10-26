# write an adventure game, have many doors with many enemies
# have a treasure in each room that specifically kills one enemy
# this makes the player have to visit each room to survive

from sys import exit

def elevator():
	print "This is an elevator that lloks like the exit, get in?"
	
	next = raw_input("> ")
	
	if "yes" in next:
		print "Nice, good-bye, you win!"
		exit(0)
	else:
		dead("You starve to death.")

		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat beat is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you the slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed and chews your leg off.")
		elif next == "open door" and bear_moved:
			elevator()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty")
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()