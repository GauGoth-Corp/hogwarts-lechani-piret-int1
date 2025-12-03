##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 2 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Functions for the second chapter of the Hogwarts Game.
We can add as much functions as we want. The mandatory functions are still needed.
"""


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
from hogwarts.universe.character import initCharacter, displayCharacter, incrementAttribute


#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
### MANDATORY FUNCTIONS ###
def meetFriends(character):
    """
    This  function  depicts  the  journey  on  the  Hogwarts  Express  and  the  ﬁrst  meeting  with  Ron, Hermione, and Draco.
    Each choice abects one of the character's attributes.
    
    :param character: {dict} - The character dictionary
    """
    #Meeting with Ron
    print(f"— Mysterious character with readhead: Hi, I'm a Ron Weasley. Would you mind if I seat next to you?")
    choice = IU.askChoice("What do you answer?", [f"- {character['First Name']}: \"Go out, you seem to me very silly.\"", "You are very afraid of this boy and jump by the wagon window.", f"- {character['First Name']}: \"Hey! What's up guy! My name is {character['First Name']}, have a seat with me: atually I feel very alone...\""])
    if choice == 1:
        print("- Ron: \"I don't mind. I want a seat.\" Ron Weasley takes a seat and do not speak to you anymore.")
        #Adds 1 to Ambition
        incrementAttribute(character, "Ambition", 1, True)
        
    elif choice == 2:
        print(f"Wrong choice! You have very bad luck today: the train is crossing a valley. You fall and flatten like a pancake. See you {character['First Name']}!")
        input("This is the end of your adventure. Press enter to exit...")
        exit()
    else:
        print(f"- Ron: \"Wow! Nice to meet you {character['First Name']}!\" You and Ron instantly become friends. You spend the rest of the trip chatting and laughing!")
        #Adds 2 to Loyalty
        incrementAttribute(character, "Loyalty", 2, True)



        
#%%###=== Program ===####
if __name__ == "__main__":
    Harry_the_goat = initCharacter("Mi", "Jean", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})

    meetFriends(Harry_the_goat)