##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 3 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################


#%%###=== Modules Import ===####
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *
from random import choice

from hogwarts.utils import input_utils as IU
from hogwarts.universe.character import initCharacter, displayCharacter, addItem, modifyMoney, endAdventure

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####

def learnSpells(character, spells_list):
    """
    The player learns 5 new spells (utility, offensive, defensive)

    Args:
        character (dict): your character info 
        spells_list (list): all the spells available in the game
    """

    input("You begin your magic lessons at Hogwarts. Press enter to continue... ")

    utility_spells = [spell for spell in spells_list if spell[1] == "Utility"]
    offensive_spells = [spell for spell in spells_list if spell[1] == "Offensive"]
    defensive_spells = [spell for spell in spells_list if spell[1] == "Defensive"]
    for i in range(3):
        learned_spell = choice(utility_spells)
        addItem(character, "Spell", learned_spell)
        input(f"You just learned the spell {learned_spell}. How exciting... Press enter to continue... ")
    for i in range(1):
        learned_spell = choice(offensive_spells)
        addItem(character, "Spell", learned_spell)
        input(f"You just learned the spell {learned_spell}. Do you even read these anymore ? Press enter to continue... ")
    for i in range(1):
        learned_spell = choice(defensive_spells)
        addItem(character, "Spell", learned_spell)
        input(f"You just learned the spell {learned_spell}. Did you know that the Alicia leitmotiv was used in 20 tracks of Clair Obscur ? Press enter to continue... ")




def startChapter3(character):
    dict = IU.loadFile("hogwarts/data/inventory.json")
    display_list =[]
    spells_list = [[value[0], value[2]] for value in dict.values()]
    

    learnSpells(display_list, spells_list, character)
    return character

#%%###=== Program ===####
if __name__ == "__main__":
    pass