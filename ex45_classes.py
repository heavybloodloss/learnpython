class Room:
    def __init__(self, color, treasure, barred):
        self.color = color
        self.treasure = treasure
        self.barred = True
        self.unlocked = not self.barred

    # def pop(self):
    #     treasure = treasure.append()


class Inventory:

    def __init__(self):
        pass

    def add(self):
        inventory = inventory.append()

    def remove(self):
        pass
        # inventory = inventory.pop()

    def show(self):
        pass
        # print inventory


class Player:

    def __init__(self):
        self.inventory = []

    def append(self, inventory):
        inventory = inventory.append()
        return inventory


# creates instance of a player
Me = Player()

# names all of the rooms and what they hold
Main = Room("Main", "red key", False)

Red = Room("Red", "blue key", True)

Yellow = Room("Yellow", "green key", True)

Blue = Room("Blue", "yellow key", True)

Green = Room("Green", "gold key", True)

Gold = Room("Gold", "freedom", False)