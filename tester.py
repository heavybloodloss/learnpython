
inventory = ["apple", "banana"]
if "apple" in inventory:
    print "It's there"
else:
    print "nada my dude"
    
inventory = []

print "You arrive at an impassible wall in the forest. This stone "
print "wall has a wooden door, which you check. It's locked, but"
print "you notice an iron key in the lock. What do you do?"

action = raw_input("> ")
list_action = []
unlock_keywords = ["unlock", "turn", "key", "door"]

if action in unlock_keywords:
    print "Door Unlocked"
else:
    print "you're stuck"
