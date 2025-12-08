##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 3 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
#### Package modules import ####
from menu import *

from hogwarts.utils import input_utils as IU
from hogwarts.universe.character import initCharacter, displayCharacter, addItem, modifyMoney, endAdventure

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####

def learnSpells(character, spell_names, values_list):
     #learn 5 spells 1 offensive, 1 defensive, 3 utility chosen at random

    input("You begin your magic lessons at Hogwarts. Press enter to continue... ")
    #list of already chosen spells
    #take random index in the list
    #check if in already chosen 
    #if yes take another random index
    #should also take utility 
    learned_spells = []




def startChapter3(character):
    dict = IU.loadFile("hogwarts/data/inventory.json")
    display_list =[]
    values_list = [[value[0], value[1], value[2]] for value in dict.values()]
    spell_names = [value[0] for value in values_list]

    learnSpells(display_list, values_list, character)
    return character

#%%###=== Program ===####
if __name__ == "__main__":
    pass