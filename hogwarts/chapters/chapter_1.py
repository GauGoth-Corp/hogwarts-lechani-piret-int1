##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 1 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
#### Package modules import ####
from menu import *
from input_utils import *

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def introduction():
    print("Welcome to Hogwarts! Ready for your first adventure? Ready guys ? Ready ? Press enter to continue...")    
    input

def createCharacter():
    first_name = input("Enter your character's first name: ")
    last_name = input("Enter your character's last name: ")
    attributes = {
        "Courage": askNumber("Enter your Courage (1-10): ", 1, 10),
        "Intelligence": askNumber("Enter your Intelligence (1-10): ", 1, 10),
        "Loyalty": askNumber("Enter your Loyalty (1-10): ", 1, 10),
        "Ambition": askNumber("Enter your Ambition (1-10): ", 1, 10)
    }    

def receiveLetter():
    pass

def meetHagrid():
    pass

def buySupplies():
    pass

def start_chapter_1():
    pass
        
#%%###=== Program ===####
if __name__ == "__main__":
    pass