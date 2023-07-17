# Write a class called Avatar that represents a character in a role-playing game. The class should have the following:

# • Fields called name, hit_points, attack_power, and defense_power
# • A constructor that sets those fields

# • A method called attack() that returns a random integer from 1 through the value of attack_power

# • A method called defend() that takes an integer representing an attack amount and decreases hit points by an amount equal to the difference of the attack amount and defense_power (using 0 if that comes out negative). It Returns the amount of damage taken.

# • A method called is_alive() that returns True or False, depending on whether hit points is greater than 0 or not

# Then test the class by creating a program

# create a list of at least three Avatar objects.

# Then repeatedly have two different random avatars be chosen and have one of them attack the other.

# Printout which avatars are chosen and the result of the attack.

# Whenever an avatar is no longer alive, a message should be printed and that avatar should be removed from the list.

# The program stops when there is only one avatar left.

# To slow down the rate at which things happen, you might want to import time and use time.sleep(.5) to pause the program for .5 seconds after each attack.

from random import randint, sample
from time import sleep


class Avatar:
    def __init__(self, name, hit_points, attack_power, defense_power):
        self.name = name
        self.hit_points = hit_points
        self.attack_power = attack_power
        self.defense_power = defense_power

    # returns attack power
    def attack(self):
        return randint(1, self.attack_power)

    # returns how much damage a player has taken
    def defend(self, attack_amount):
        damage = attack_amount - self.defense_power
        if damage <= 0:
            damage = 0
        self.hit_points -= damage
        return damage

    # checks if player is alive
    def is_alive(self):
        return self.hit_points > 0


players = [
    Avatar('john', 40, 30, 3),
    Avatar('seth', 100, 20, 5),
    Avatar('cody', 80, 10, 8)
]

# function for running game


def startGame(players):
    # loop runs until a player is left
    while len(players) > 1:
        # selecting 2 players randomly
        attacker, defender = sample(players, 2)
        # storing attack power
        attackPower = attacker.attack()
        # printing players' names and damage they've taken
        print(f'{attacker.name} attacks')
        print(f'{defender.name} takes {defender.defend(attackPower)} damage')

        # checking if a player is defeated
        if not defender.is_alive():
            print(f'{defender.name} is defeated')
            # removing player from the list of players
            players.remove(defender)
            print('-----Round Over-----')
            print()

        # printing player name and hitpoints left
        for player in players:
            print(f'{player.name} ---- {player.hit_points}')

        print()
        # loop runs after every 0.5 seconds
        sleep(.5)

    print(f'winner is {players[0].name}')


startGame(players)
