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
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from utils import input_utils as IU
#from chapters.chapter_3 import startChapter3
from chapters.chapter_4 import startChapter4


#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####


#%%###=== Program ===####
if __name__ == "__main__":
    print("=== DEBUG MODE ACTIVATED ===\n\n")
    #### Chapter 4 test ####
    igor_character = {
                        "Last Name": "D'Osgor", 
                        "First Name": "Igor", 
                        "Money": 531,
                        "Inventory": ["Magic Wand", "Bus full of children", "House elf", "Potions Book", "Wizard Robe"],
                        "Spells": ["Lumos", "Alohomora", "Expelliarmus", "Stupefy", "Avada Kedavra"],
                        "Attributes": {"Courage": 8, "Intelligence": 6, "Loyalty": 4, "Ambition": 7}
                        }

    startChapter4(igor_character)
