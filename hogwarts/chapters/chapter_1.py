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
from hogwarts.utils.input_utils import *

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
    choice = askChoice("Do you wish to attend Hogwarts ?", ["Yes", "No"])
    if choice == "Yes":
        print("Great! Let's get started on your magical journey. Press enter to continue...")
        input() 

    else:
        print("You won't be missed! Goodbye!")
        input()
        exit()


def meetHagrid():
    print("Hagrid arrives to take you to Hogwarts after assaulting your cousin. Press enter to continue...")
    input()
    print("Hagrid: 'You're a wizard, Harry!' Now, go buy me some beers with your dead parents' money. Press enter to continue...")
    input()
    print("You arrive at Diagon Alley with Hagrid. Instead of buying your school supplies, you decide to buy beers for Hagrid. Press enter to continue...")
    input()
    print("Hagrid is pleased with your choice. However, you still need to get your school supplies. Press enter to continue...")
    input()

def buySupplies():
    print("Welcome to Diagon Alley! You need to buy your school supplies. Press enter to continue...")
    input()
    print("Catalog of available items:")
    

def start_chapter_1():
    pass
        
#%%###=== Program ===####
if __name__ == "__main__":
    pass