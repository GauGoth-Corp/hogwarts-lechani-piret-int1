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
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *


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
        print(f"You choose the {choice}th wagon and seat near the window.")
        print(f"{character['First Name']}, do you really think choosing a precise wagon will change anything? It's just a train after all...")
    print()

    #%%== Meeting with Ron ==
    print("As the train starts moving, a boy with red hair approaches you.")
    print(f"— Mysterious character with redhead: Hi, I'm Ron Weasley. Would you mind if I sit next to you?")
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

    input("Press enter to continue... ")
    print()
    print("After hours of travelling across the British and then Scottish countryside, the Hogwarts Express finally arrives in sight of Hogwarts Castle.")
    print("You already have met Ron, Hermione, and Draco during this journey. Your adventure is just beginning!")

    print("\nHere is your current character profile, updated with your choices:")
    displayCharacter(character)
    input("\nPress enter to continue... ")
    print()

def welcomeMessage(houses):
    """
    Welcome Message from Dumbledore

    :param houses: {dict} - Houses & their current points. 
    """
    print("- Dumbledore: \"Ready guys? My name is Albus Dumbledore and I will be your headschool teacher for the year!\"")
    print("- Dumbledore: \"What am I hearing? No I am not 200 years old, thank you. -30 points for Hupplepuff!\"")
    #-30 points for Hupplepuff 
    updateHousePoints(houses, "Hufflepuff", -30, True)

    print("- Dumbledore: \"Oh, by the way very little children, did you know the existence of Houses? You will learn more about them in a very short time...\"")
    print("- Dumbledore: \"Welcome to Hogwarts School of Witchcraft and Wizardry! (Yes I'm totally crazy, but you know, we are in 1998 after all...)\"")
    print("Students applause. [This is how liberty dies... under thunderous applause.]")

    input("Press enter to continue... ")
    print()

def sortingCeremony(character, questions):
    """
    Sorting Ceremony function

    :param character: {dict} - The character dictionary
    :param questions: {list[tuple]} -  A list of tuples, each containing: (1) the question text, (2) a list of possible choices, and (3) the corresponding houses for each answer.
    """
    print("It's time for the Sorting Ceremony! The Sorting Hat will now determine your house based on your personality and choices. \nHere is a quizz. Answer the questions and discover your House! ")
    assignedHouse = assignHouse(character, questions)
    character["House"] = assignedHouse
    print(f"- Sorting Hat: \"After careful consideration, I have decided that {character['First Name']} {character['Last Name']} belongs to...\"")
    print(f"- Sorting Hat: \"{assignedHouse.upper()}!!!!\"")
    print(f"** Congratulations {character['First Name']}! You have been sorted into {assignedHouse}! **")
    print(f"\nYou then join the {assignedHouse} students under thunderous applause.")
    input("Press enter to continue... ")
    print()

def enterCommonRoom(character):
#%%
    """
    The character enters his/her House common room

    :param character: {dict} - The character dictionary
    """

    #Handles if no house assigned 
    if "House" not in character or character["House"] == None:
        print(f"[Error] No house assigned to {character['First Name']} {character['Last Name']}. Cannot enter common room.")
        endAdventure(character, "YOU HAVE FAILED THE SORTING CEREMONY. You are expelled from Hogwarts. GAME OVER")
    
    house = character["House"]
    housesDescriptions = IU.loadFile("hogwarts/data/houses.json")

    print("After stuffing yourself like a pig, you follow the Prefects through the castle corridors...\n")

    print(f"{housesDescriptions[house]['emoji']} {housesDescriptions[house]['description']}")
    print(f"{housesDescriptions[house]['installation_message']}")
    print(f"Your House colors: {housesDescriptions[house]['colors'][0]} and {housesDescriptions[house]['colors'][1]}.")
    print()
    for key, value in housesDescriptions[house]["bonus_attributs"].items():
        incrementAttribute(character, key, value, True)
    print()
    
    input("Press enter to continue... ")
    print()
#%%

def startChapter2(character, houses):

    """
    Starts Chapter 2 

    :param character: {dict} - The character dictionary 
    :param houses: {dict} - Houses & their current points. Structure used: houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}
    """
    print("=== Chapter 2: The Journey to Hogwarts ===")
    print()
    meetFriends(character)
    welcomeMessage(houses)
    #Import questions from JSON file
    questions = IU.loadFile("hogwarts/data/sorting_ceremony_questions.json")
    sortingCeremony(character, questions)
    enterCommonRoom(character)

    print("This is the end of Chapter 2. Here is your current character profile:")
    displayCharacter(character)
    print()
    print("It's now time to sleep in your common room and prepare for the classes starting tomorrow!")
    input("Press enter to continue... ")


    
#%%###=== Program ===####
if __name__ == "__main__":
    Harry_the_goat = initCharacter("Moustafa Al Ben Wallouh Ben Muhammad Abdel Kader Al Psartek", "Abdelaziz Al Saoudima", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})
    hgg_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    startChapter2(Harry_the_goat, hgg_houses)
