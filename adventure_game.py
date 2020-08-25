#!/usr/bin/env python3

"""This program plays an interactive adventure game where it gives the player
different adventure scnarios based on the player choice."""

# The random module required in order to use random functionalities
import random

# The time module required in order to create dealys in the game
import time

# The termcolor & colorma modules are used to print to the console with colors
from termcolor import colored
from colorama import init

# Some initilization required to enable coloring
init()

# lists
creatures = ['Dragon', 'Troll', 'Pirate', 'Alien']
weapons = ['dagger', 'knive', 'fists', 'long sowrd', 'bat']
PlayerChoice = ['1', '2']

# varaiable def
wep = random.choice(weapons)
mon = random.choice(creatures)


# method describe the begining of the adventure game:.
def desc():
    time.sleep(2)
    print("You find yourself standing in an open field, filled with grass",
          "and yellow wildflowers.")
    time.sleep(2)
    print("Rumor has it that a wicked " + colored(f"monster ", 'red') +
          "is somewhere around here, " +
          "and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a " + colored(f"house", 'cyan') + ".")
    time.sleep(2)
    print("To your right is a " + colored(f"dark cave", 'blue') + ".")
    time.sleep(2)
    print("In your hand you hold your trusty (but not very effective)," +
          colored(f"{wep}", 'green') + ".")
    time.sleep(2)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do (Please enter 1 or 2)?")
    time.sleep(2)
    Choice = ""
    while Choice not in PlayerChoice:
        Choice = input(
            "Please enter 1 or 2: ").lower()
    if Choice == "1":
        house()
    if Choice == "2":
        cave()


# method describe the fight in the adventure game:
def fight():
    print("\nHit the " + f"{mon}" + " with your " + f"{wep} " + "...")
    time.sleep(2)
    print("AGGGGGHHH ... The " + f"{mon}" + " is dead!!\n")
    time.sleep(2)
    print(colored(f" You WIN ..!!", 'yellow'))
    time.sleep(2)
    print("\n .. GAME OVER ..\n")


# method describe the house adventure:
def house():
    print(" inside the house there is a " + f"{mon}" + "...")
    time.sleep(2)
    print("Enter 1 to fight the monster.")
    time.sleep(2)
    print("Enter 2 to run away.")
    time.sleep(2)
    print("What would you like to do (Please enter 1 or 2)?")
    time.sleep(2)
    Choice = ""
    while Choice not in PlayerChoice:
        Choice = input(
            "Please enter 1 or 2: ").lower()
    if Choice == "1":
        time.sleep(2)
        fight()
    if Choice == "2":
        time.sleep(2)
        print("\n .. You run away ..\n")
        time.sleep(2)
        print(colored(f" You LOSE ..!!", 'yellow'))
        time.sleep(2)
        print("\n .. GAME OVER ..\n")


# method describe the cave adventure:
def cave():
    print(" inside the cave there is a " + f"{mon}" + "...")
    time.sleep(2)
    print("Enter 1 to fight the monster.")
    time.sleep(2)
    print("Enter 2 to run away.")
    time.sleep(2)
    print("What would you like to do (Please enter 1 or 2)?")
    time.sleep(2)
    Choice = ""
    while Choice not in PlayerChoice:
        Choice = input(
            "Please enter 1 or 2: ").lower()
    if Choice == "1":
        time.sleep(2)
        fight()
    if Choice == "2":
        time.sleep(2)
        print("\n .. You run away ..\n")
        print(colored(f" You LOSE ..!!", 'yellow'))
        time.sleep(2)
        print("\n .. GAME OVER ..\n")


# Starting the game and checking the validity of user input.
if __name__ == '__main__':
    ch = ""
    print(colored(
        "        ... Welcome to Advenure Game ... ", 'yellow'))
    print("")
    desc()

    while True:
        print("")
        ch = input(
            "Would you like to play again (y or n )?").lower()
        print("")
        if ch == 'y':
            wep = random.choice(weapons)
            mon = random.choice(creatures)
            desc()
        if ch == 'n':
            print("\n .. You Quit ..\n")
            quit()
