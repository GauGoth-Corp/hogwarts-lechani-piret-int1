##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHARACTER################################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
#### Package modules import ####

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

        
#%%###=== Program ===####
if __name__ == "__main__":
    print(initCharacter("Potter", "Harry", {"Courage": 10, "Intelligence": 8, "Loyalty": 9, "Ambition": 7}))