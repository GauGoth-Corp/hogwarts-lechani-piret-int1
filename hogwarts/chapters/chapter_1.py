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
    """
    Introduction to the first chapter
    """
    print("Welcome to Hogwarts! Ready for your first adventure? Ready guys ? Ready ? Press enter to continue...")    
    input

def createCharacter():
    """
    Asks user for character info to create a character and then displays it
    """
    first_name = input("Enter your character's first name: ")
    last_name = input("Enter your character's last name: ")
    attributes = {
        "Courage": askNumber("Enter your Courage (1-10): ", 1, 10),
        "Intelligence": askNumber("Enter your Intelligence (1-10): ", 1, 10),
        "Loyalty": askNumber("Enter your Loyalty (1-10): ", 1, 10),
        "Ambition": askNumber("Enter your Ambition (1-10): ", 1, 10)
    } 

    character = initCharacter(last_name, first_name, attributes)
    displayCharacter(character)


def receiveLetter():
    print("You have received your acceptance letter to Hogwarts School of Witchcraft and Wizardry! Press enter to continue...")
    input()
    askChoice("Do you wish to attend Hogwarts ?", ["Yes", "No"])


def meetHagrid():
    pass

def buySupplies():
    pass

def start_chapter_1():
    pass
        
#%%###=== Program ===####
if __name__ == "__main__":
    pass