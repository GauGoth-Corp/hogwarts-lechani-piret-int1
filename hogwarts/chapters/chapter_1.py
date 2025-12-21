##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 1 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *

from random import randint

from universe.character import modifyMoney

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
    first_name, last_name = "", ""
    while first_name.strip() == "":
        first_name = input("Enter your character's first name: ")
        if first_name.strip() == "":
            print("You're not ready to become a problem solver if you don't even have a name... Try again shitty\n")
    while last_name.strip() == "":
        last_name = input("Enter your character's last name: ")
        if last_name.strip() == "":
            print("You're not ready to become a problem solver if you don't even have a last name... Try again shitty\n")
    attributes = {
        "Courage": IU.askNumber("Enter your Courage (1-10): ", 1, 10),
        "Intelligence": IU.askNumber("Enter your Intelligence (1-10): ", 1, 10),
        "Loyalty": IU.askNumber("Enter your Loyalty (1-10): ", 1, 10),
        "Ambition": IU.askNumber("Enter your Ambition (1-10): ", 1, 10)
    } 

    character = initCharacter(last_name, first_name, attributes)
    displayCharacter(character)
    return character


def receiveLetter(character):
    """
    Receives letter from Hogwarts and asks if the player wishes to go on an adventure (possible end state)
    :return:
    """
    input("You have received your acceptance letter to Hogwarts School of Witchcraft and Wizardry! Press enter to continue... ")
    choice = IU.askChoice("Do you wish to attend Hogwarts ?", ["Yes", "No"])
    if choice == 1 :
        input("Great! Let's get started on your magical journey. Press enter to continue... ")

    else:
        endAdventure(character, "You won't be missed! Goodbye! GAME OVER")


def meetHagrid():
    input("Hagrid arrives to take you to Hogwarts after assaulting your cousin. Press enter to continue... ")
    input("Hagrid: You're a wizard, Harry! Now, go buy me some beers with your dead parents' money. Press enter to continue... ")
    input("You arrive at Diagon Alley, the place is bustling with life. You should buy school supplies but you have enough to have some fun. Press enter to continue... ")
    input("It's now time to buy supplies! You may buy all that you want but be mindful of your money! Press enter to continue... ")

def buySupplies(display_list, values_list, character):
    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]
    required_bought = 0
    while character['Money'] >= 5:
        print(f"You have {character['Money']} Galleons. Make sure to save enough to buy the required items !")
        user_choice = IU.askChoice("Catalog of available items:", display_list + ["Exit the shop"])
        if user_choice == len(display_list) + 1: #Quit shop
            if required_bought < 3:
                msg = "You have not bought all the required supplies. Are you sure you want to go out?"
            else:
                msg = "Are you sure you want to go out of the shop?"
            quit = IU.askChoice(msg, ["Stop bothering me, let me go!", "Uhh no sorry your Highness, I will continue shopping"])
            if quit == 1:
                break
            
        #Do not check if "exit" was chosen
        if user_choice <= len(display_list):
            if values_list[user_choice-1][1] > character['Money']:
                input("You're too poor to buy this item. How about you cross the street to get a job? Press enter to continue... ")

            else:
                #Manages the strange options:
                if user_choice == 15: #100 Galleons
                    modifyMoney(character, 120)
                elif user_choice == 16: #500 Galleons
                    modifyMoney(character, 500)  
                else:
                    addItem(character, "Inventory", values_list[user_choice-1][0])

                modifyMoney(character, -values_list[user_choice-1][1])



                input(f"You have successfully purchased {values_list[user_choice-1][0]} for {values_list[user_choice-1][1]} Galleons! Press enter to continue... ")
                print(f"You now have {character['Money']} Galleons left.")
                if values_list[user_choice-1][0] in required_items:
                    required_items.remove(values_list[user_choice-1][0])
                    required_bought += 1
                    print(f"= {len(required_items)} required item(s) left to buy. =\n")

    if required_bought < 3:
        endAdventure(character, "Instead of buying school supplies you thought it would be a good idea to buy beers, guns and children. You are not a problem solver and failed your school year. Get your priorities straight. GAME OVER")
    
    else: 
        print("You have successfully bought all the required supplies! You can now head to Hogwarts.\n")
        print("Here is a summary of your character:")
        displayCharacter(character)
        input("Press enter to continue... ")
        print()

def buyPet(character):
    input("It's time to choose your pet ! ")
    input(f"You have {character['Money']} Galleons.")
    welcome_message = "Welcome to the pet store ! Don't worry if you've already spent all your money we have options for the... financially challenged"
    options = [["Owl", 20], ["Cat", 15], ["Rat", 10], ["Toad", 5], ["Random creepy guy", 0]]
    display_list = [f"{option[0]} - {option[1]} Galleons" for option in options]
    user_choice = IU.askChoice(welcome_message, display_list)
    if options[user_choice-1][1] > character['Money']:
        input("You are poor and a disappointment")

    else:
        modifyMoney(character, -options[user_choice-1][1])
        addItem(character, "Inventory", options[user_choice-1][0])
        input(f"Congratulations ! You are now the proud owner of a {options[user_choice-1][0]} .")


def startChapter1():
    """
    Starts chapter 1 of the Hogwarts adventure
    """
    introduction()
    character = createCharacter()
    receiveLetter(character) 
    meetHagrid()
    dict = IU.loadFile("data/inventory.json")
    display_list =[]
    values_list = [[value[0], value[1], value[2]] for value in dict.values()]
    required_items = ["Magic Wand", "Wizard Robe", "Potions book"]
    for value in dict.values():
        display_list.append(f"{value[0]} - {value[1]} Galleons {value[2]}")
    buySupplies(display_list, values_list, character)
    buyPet(character)
    return character
        
#%%###=== Program ===####
if __name__ == "__main__":
    startChapter1()