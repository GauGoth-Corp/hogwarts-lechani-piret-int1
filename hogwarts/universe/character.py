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

def modifyMoney(character, amount):
    """
    Adds or removes (negative value) the specified amount of money to the character

    :param character: {dict} - The character dictionary
    :param amount: {int} - The amount of money to add or remove
    :return character: {dict} - The updated character dictionary
    """

    character["Money"] += amount
    return character

def addItem(character, key, item):
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
        return character
    else:
        print(f"[Error:] The key '{key}' does not exist.")
        return character
        
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