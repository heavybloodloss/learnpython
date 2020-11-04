# my game

from sys import exit

inventory = []

print "You arrive at an impassible wall in the forest. This stone "
print "wall has a wooden door, which you check. It's locked, but"
print "you notice an iron key in the lock. Will you unlock the door?"

action = raw_input("> ")
action = action.lower()


if action == "yes":
    print "You enter a dark room and see four glowing door silhoettes, "
    print "Red, Blue, Green, and Yellow."
    print "You also notice a glowing red object in front of you on the floor."
else:
    print "You head back the way you came."
    exit()


class Room():
    def __init__(self, color, locked, treasure):
        self.color = color
        self.locked = True
        self.treasure = treasure


class Inventory():
    
    def add(self):
        pass
        # inventory = inventory.append()
        
    def remove(self):
        pass
        # inventory = inventory.pop()
        
    def show(self):
        print inventory


class UserAction():
    
    def __init__(self):
        pass
        
    def check_inventory(self):
        print self.inventory()


Room("red", True, "blue key")


Room("yellow", True, "green key")


Room("blue", True, "yellow key")


Room("green", True, "gold key")


print Room.red.locked



AnyDoorsLocked = Room("red").locked or Room("green").locked or Room("blue").locked or Room("yellow").locked

# while AnyDoorsLocked:

print inventory

