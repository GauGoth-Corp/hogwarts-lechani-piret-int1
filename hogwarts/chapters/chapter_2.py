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
from hogwarts.universe.character import initCharacter, displayCharacter, incrementAttribute, endAdventure


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

    input("Welcome aboard the Hogwarts Express! You are about to embark on your magical journey. Press enter to continue... ")

    choice = IU.askChoice("As the train departs, you look around for a free wagon. Which one do you choose?", ["Wagon 1", "Wagon 2", "Wagon 3", "Wagon 4", "Wagon 5", "Wagon 6", "Wagon 7", "Wagon 8", "Wagon 9", "Wagon 10", "Wagon 11", "Wagon 12"]) 

    PrimeNumberWagons = [2, 3, 5, 7, 11]
    if choice in PrimeNumberWagons:
        print(f"You choose the {choice}th wagon. A mysterious aura surrounds this wagon.")
        print("As you enter, you find a mathematician atmosphere: indeed, the wagon number is prime! You suddendly feel a surge of intelligence.")
        #Adds 1 to Intelligence
        incrementAttribute(character, "Intelligence", 1, True)
    else:
        print(f"You choose the {choice}th wagon. And seat near the window.")
        print(f"{character['First Name']}, do you really think choosing a precise wagon will change anything? It's just a train after all...")
    print()

    #%%== Meeting with Ron ==
    print("As the train starts moving, a boy with red hair approaches you.")
    print(f"— Mysterious character with readhead: Hi, I'm a Ron Weasley. Would you mind if I seat next to you?")
    choice = IU.askChoice("What do you answer?", [f"- {character['First Name']}: \"Go out, you seem to me very silly.\"", "You are very afraid of this boy and jump by the wagon window.", f"- {character['First Name']}: \"Hey! What's up guy! My name is {character['First Name']}, have a seat with me: atually I feel very alone...\""])
    if choice == 1:
        print("- Ron: \"I don't mind. I want a seat.\" Ron Weasley takes a seat and do not speak to you anymore.")
        #Adds 1 to Ambition
        incrementAttribute(character, "Ambition", 1, True)
        
    elif choice == 2:
        endAdventure(character, f"You have very bad luck today: the train is crossing a valley. You fall and flatten like a pancake. See you {character['First Name']}!")
    else:
        print(f"- Ron: \"Wow! Nice to meet you {character['First Name']}!\" You and Ron instantly become friends. You spend the rest of the trip chatting and laughing!")
        #Adds 2 to Loyalty
        incrementAttribute(character, "Loyalty", 2, True)
    input("Press enter to continue... ")
    print()

    #%%== Meeting with Hermione ==
    print("A girl with bushy brown hair and a book in her hand approaches you.")
    print("— Mysterious character with bushy hair: : Hi, I'm Hermione Granger. Mind if I join you?") 
    choice = IU.askChoice("What do you answer?", [f"- {character['First Name']}: \"Go out, you seem to me very nerdy.\"", "You are very afraid of this girl and jump by the wagon window.", f"- {character['First Name']}: \"Sure, have a seat! I'm {character['First Name']} by the way.\""])
    if choice == 1:
        print("- Hermione: \"Are you kidding me?? I know more spells than you can imagine! Did you know that the square root of 144 is 12? Or that the spell 'Alohomora' is used to unlock doors?\" Hermione Granger takes a seat but continues to bother you about random facts during a very (too much) long time...")
        #Adds 1 to Courage
        incrementAttribute(character, "Courage", 1, True)
    elif choice == 2:
        endAdventure(character, f"You have very bad luck today: the train is crossing a valley. You fall and flatten like a pancake. See you {character['First Name']}!")
    else:
        print(f"- Hermione: \"Nice to meet you {character['First Name']}!\" You and Hermione instantly become friends. You spend the rest of the trip discussing about various subjects, including books and spells!")
        #Adds 2 to Intelligence
        incrementAttribute(character, "Intelligence", 2, True)
    input("Press enter to continue... ")
    print()

    #%%== Encounter with Draco ==
    print("Suddenly, a boy with slicked-back blond hair and a sneer on his face approaches you.")
    print("— Mysterious character with slicked-back hair: : Well, well, well... What do we have here? I'm Draco Malfoy. Can I join you?")
    choice = IU.askChoice("What do you answer?", [f"- {character['First Name']}: \"I don't like your face: go out of there shitty!\"", "You are very afraid of this boy and jump by the wagon window.", f"- {character['First Name']}: \"Sure, have a seat! I'm {character['First Name']} by the way.\""])
    if choice == 1:
        print("- Draco: \"How rude! You will regret this!\" Draco Malfoy turns back and goes away, muttering insults under his breath.")
        #Adds 1 to Courage
        incrementAttribute(character, "Courage", 1, True)
    elif choice == 2:
        endAdventure(character, f"You have very bad luck today: the train is crossing a valley. You fall and flatten like a pancake. See you {character['First Name']}!")
    else:
        print(f"- Draco: \"Hmph. I suppose I can tolerate your presence for...")
        print("Hermione and Ron suddenly stand up.")
        print("- Ron: \"Get out of here Malfoy! We don't want your kind around us!\"")
        print("- Hermione: \"Yes! Go away!\"")
        print("Draco Malfoy, clearly offended, side eyes you and leaves the wagon.")
        print("Ron and Hermione then look at you and insult you for being friendly with Draco.")
        #Removes 2 to Loyalty
        incrementAttribute(character, "Loyalty", -2, True)
    
#%%###=== Program ===####
if __name__ == "__main__":
    Harry_the_goat = initCharacter("Mi", "Jean", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})

    meetFriends(Harry_the_goat)