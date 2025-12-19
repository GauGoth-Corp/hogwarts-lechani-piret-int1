##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHARACTER ###############################################
#### 27/11/2025 - 29/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Functions for creating, managing, and displaying the player's character. 
"""

#%%###=== Modules Import ===####
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


#%%###=== Module (functions) ===####
def initCharacter(lastName, firstName, attributes):
    """
    Creates a dictionary to represent the player's character, using the following structure: 

    {"Last Name": {str}, "First Name": {str}, "Money": {int}, "Inventory": {list}, "Spells": {list}, "Attributes": {dict} }

    :param lastName: {str} - The last name of the character
    :param firstName: {str} - The first name of the character
    :param attributes: {dict} - The attributes of the character
    :return character: {dict} - The character created
    """
    character = {}

    character["Last Name"] = lastName
    character["First Name"] = firstName
    character["Money"] = 100  #100 Galleons at the beginning
    character["Inventory"] = [] #Empty at init
    character["Spells"] = [] #Empty at init
    character["Attributes"] = attributes

    return character

def displayCharacter(character):
    """
    Displays all the character's information.

    :param character: {dict} - The character dictionary
    """
    print(f"== {character['First Name']} {character['Last Name']} profile ==")
    for key, value in character.items():
        if type(value) == dict:
            print(f"{key}: ")
            for dictKey, dictValue in value.items():
                print(f"    - {dictKey}: {dictValue}")
        elif type(value) == list:
            print(f"{key}: ")
            if value:
                print(f"    - " + "\n    - ".join(value))
        else:
            print(f"{key}: {value}")

def modifyMoney(character, amount, displayMsg=False):
    """
    Adds or removes (negative value) the specified amount of money to the character

    :param character: {dict} - The character dictionary
    :param amount: {int} - The amount of money to add or remove
    :param displayMsg: {bool} ? - Whether to display a message about the money modification
    :return character: {dict} - The updated character dictionary
    """

    character["Money"] += amount
    if displayMsg:
        if amount >= 0:
            print(f"** You have received {amount} Galleons! **")
        else: 
            print(f"** You have lost {-amount} Galleons... **") 
    return character

def addItem(character, key, item ,displayMsg=False):
    """
    Adds an item to the specified list in the character dictionary. Raises an error if the key does not exist or is not a list.
    (Existing keys for lists are: "Inventory" and "Spells")

    :param character: {dict} - The character dictionary
    :param key: {str} - The key in the character dictionary where the item should be added 
    :param item: {str} - The item to add to the list
    :return character: {dict} - The updated character dictionary 
    """
    #Checks if the key exists and is a list
    if key in character:
        if type(character[key]) != list:
            print(f"[Error:] The key '{key}' is not a list.")
            return character
        
        character[key].append(item)
        if displayMsg:
            print(f"** You have obtained the item: {item}! **")
        return character
    else:
        print(f"[Error:] The key '{key}' does not exist.")
        return character
    
def incrementAttribute(character, attributeName, amount=1, displayMsg=False):
    """ 
    Increments one of the character's attributes (+ or -) by the specified amount 

    Available attributes are: "Courage", "Intelligence", "Loyalty" & "Ambition"

    :param character: {dict} - The character dictionary 
    :param attributeName: {str} - The name of the attribute to increment
    :param amount: {int} ? - The amount to increment the attribute by 
    :param displayMsg: {bool} ? - Whether to display a message about the increment 

    :return character: {dict} - The updated character dictionary  
    """

    if attributeName in character["Attributes"]:
        character["Attributes"][attributeName] += amount

        if displayMsg:
            if amount >= 0:
                if amount >= 2:
                    suffix = "s"
                else:
                    suffix = ""
                print(f"** Your {attributeName} has increased by {amount} point{suffix}! **")
            else:
                if -amount >= 2:
                    suffix = "s"
                else:
                    suffix = ""
                print(f"** Oh no, your {attributeName} has decreased by {-amount} point{suffix}... **")
    else:
        print(f"[Error] The attribute '{attributeName}' does not exist.")
    
    return character

def endAdventure(character, msg):
    """
    Ends the adventure for the character with a message and displays the final character profile 

    :param character: {dict} - The character dictionary 
    :param msg: {str} - The message to display before ending the adventure
    """ 
    print(msg)
    print("\nFinal character profile:")
    displayCharacter(character)
    print()
    cheat = input(f"This is the end of your adventure. Press enter to exit... ")
    #Loading secured key from sensitive_info.json (ADD TO .gitignore)
    try:
        key = IU.loadFile("data/sensitive_info.json")["easter_egg_pswd_key"]
    

        if IU.encryptText(cheat, key) == "Ig}H{}s%L{~x0":
            print("\n** Congratulations! You've discovered the secret cheat code easter egg! Here is a little reward: you win 1,000,000 Galleons! **")
            character = modifyMoney(character, 1000000, True)
            print()
            print("Everyone thought you were done, but suddendly you take a great breath and get back on your feet. How mysterious is magic, isn't it?")
            print(f"Welcome back, {character['First Name']} {character['Last Name']}!")
            print()

        else:
            exit()
    except TypeError:
        print(f"An error occured while trying to read the file 'data/sensitive_info.json'.\nPlease try again later or contact us at the adress {contactSupportURL} for help.")
        exit()


        
#%%###=== Program ===####
if __name__ == "__main__":
    ###For testing the file functions:
    Harry_the_goat = initCharacter("Potter", "Harry", {"Courage": 1000, "Intelligence": 0, "Loyalty": 9, "Ambition": 7})
    displayCharacter(Harry_the_goat)

    print("\nModifying money...")
    Harry_the_goat = modifyMoney(Harry_the_goat, -1000)
    displayCharacter(Harry_the_goat)

    print("\n\nTesting the addItem() function...")
    Harry_the_goat = addItem(Harry_the_goat, "Inventory", "Blaster Blastech E-11")
    list_items = ["Green Light Saber", "Comlink", "Thermal Detonator", "Datapad", "Vibroblade", "Medpac", "Poodoo", "64x Dirt", "64x Cobblestone", "64x Cobblestone", "A beautiful young Twi'lek slave", "64x Cobblestone", "38x Cobblestone", "47x Dark Oak Planks"]
    for item in list_items:
        Harry_the_goat = addItem(Harry_the_goat, "Inventory", item) 
    Harry_the_goat = addItem(Harry_the_goat, "Spells", "Abracadabite")
    Harry_the_goat = addItem(Harry_the_goat, "Spells", "Expelliarmus")
    displayCharacter(Harry_the_goat)