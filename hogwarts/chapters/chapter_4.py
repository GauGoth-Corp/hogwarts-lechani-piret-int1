##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 4 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Chapter 4 of the Hogwarts Game

Plot: The main character fights the Dragon in the Goblet of Fire tournament
"""


#%%###=== Modules Import ===####
import random as rd
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def introductionBeforeFight():
    """
    Chapter 4 introduction before the dragon fight 
    """

    input("Oh wow! The time has passed very very quickly! It's now your 4th year at Hogwarts and you have been selected to participate in the Triwizard Tournament! " \
    "Press enter to continue... ")
    print()
    print("You're now in the Hogwarts Great Hall, filled with students and professors, not only from Hogwarts but also from Beauxbatons and Durmstrang magical schools.")
    print("Indeed, the Triwizard Tournament is a magical competition, created 700 years ago, and opposing the three largest magical schools in Europe.")
    print("The official ceremony is about to begin... You are in the center of the hall, surrounded by Cedric Diggory, Fleur Delacour and Viktor Krum, the other champions.")
    input("Press enter to continue... ")
    print()

    print(" - Bartemius Croupton Sr.: \"Welcome, welcome everyone to the 253rd edition of the Triwizard Tournament! As you all know, this is a very dangerous competition and some of our fellow students have lost their lives in the past... So please, be careful out there! I wouldn't want to lose my job after all... Now, let the Hunger Games begin! And may the odds be ever in your favor! Uhh nope sorry wrong movie.\"")
    print("[The crowd applauds loudly]")
    print()
    print("You feel a chill run down your spine as you hear his words. You know that you will have to face a dragon in the first task...")
    input("Press enter to continue... ")
    print()

def createDragonBoss(name, pv, pe, attack, defense, special_attack):
    """
    Creates a dictionary to represent the dragon boss 
 
    :param name: {str} - Dragon's name
    :param pv: {int} - Dragon's health points
    :param pe: {int} - Dragon's energy points
    :param attack: {int} - Attack power
    :param defense: {int} - Defense power
    :param special_attack: {int} - Special attack power

    :return dragonBoss: {dict} - The dragon boss created
    """

    dragonBoss = {}

    dragonBoss["Name"] = name
    dragonBoss["PV"] = pv
    dragonBoss["PE"] = pe
    dragonBoss["Attack"] = attack
    dragonBoss["Defense"] = defense
    dragonBoss["Special Attack"] = special_attack

    return dragonBoss

#%%## Combat functions ####
def displayDragonStats(dragonBoss):
    """
    Displays the dragon boss stats 

    :param dragonBoss: {dict} - The dragon boss dictionary 
    """

    for key, item in dragonBoss.items():
        print(f"    - {key}: {item}")

def displayPlayerStats(character):
    """
    Displays the player's character stats (PV & PE)

    :param character: {dict} - The player's character dictionary 
    """

    print(f"== {character['First Name']} {character['Last Name']} stats ==")
    print(f"    - PV: {character['PV']}")
    print(f"    - PE: {character['PE']}")

def playerAttack(character, attack_increase):
    """
    The player's attack

    :param character: {dict} - The player's character dictionary 
    """

    #Fight simulation: we combine character's Courage, PE and some random to determine attack power:
    return character["Attributes"]["Courage"] * 2 + character["PE"] + rd.randint(0, 20)

def dragonAttack(dragonBoss, attack_increase):
    """
    The dragon's attack

    :param dragonBoss: {dict} - The dragon boss dictionary 
    """

    #Fight simulation: we combine dragon's Attack, PE and some random to determine attack power:
    return dragonBoss["Attack"] + dragonBoss["PE"] + rd.randint(0, 20)


def dragonFightFirstRound(character, dragonBoss): 
    """
    The first round of the dragon fight. Directly called (always same choice)

    :param character: {dict} - The player's character dictionary 
    :param dragonBoss: {dict} - The dragon boss dictionary 
    """

    choice = IU.askChoice(f"The dragon notices you and lets out a huge roar. What will you do, {character["First Name"]}?", ["Load the creature from the front", "Save time to think", "Use Avadakedavra"])
    if choice == 1:
        print("You decide to gather your courage and launch a frontal attack, hoping that this will take the dragon by surprise.")

        #Fight simulation: we combine character's Courage, PE and some random to determine attack power:
        player_attack = playerAttack(character, 0)
        print(f"Your attack power is {player_attack}!")

        #Defense: we combine dragon's Defense, PE and some random to determine defense power:
        dragon_defense = dragonBoss["Defense"] + dragonBoss["PE"] + rd.randint(0, 20)

        #Damage calculation
        damage = player_attack - dragon_defense
        if damage > 0:
            dragonBoss["PV"] -= damage
            print(f"Your attack is successful! You deal {damage} points of damage to the dragon. It now has {dragonBoss['PV']} PV left.")
        else:
            print("Your attack misses! The dragon evades your attack and prepares to strike back.")    

def dragonFightSimulation(): ...

def dragonFight(character):
    """
    The dragon fight of chapter 4

    :param character: {dict} - The player's character dictionary 
    """

    dragonBoss = createDragonBoss("Hungarian Horntail", 150, 80, 30, 20, 25)

    #Adds a PV and PE system to the character for the fight
    character["PV"] = 80
    character["PE"] = 50

    print("The time has come for your first task! You are the last champion to enter the arena. You take a deep breath and step forward, trying to calm your nerves.")
    input("Press enter to continue... ")
    print()
    print(f"As you enter the arena, you see the dragon waiting for you. It's an enormous creature and you are filled with both fear and excitement. It is a {dragonBoss['Name']}!")
    input("Press enter to continue... ")
    print()

    #%%### Fight simulation ####
    print(f"== A wild {dragonBoss['Name']} appears in front of you, breathing fire and looking very angry! ==")
    displayDragonStats(dragonBoss)
    print()

    #FIRST ROUND: always the same choice
    dragonFightFirstRound(character, dragonBoss)
    

def startChapter4(character):
    """
    Starts chapter 4 of the game: The Dragon Fight
 
    :param character: {dict} - The player's character dictionary 
    """

    print("=== Chapter 4: The Dragon Fight ===")
    print()
    introductionBeforeFight()
    dragonFight(character)
    



        
#%%###=== Program ===####
if __name__ == "__main__":
    pass