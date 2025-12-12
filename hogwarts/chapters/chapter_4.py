##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 4 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Chapter 4 of the Hogwarts Game

Plot: The main character fights the Dragon in the Goblet of Fire tournament
"""


#%%###=== Modules Import ===####
import random as rd
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from utils import input_utils as IU
from universe.character import *

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def introductionBeforeFight():
    """
    Chapter 4 introduction before the dragon fight 
    """

    input("Oh wow! The time has passed very very quickly! It's now your 4th year at Hogwarts and you have been selected to participate in the Triwizard Tournament! " \
    "Press enter to continue... ")
    print()
    print("You're now in the Hogwarts Great Hall, filled with students and professors, not only from Hogwarts but also from Beauxbatons and Durmstrang magical schools.")
    print("Indeed, the Triwizard Tournament is a magical competition, created 700 years ago, and opposing the three largest magical schools in Europe.")
    print("The official ceremony is about to begin... You are in the center of the hall, surrounded by Cedric Diggory, Fleur Delacour and Viktor Krum, the other champions.")
    input("Press enter to continue... ")
    print()

    print(" - Bartemius Croupton Sr.: \"Welcome, welcome everyone to the 253rd edition of the Triwizard Tournament! As you all know, this is a very dangerous competition and some of our fellow students have lost their lives in the past... So please, be careful out there! I wouldn't want to lose my job after all... Now, let the Hunger Games begin! And may the odds be ever in your favor! Uhh nope sorry wrong movie.\"")
    print("[The crowd applauds loudly]")
    print()
    print("You feel a chill run down your spine as you hear his words. You know that you will have to face a dragon in the first task...")
    input("Press enter to continue... ")
    print()

def createDragonBoss(name, pv, pe, attack):
    """
    Creates a dictionary to represent the dragon boss 
 
    :param name: {str} - Dragon's name
    :param pv: {int} - Dragon's health points
    :param pe: {int} - Dragon's energy points
    :param attack: {int} - Attack power

    :return dragonBoss: {dict} - The dragon boss created
    """

    dragonBoss = {}

    dragonBoss["Name"] = name
    dragonBoss["PV"] = pv
    dragonBoss["PE"] = pe
    dragonBoss["Attack"] = attack

    return dragonBoss

#%%## Combat functions ####
def displayDragonStats(dragonBoss):
    """
    Displays the dragon boss stats 

    :param dragonBoss: {dict} - The dragon boss dictionary 
    """

    for key, item in dragonBoss.items():
        print(f"    - {key}: {item}")

def displayPlayerStats(character):
    """
    Displays the player's character stats (PV & PE)

    :param character: {dict} - The player's character dictionary 
    """

    print(f"== {character['First Name']} {character['Last Name']} stats ==")
    print(f"    - PV: {character['PV']}")
    print(f"    - PE: {character['PE']}")

def playerAttack(character, attribute_used, attribute_power, attack_increase):
    """
    The player's attack

    :param character: {dict} - The player's character dictionary 
    :param attribute_used: {str} - The attribute used for the attack (can be "Courage", "Loyalty", "Intelligence", "Ambition" or "None")
    :param attribute_power: {int} - The power of the attribute used 
    :param attack_increase: {int} - Attack increase from the chosen action (can be positive or negative) 
    """

    #Fight simulation:
    #(Chosen attribute ; attribute power ; attack increase) from action ; PE ; random(0, 20)
    attack = attack_increase + character["PE"]//2  + rd.randint(0, 10)

    if attribute_used != "None":
        attack += character["Attributes"][attribute_used] * attribute_power
        print(f"** Your {attribute_used} increases your attack by {character['Attributes'][attribute_used] * attribute_power}! **")

    #Base PE = 50

    #Attack exemple: 15 (Courage) * 2 + 3 (increase) + 45 (PE) //2 + 7 (random) = 62
    #Very good attack exemple: 16 (Ambition) * 3 + 15 (increase) + 50 (PE) //2 + 10 (random) = 98
    #Very bad attack exemple: (no attribute) + -5 (increase) + 20 (PE) //2 + 1 (random) = 6
    #Average attack exemple: 12 (Loyalty) * 2 + 5 (increase) + 35 (PE) //2 + 5 (random) =  51

    #Critical hit: +50% attack if attack >= 60 and random chance (40%)
    if rd.randint(1, 100) <= 40 and attack >= 60:
        print("** Critical hit! **")
        attack += attack//2 


    print(f"You attack with a power of {attack}!")
    return attack 

def dragonAttack(dragonBoss, attack_increase):
    """
    The dragon's attack

    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param attack_increase: {int} - Attack increase from the dragon's action (can be positive or negative) 
    """

    #Fight simulation:
    #Dragon's Attack ; PE ; attack increase from action ; random(0, 10)
    attack = dragonBoss["Attack"] + dragonBoss["PE"]//2 + attack_increase + rd.randint(0, 10)

    #[POSSIBILITY FOR CRITICAL HIT => see the fight difficulty when testing]

    #Base PE = 80

    #Average attack exemple: 30 (Attack) + 70 (PE) //2 + 3 (increase) + 7 (random) = 75
    #Very good attack exemple: 30 (Attack) + 80 (PE) //2 + 10 (increase) + 10 (random) = 90
    #Very bad attack exemple: 30 (Attack) + 20 (PE) //2 + -5 (increase) + 1 (random) = 36

    print(f"The {dragonBoss['Name']} attacks with a power of {attack}!")

    return attack

def playerPEuse(character, pe_used):
    """
    The player's PE usage (chosed from action)

    :param character: {dict} - The player's character dictionary 
    :param pe_used: {int} - The amount of PE used. Can be positive (PE loss), null, or negative (PE gain) => one of only ways to rest during fight
    """

    character["PE"] -= pe_used
    if character["PE"] < 0:
        character["PE"] = 0

    print(f"** You used {pe_used} PE points. **")

def dragonPEuse(dragonBoss, pe_used):
    """
    The dragon's PE usage (chosed from action)

    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param pe_used: {int} - The amount of PE used. Can be positive (PE loss) or negative (PE gain) => one of only ways to rest during fight
    """

    dragonBoss["PE"] -= pe_used
    if dragonBoss["PE"] < 20: #Cannot be less than 20 for the dragon!
        dragonBoss["PE"] = 20

    print(f"** The dragon used {pe_used} PE points. **")

def playerPErest(character, maxPE=50):
    """
    A little chance for the player to rest and regain some PE (to be called after an action)

    :param character: {dict} - The player's character dictionary 
    :param maxPE: {int} - The maximum PE of the character (default = 50)
    """

    restChance = rd.randint(1, 100)
    if restChance <= 40: #40% chance to rest
        restAmount = rd.randint(10, 20)

        character["PE"] += restAmount
        if character["PE"] > maxPE: #Max PE = 50
            character["PE"] = 50
        print(f"** You have luck! {restAmount} PE points have been restored! **")

def dragonPErest(dragonBoss, maxPE):
    """
    A little chance for the dragon to rest and regain some PE (to be called after an action)

    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param maxPE: {int} - The maximum PE of the dragon => Do not forget to stock the max value before fight 
    """

    restChance = rd.randint(1, 100)
    if restChance <= 30: #30% chance to rest
        restAmount = rd.randint(5, 15)

        dragonBoss["PE"] += restAmount
        if dragonBoss["PE"] > maxPE: #Max default PE = 80
            dragonBoss["PE"] = maxPE
        print(f"** Oh no, the dragon seems to regain some energy! It restores {restAmount} PE points! **")

def dragonFightFirstRound(character, dragonBoss, dragon_maxPE): 
    """
    The first round of the dragon fight. Directly called (always same choice)

    The 3 choices proposed are original compared to the rounds stocked in data/dragon_fight_choices.json. The choices can lead to fight or other actions.

    The 1st choice process is the same as the other rounds simulated, but then is hardcoded here (find it in dragonFightSimulation() function).

    :param character: {dict} - The player's character dictionary 
    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param dragon_maxPE: {int} - The maximum PE of the dragon => Do not forget to stock the max value before fight
    """

    choice = IU.askChoice(f"The dragon notices you and lets out a huge roar. What will you do, {character["First Name"]}?", ["Load the creature from the front", "Save time to think", "Use Avadakedavra"])
    if choice == 1:
        print("You decide to gather your courage and launch a frontal attack, hoping that this will take the dragon by surprise.")

        #Fight simulation
        player_attack = playerAttack(character, "Courage", 3, 15)
        input("Press enter to continue... ")
        print()
        dragon_attack = dragonAttack(dragonBoss, 5)
        input("Press enter to continue... ")
        print()

        #Damage calculation
        damage = player_attack - dragon_attack
        if damage > 0:
            dragonBoss["PV"] -= damage
            print(f"** Attack successful! {dragonBoss['Name']} loses {damage} PV points. **")
            input("Press enter to continue... ")
            print()
        else:
            character["PV"] += damage #damage is negative here
            print(f"** Your attack failed! You lose {-damage} PV points. **")
            input("Press enter to continue... ")
            print()

        #PE usage
        playerPEuse(character, 7)
        dragonPEuse(dragonBoss, 3)

        #PE rest chance
        playerPErest(character)
        dragonPErest(dragonBoss, dragon_maxPE)

    elif choice == 2:
        print("You decide to take a moment to think and analyze the situation before making your move.")
        #No fight simulation in this case (only in the fight bcs it is the first round)

        #PE usage
        playerPEuse(character, -10)
        dragonPEuse(dragonBoss, -4)

        #PE rest chance
        playerPErest(character)
        dragonPErest(dragonBoss, dragon_maxPE)

    else:
        if "Avada Kedavra" in character["Spells"]:
            print(f"- {character['First Name']}: \"Aaaawaadakédavraaa!\"")
            print("You shout the killing curse with all your might, hoping to take down the dragon in one swift move.")

            #Fight simulation
            player_attack = playerAttack(character, "Ambition", 4, 20) #Very high attack increase uhh is it ok?
            input("Press enter to continue... ")
            print()

            #Dragon does not strike back (!)

            #Damage calculation
            dragonBoss["PV"] -= player_attack
            print(f"** Attack VERY successful! {dragonBoss['Name']} loses {player_attack} PV points. **")
            print(f"The {dragonBoss['Name']} falls to the ground, very weakened, but still alive...")
            input("Press enter to continue... ")

            #PE usage
            playerPEuse(character, 7)
            dragonPEuse(dragonBoss, 10)

        else: #If the spell did not learn the spell
            print(f"{character['First Name']}, did you think you could cast this dark spell without having learned it first??? How mad you are...")
            print("The spell turns against you, causing you severe damage. The dragon didn't even moved haha!")

            #Player loses -30 PV points
            damage = -30
            character["PV"] += damage
            print(f"** Your attack failed! You lose {-damage} PV points. **")
            input("Press enter to continue... ")
            print()

            #PE usage
            playerPEuse(character, 10)
            dragonPEuse(dragonBoss, 0)

        #PE rest chance
        playerPErest(character)
        dragonPErest(dragonBoss, dragon_maxPE)            

def dragonFightSimulation(): ...

def dragonFight(character):
    """
    The dragon fight of chapter 4

    :param character: {dict} - The player's character dictionary 
    """

    dragonBoss = createDragonBoss("Hungarian Horntail", 250, 80, 30)
    dragon_maxPE = dragonBoss["PE"]

    #Adds a PV and PE system to the character for the fight
    character["PV"] = 80
    character["PE"] = 50

    print("The time has come for your first task! You are the last champion to enter the arena. You take a deep breath and step forward, trying to calm your nerves.")
    input("Press enter to continue... ")
    print()
    print(f"As you enter the arena, you see the dragon waiting for you. It's an enormous creature and you are filled with both fear and excitement. It is a {dragonBoss['Name']}!")
    input("Press enter to continue... ")
    print()

#%%### Fight simulation ####
    print(f"== A wild {dragonBoss['Name']} appears in front of you, breathing fire and looking very angry! ==")
    displayDragonStats(dragonBoss)
    print()

    #FIRST ROUND: always the same choice
    dragonFightFirstRound(character, dragonBoss, dragon_maxPE)
    

def startChapter4(character):
    """
    Starts chapter 4 of the game: The Dragon Fight
 
    :param character: {dict} - The player's character dictionary 
    """

    print("=== Chapter 4: The Dragon Fight ===")
    print()
    introductionBeforeFight()
    dragonFight(character)
    



        
#%%###=== Program ===####
if __name__ == "__main__":
    pass