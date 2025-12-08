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

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####


#%%###=== Program ===####
if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    key = [random.randint(1,15) for i in range(len(text))]

    crypt = encryptText(text, key)
    print(f"Encrypted text: '{crypt}', using auto generated key: '{key}'")
    decrypt = decryptText(crypt, key)
    print(f"Decrypted text: '{decrypt}'\n\n")


    Harry_the_goat = initCharacter("Moustafa Al Ben Wallouh Ben Muhammad Abdel Kader Al Psartek", "Abdelaziz Al Saoudima", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})
    Harry_the_goat["House"] = "Ravenclaw"
    enterCommonRoom(Harry_the_goat)