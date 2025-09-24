# Plants vs. Zombies Game Implementation

class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.health = 100

    def attack(self):
        return "I am attacking!"

class Zombie:
    def __init__(self, type, health):
        self.type = type
        self.health = health

    def eat_brain(self):
        return "Brains!"

class Game:
    def __init__(self):
        self.plants = []
        self.zombies = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def add_zombie(self, zombie):
        self.zombies.append(zombie)

    def start_game(self):
        print("Game started!")

# Example usage
if __name__ == '__main__':
    game = Game()
    peashooter = Plant("Peashooter", 100)
    zombie = Zombie("Regular Zombie", 100)
    game.add_plant(peashooter)
    game.add_zombie(zombie)
    game.start_game()