class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, zombie_damage):
        self.health -= zombie_damage

    def attack(self, zombie):
        zombie.take_damage(self.damage)



class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1

    def attack_plant(self, plant):
            plant.take_damage(self.damage)

    def take_damage(self, plant_damage):
        self.health -= plant_damage

def main():
    peashooter = Plant("Peashooter", 100, 15)
    snow_pea = Plant("Snow Pea", 100, 10)
    zombie = Zombie("Zombie", 500, 20 , 2)

    turn = 1

    while True:
        print("Turn", turn)
        print("Zombie health: ", zombie.health)
        print("Zombie distance: ", zombie.distance)
        print("Peashooter health: ", peashooter.health)
        print("Snow Pea health: ", snow_pea.health)

        if peashooter.health > 0:
            peashooter.attack(zombie)

        if zombie.health <= 0:
            print("Plants win!")
            break

        if snow_pea.health > 0:
            snow_pea.attack(zombie)

        if zombie.health <= 0:
            print("Plants win!")
            break

        if zombie.distance > 0:
            zombie.move()
        else:
            if peashooter.health > 0:
                zombie.attack_plant(peashooter)
            elif snow_pea.health > 0:
                zombie.attack_plant(snow_pea)

        if peashooter.health <= 0 and snow_pea.health <= 0:
            print("Zombie wins!")
            break

        turn += 1

main()
        



