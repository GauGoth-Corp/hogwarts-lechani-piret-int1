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
from hogwarts.universe.character import initCharacter, displayCharacter, addItem, modifyMoney

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def introduction():
    """
    Introduction to the first chapter
    """
    input("Welcome to Hogwarts! Ready for your first adventure? Ready guys ? Ready ? Press enter to continue...")    

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
    return character


def receiveLetter():
    input("You have received your acceptance letter to Hogwarts School of Witchcraft and Wizardry! Press enter to continue... ")
    choice = IU.askChoice("Do you wish to attend Hogwarts ?", ["Yes", "No"])
    if choice == 1 :
        input("Great! Let's get started on your magical journey. Press enter to continue... ")

    else:
        input("You won't be missed! Goodbye! Press enter to exit...")
        exit()


def meetHagrid():
    input("Hagrid arrives to take you to Hogwarts after assaulting your cousin. Press enter to continue... ")
    input("Hagrid: 'You're a wizard, Harry!' Now, go buy me some beers with your dead parents' money. Press enter to continue... ")
    input("You arrive at Diagon Alley, the place is bustling with life. You should buy school supplies but you have enough to have some fun. Press enter to continue... ")
    input("It's now time to buy supplies! You may buy all that you want but be mindful of your money! Press enter to continue... ")

def buySupplies(display_list, values_list, character):
    required_bought = 0
    while character['Money'] >= 5:
        print(f"You have {character['Money']} Galleons. Make sure to save enough to buy the required items !")
        choice = IU.askChoice("Catalog of available items:", display_list)
        if values_list[choice-1][1] > character['Money']:
            input("You're too poor to buy this item. How about you cross the street to get a job? Press enter to continue... ")

        else:
            addItem(character, "Inventory", values_list[choice-1][0])
            modifyMoney(character, -values_list[choice-1][1])
            input(f"You have successfully purchased {values_list[choice-1][0]} for {values_list[choice-1][1]} Galleons! Press enter to continue... ")
            input(f"You now have {character['Money']} Galleons left.")
            if values_list[choice-1][2] == "(required)":
                required_bought += 1

    if required_bought < 3:
        input("Instead of buying school supplies you thought it would be a good idea to buy beers, guns and children. You didn't have the necessary supplies and failed your school year. Get your priorities straight. GAME OVER")
        exit()
    
    else: 
        input("You have successfully bought all the required supplies! You can now head to Hogwarts. Press enter to continue... ")

        

def start_chapter_1():
    pass
        
#%%###=== Program ===####
if __name__ == "__main__":
    character = createCharacter()
    receiveLetter() 
    meetHagrid()
    dict = IU.loadFile("hogwarts/data/inventory.json")
    display_list =[]
    values_list = [[value[0], value[1], value[2]] for value in dict.values()]

    for value in dict.values():
        display_list.append(f"{value[0]} - {value[1]} Galleons {value[2]}")
    buySupplies(display_list, values_list, character)
