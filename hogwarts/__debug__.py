##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### DEBUG FILE ##############################################
#### 27/11/2025 - 04/12/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
from random import choice, randint
#### Package modules import ####

from universe.house import *
from universe.character import *
from utils.input_utils import *
from chapters.chapter_1 import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from utils import input_utils as IU
#from chapters.chapter_3 import startChapter3
from chapters.chapter_4 import *


#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####


#%%###=== Program ===####
if __name__ == "__main__":
    print("=== DEBUG MODE ACTIVATED ===\n\n")
    
    #### Chapter 4 test ####
    igor_character = {
                        "Last Name": "clair", 
                        "First Name": "obscur", 
                        "Money": 531,
                        "Inventory": ["Magic Wand", "Bus full of children", "House elf", "Potions Book", "Wizard Robe"],
                        "Spells": [],
                        "Attributes": {"Courage": 13, "Intelligence": 11, "Loyalty": 10, "Ambition": 13},
                        "House": "Slytherin"
                        }
    
    """
    hungarian_horntail = createDragonBoss("Hungarian Horntail", 250, 80, 30)

    #Adds a PV and PE system to the character for the fight
    igor_character["PV"] = 80
    igor_character["PE"] = 50
    
    dragonFightFirstRound(igor_character, hungarian_horntail)
    """
    
    startChapter1()

