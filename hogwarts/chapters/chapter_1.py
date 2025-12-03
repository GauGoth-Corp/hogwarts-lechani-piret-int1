##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 1 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
#### Package modules import ####
import sys
from pathlib import Path


####### A RETIRER LORS DU BUILD - UTILISE POUR LES TESTS RELATIFS AUX FICHIERS LOCAUX #######
#Add project root to sys.path to allow imports to work
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


from hogwarts.utils import input_utils as IU
from hogwarts.universe.character import initCharacter, displayCharacter

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def introduction():
    """
    Introduction to the first chapter
    """
    print("Welcome to Hogwarts! Ready for your first adventure? Ready guys ? Ready ? Press enter to continue...")    
    input()

def createCharacter():
    """
    Asks user for character info to create a character and then displays it
    """
    first_name = input("Enter your character's first name: ")
    last_name = input("Enter your character's last name: ")
    attributes = {
        "Courage": IU.askNumber("Enter your Courage (1-10): ", 1, 10),
        "Intelligence": IU.askNumber("Enter your Intelligence (1-10): ", 1, 10),
        "Loyalty": IU.askNumber("Enter your Loyalty (1-10): ", 1, 10),
        "Ambition": IU.askNumber("Enter your Ambition (1-10): ", 1, 10)
    } 

    character = initCharacter(last_name, first_name, attributes)
    displayCharacter(character)


def receiveLetter():
    print("You have received your acceptance letter to Hogwarts School of Witchcraft and Wizardry! Press enter to continue...")
    input()
    choice = IU.askChoice("Do you wish to attend Hogwarts ?", ["Yes", "No"])
    if choice == 1 :
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
    print("You arrive at Diagon Alley, the place is bustling with life. You should buy school supplies but you have enough to have some fun. Press enter to continue...")
    input()
    print("It's now time to buy supplies! You may buy all that you want but be mindful of your money! Press enter to continue...")
    input()

def buySupplies():
    print("Catalog of available items:")

    

def start_chapter_1():
    pass
        
#%%###=== Program ===####
if __name__ == "__main__":
    createCharacter()
    receiveLetter() 
    meetHagrid()
    buySupplies()