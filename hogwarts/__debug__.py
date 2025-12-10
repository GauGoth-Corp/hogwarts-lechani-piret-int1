##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### DEBUG FILE ##############################################
#### 27/11/2025 - 04/12/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
import random
#### Package modules import ####

from universe.house import *
from universe.character import *
from utils.input_utils import *
from chapters.chapter_2 import *
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
                        "Spells": ["Lumos", "Alohomora", "Expelliarmus", "Stupefy"],
                        "Attributes": {"Courage": 8, "Intelligence": 6, "Loyalty": 4, "Ambition": 7}
                        }

    startChapter4(igor_character)

    """
    startChapter3(initCharacter("Test Debug", "Debugging Inc.", {"Courage": 5, "Intelligence": 5, "Loyalty": 5, "Ambition": 5}))



    text = input("Enter text to encrypt: ")
    key = [random.randint(1,15) for i in range(len(text))]

    crypt = encryptText(text, key)
    print(f"Encrypted text: '{crypt}', using auto generated key: '{key}'")
    decrypt = decryptText(crypt, key)
    print(f"Decrypted text: '{decrypt}'\n\n")


    Harry_the_goat = initCharacter("Moustafa Al Ben Wallouh Ben Muhammad Abdel Kader Al Psartek", "Abdelaziz Al Saoudima", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})
    Harry_the_goat["House"] = "Ravenclaw"
    enterCommonRoom(Harry_the_goat)
    """