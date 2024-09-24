import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.alive = True

    def attack(self, other):
        if self.alive:
            damage = random.randint(1, self.attack_power)
            print(f'{self.name} attacks {other.name} for {damage} damage!')
            other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            print(f'{self.name} has been defeated!')
        else:
            print(f'{self.name} has {self.health} health remaining.')

    def is_alive(self):
        return self.alive


class Player(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def choose_monster(self, monsters):
        print("\nMonsters to attack:")
        for i, monster in enumerate(monsters):
            if monster.is_alive():
                print(f"{i}. {monster.name} (Health: {monster.health})")
        
        choice = int(input(f"Choose a monster to attack (0-{len(monsters) - 1}): "))
        if 0 <= choice < len(monsters) and monsters[choice].is_alive():
            return monsters[choice]
        else:
            print("Invalid choice. Choose again.")
            return self.choose_monster(monsters)


class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)


def main():
    player = Player("Hero", health=100, attack_power=20)
    monsters = [
        Monster("Goblin", health=50, attack_power=10),
        Monster("Dragon", health=80, attack_power=15)
    ]

    print("A battle begins against monsters!\n")
    
    while player.is_alive() and any(monster.is_alive() for monster in monsters):
        monster_to_attack = player.choose_monster(monsters)
        player.attack(monster_to_attack)

        if monster_to_attack.is_alive():
            monster_to_attack.attack(player)

    if player.is_alive():
        print("\nYou have defeated all the monsters!")
    else:
        print("\nYou have been defeated by the monsters!")

if __name__ == "__main__":
    main()
