##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. 0.1 #################################
#### CHAPTER 4 ###############################################
#### 27/11/2025 - 21/12/2025 #################################
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

def createDragonBoss(name, pv, pe, strength):
    """
    Creates a dictionary to represent the dragon boss 
 
    :param name: {str} - Dragon's name
    :param pv: {int} - Dragon's health points
    :param pe: {int} - Dragon's energy points
    :param strength: {int} - Strength power

    :return dragonBoss: {dict} - The dragon boss created
    """

    dragonBoss = {}

    dragonBoss["Name"] = name
    dragonBoss["PV"] = pv
    dragonBoss["PE"] = pe
    dragonBoss["Strength"] = strength

    return dragonBoss

#%%## Combat functions ####
def displayDragonStats(dragonBoss):
    """
    Displays the dragon boss stats 

    :param dragonBoss: {dict} - The dragon boss dictionary 
    """

    print(f"== {dragonBoss['Name']} stats ==")
    print(f"    - PV: {dragonBoss['PV']}")
    print(f"    - PE: {dragonBoss['PE']}")
    print(f"    - Strength: {dragonBoss['Strength']}")

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
    #(Chosen attribute ; attribute power ; attack increase) from action ; PE ; random(0, 10)
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
    #Dragon's Strength ; PE ; attack increase from action ; random(0, 10)
    attack = dragonBoss["Strength"] + dragonBoss["PE"]//2 + attack_increase + rd.randint(0, 10)

    #[POSSIBILITY FOR CRITICAL HIT => see the fight difficulty when testing]

    #Base PE = 80

    #Average attack exemple: 30 (Strength) + 70 (PE) //2 + 3 (increase) + 7 (random) = 75
    #Very good attack exemple: 30 (Strength) + 80 (PE) //2 + 10 (increase) + 10 (random) = 90
    #Very bad attack exemple: 30 (Strength) + 20 (PE) //2 + -5 (increase) + 1 (random) = 36

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

    if pe_used >=0:
        print(f"** You used {pe_used} PE points. **")
    else:
        print(f"** You earn {-pe_used} PE points. **")

def dragonPEuse(dragonBoss, pe_used):
    """
    The dragon's PE usage (chosed from action)

    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param pe_used: {int} - The amount of PE used. Can be positive (PE loss) or negative (PE gain) => one of only ways to rest during fight
    """

    dragonBoss["PE"] -= pe_used
    if dragonBoss["PE"] < 20: #Cannot be less than 20 for the dragon!
        dragonBoss["PE"] = 20

    if pe_used >=0:
        print(f"** The dragon used {pe_used} PE points. **")
    else:
        print(f"** The dragon earns {-pe_used} PE points. **")

def playerPErest(character):
    """
    A little chance for the player to rest and regain some PE (to be called after an action)

    :param character: {dict} - The player's character dictionary 
    :param maxPE: {int} - The maximum PE of the character (default = 50)
    """

    restChance = rd.randint(1, 100)
    if restChance <= 40: #40% chance to rest
        restAmount = rd.randint(10, 20)

        character["PE"] += restAmount #No max PE

        print(f"** You have luck! You earn {restAmount} PE points! **")

def dragonPErest(dragonBoss):
    """
    A little chance for the dragon to rest and regain some PE (to be called after an action)

    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param maxPE: {int} - The maximum PE of the dragon => Do not forget to stock the max value before fight 
    """

    restChance = rd.randint(1, 100)
    if restChance <= 30: #30% chance to rest
        restAmount = rd.randint(5, 15)

        dragonBoss["PE"] += restAmount #No max PE

        print(f"** Oh no, the dragon seems to regain some Energy! It earns {restAmount} PE points! **")

def dragonFightFirstRound(character, dragonBoss): 
    """
    The first round of the dragon fight. Directly called (always same choice)

    The 3 choices proposed are original compared to the rounds stocked in data/dragon_fight_choices.json. The choices can lead to fight or other actions.

    The 1st choice process is the same as the other rounds simulated, but then is hardcoded here (find it in dragonFightSimulation() function).

    :param character: {dict} - The player's character dictionary 
    :param dragonBoss: {dict} - The dragon boss dictionary 
    :param dragon_maxPE: {int} - The maximum PE of the dragon => Do not forget to stock the max value before fight
    """

    print("=== Round 1 ===")
    choice = IU.askChoice(f"The dragon notices you and lets out a huge roar. What will you do, {character['First Name']}?", ["Load the creature from the front", "Save time to think", "Use Avadakedavra"])
    print()
    
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


    elif choice == 2:
        print("You decide to take a moment to think and analyze the situation before making your move.")
        #No fight simulation in this case (only in the fight bcs it is the first round)

        #PE usage
        playerPEuse(character, -10)
        dragonPEuse(dragonBoss, -4)


    else:
        if "Avada Kedavra" in character["Spells"]:
            print(f"- {character['First Name']}: \"Aaaaweuhdaaakédaavraaa!\"")
            print("You shout the killing curse with all your might, hoping to take down the dragon in one swift move.")

            #Fight simulation
            player_attack = playerAttack(character, "Ambition", 5, 20) #Very high attack increase uhh is it ok?
            input("Press enter to continue... ")
            print()

            #Dragon does not strike back (!)
            print(f"The {dragonBoss['Name']} is surprised by your powerful spell and doesn't have time to react!")
            input("Press enter to continue... ")
            print()

            #Damage calculation
            dragonBoss["PV"] -= player_attack
            print(f"** Attack VERY successful! {dragonBoss['Name']} loses {player_attack} PV points. **")
            print(f"The {dragonBoss['Name']} falls to the ground, very weakened, but still alive...")
            input("Press enter to continue... ")
            print()

            #PE usage
            playerPEuse(character, 7)
            dragonPEuse(dragonBoss, 10)

        else: #If the player did not learn the spell
            print(f"- {character['First Name']}: \"AaaaweuhdaaaAAHHH Heuheuheu... [*Tousse*]\"")
            print(f"{character['First Name']}, did you think you could cast this dark spell without having learned it first??? How mad you are...")
            print("The spell turns against you, causing you severe damage. The dragon didn't even moved haha!")
            input("Press enter to continue... ")
            print()

            #Player loses -30 PV points
            damage = -30
            character["PV"] += damage
            print(f"Your attack failed miserably {character['First Name']}! What a shame you've just brought upon yourself!")
            print(f"** You lose {-damage} PV points. **")
            input("Press enter to continue... ")
            print()

            #PE usage
            playerPEuse(character, 10)
            dragonPEuse(dragonBoss, 0)

    #PE rest chance
    playerPErest(character)
    dragonPErest(dragonBoss)
    input("Press enter to continue... ")
    print()

    #Display stats at the end of the round 
    print("======= Round 1 Results =======")
    displayPlayerStats(character)
    print()
    displayDragonStats(dragonBoss)

    input("Press enter to continue... ")
    print()

def getRandomFightAction():
    """
    Gets a random fight action from the data/dragon_fight_choices.json file

    :return action: {dict} - The action chosen randomly
    """

    actions_file = IU.loadFile("data/dragon_fight_choices.json")

    #Chooses randomly one action from the file 
    action = rd.choice(actions_file)

    return action

def dragonFightSimulation(character, dragonBoss, roundNumber, message, choicesList, outcomesList):
    """
    Simulates one round of the dragon fight:

        - Round number display
        - Choice selection with message display
        - Fight simulation:
            - Player attack
            - Dragon attack
            - Damage calculation
            - PE usage
            - PE rest chance
        - Round results (stats display of player & dragon)

    :param character: {dict} - The player's character dictionary
    :param dragonBoss: {dict} - The dragon boss dictionary
    :param roundNumber: {int} - Current round number
    :param message: {str} - The message to display 
    :param choicesList: {list} - List of choices available 
    :param outcomesList: {list} - The list of possible outcomes for the choices. Each outcome is a {dict} with:
    
        - "message": {str} - Outcome message to display
        - "dragon_attack_increase": {int} - Dragon's attack increase
        - "player_attack_increase": {int} - Player's attack increase
        - "player_PE_use": {int} - Player's PE usage
        - "dragon_PE_use": {int} - Dragon's PE usage
        - "Attribute_use": {list} - [attribute_used {str} - the attribute used, attribute_power {int} - the power of the attribute used]

        :return FightResult: {bool} - True if the player wins, False if the dragon wins
    """

    print(f"=== Round {roundNumber} ===")

    choice = IU.askChoice(f"{message} What will you do, {character['First Name']}?", choicesList)
    choice -= 1 #Match list index
    print()

    #Initialization of the outcome variables:
    outComeMessage = outcomesList[choice]["message"]
    dragon_attack_increase = outcomesList[choice]["dragon_attack_increase"]
    player_attack_increase = outcomesList[choice]["player_attack_increase"]
    player_PE_use = outcomesList[choice]["player_PE_use"]
    dragon_PE_use = outcomesList[choice]["dragon_PE_use"]
    attribute_used = outcomesList[choice]["Attribute_use"][0]
    attribute_power = outcomesList[choice]["Attribute_use"][1]

    print(f"{outComeMessage}")

    #Fight simulation
    player_attack = playerAttack(character, attribute_used, attribute_power, player_attack_increase)
    input("Press enter to continue... ")
    print()
    dragon_attack = dragonAttack(dragonBoss, dragon_attack_increase)
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
    playerPEuse(character, player_PE_use)
    dragonPEuse(dragonBoss, dragon_PE_use)

    #PE rest chance
    playerPErest(character)
    dragonPErest(dragonBoss)
    input("Press enter to continue... ")
    print()

    #Display stats at the end of the round 
    print(f"======= Round {roundNumber} Results =======")
    displayPlayerStats(character)
    print()
    displayDragonStats(dragonBoss)

    input("Press enter to continue... ")
    print()

def dragonFight(character, tentativeNumber):
    """
    The dragon fight of chapter 4

    :param character: {dict} - The player's character dictionary 
    :param tentativeNumber: {int} - The number of tentatives already made 

    :return FightResult: {bool | str} - True if the player wins, False if the dragon wins. A string msg if the fight ends in the first round (considered as True then)
    """

    dragonBoss = createDragonBoss("Hungarian Horntail", 250, 80, 30)

    #Adds a PV and PE system to the character for the fight
    character["PV"] = 80
    character["PE"] = 50

    print("The time has come for your first task! You are the last champion to enter the arena. You take a deep breath and step forward, trying to calm your nerves.")
    print(f"As you enter the arena, you see the dragon waiting for you. It's an enormous creature and you are filled with both fear and excitement.")
    input("Press enter to continue... ")
    print()

    help = 0
    if tentativeNumber > 0:
        #Asks to display a help message explaining the fight dynamics
        help = IU.askChoice("** Show me how to fight the dragon? **", ["Yes please", "No, I fight dragons everyday."])
    print()
    #Displays help by default the 1st time
    if help == 1 or tentativeNumber == 0:
        print("====== Dragon Fight Help ======")
        
        print("The fight is turn-based. Each round, you will have to choose an action from a list of options.\n"\
        "Each action will have different consequences on the fight, \n" \
        "such as increasing or decreasing your attack power, using or regaining PE (Energy Points), using your attributes, etc.\n" \
        "Same for the dragon.\n" \
        "\n" \
        "Here is a detailed table explaining the different key words used during the fight:\n" \
        "Category  | Name         | Description             | Player/Dragon    | Long description\n" \
        "----------------------------------------------------------------------------------------------------------------------------\n" \
        "Key words |  Round       | Current round number    | Player           | The fight is divided into rounds, starting from 1.\n" \
        "          |  Stats       | PV/PE/Attack            | Player & Dragon  | X        \n" \
        "          |  PV          | Health Points           | Player & Dragon  | When PV <= 0, the fighter dies and the fight stops.\n" \
        "          |  PE          | Energy Points           | Player & Dragon  | PE adds damage to the attack. An amount is losed ...\n" \
        "          |              |                         |                  | ... during actions, and sometimes it is recovered.\n" \
        "          |  Strength    | Constant extra damages  | Dragon           | X\n" \
        "          |  Attribute   | Player has 4 diff Attr: | Player           | During action, a player Attribute amount can ... \n" \
        "          |              |                         |                  | ... influence them attack (multiplied by 1, 2 or 3).\n" \
        "          |              |                         |                  | ... Courage, Loyalty, Intelligence & Ambition\n" \
        "          |  Power       | Attack power            | Player & Dragon  | The higher the power is, the more damage is done.\n" \
        "          | Critical hit | Very powerful attack    | Player           | If the attack power >= 60, there is a chance to ...\n" \
        "          |              |                         |                  | ... increase the player attack by 50%.\n" \
        "-----------------------------------------------------------------------------------------------------------------------------")
        
        input("Press enter to continue... ")
        print()
        
        


#%%### Fight simulation ####
    print(f"== A wild {dragonBoss['Name']} appears in front of you, breathing fire and looking very angry! ==")
    displayDragonStats(dragonBoss)
    print()
    displayPlayerStats(character)
    input("Press enter to continue... ")
    print()

    #FIRST ROUND: always the same choice for this one only
    dragonFightFirstRound(character, dragonBoss)

    #Add a security if the fight ends in the first round
    if character["PV"] <= 0: 
        return "You are really REALLY bad... How did you manage to die in the first round???"
    elif dragonBoss["PV"] <= 0:
        return "Wow! You defeated the dragon in the first round! Incredible! Did you have a cheat code??? Tell me 👀..."

    #Other rounds
    round_number = 2

    while character["PV"] > 0 and dragonBoss["PV"] > 0:
        action = getRandomFightAction()

        #Initialization of action sub variables 
        message = action["message"]
        choicesList = action["choices"]
        outComesList = action["outcomes"]

        dragonFightSimulation(character, dragonBoss, round_number, message, choicesList, outComesList)

        #Ends the fight:
        if character["PV"] <= 0:
            return False
        
        elif dragonBoss["PV"] <= 0:
            return True
        
        round_number += 1
    

def fightWin(character, fightResult):
    """
    Personnalized dialogues for the fight win 

    :param character: {dict} - The player's character dictionary 
    :param fightResult: {bool | str} - True if the player wins, False if the dragon wins. A string msg if the fight ends in the first round (considered as True then)
    """
    print("=== VICTORY ===\n")
    if fightResult == "Wow! You defeated the dragon in the first round! Incredible! Did you have a cheat code??? Tell me 👀...":
        print(fightResult)
    
    print(f"Albus Dumbledore: - \"Congratulations {character['First Name']} {character['Last Name']}! You have successfully completed the first task of the Triwizard Tournament by defeating the dragon!")
    print("WELL DONE!!! Yes, really!\"")
    print("Uh yes, you have maybe killed some innocent spectators too but hey, details...")
    print("[The crowd erupts in applause (not talking of the injuries families of course) as you are declared the winner of the first task.]")
    input("Press enter to continue... ")
    print()
    print("=== END OF CHAPTER 4 ===")

    return fightResult

def fightLose(character, fightResult, tentativeNumber):
    """
    Personnalized dialogues for the fight lose 

    :param character: {dict} - The player's character dictionary 
    :param fightResult: {bool | str} - True if the player wins, False if the dragon wins. A string msg if the fight ends in the first round (considered as True then)
    :param tentativeNumber: {int} - The number of tentatives already made 
    """

    print("=== DEFEAT ===\n")
    if fightResult == "You are really REALLY bad... How did you manage to die in the first round???":
        print(fightResult)
    
    #Special dialogues if the player dies
    print(f"Albus Dumbledore: - \"{character['First Name'].upper()} {character['Last Name'].upper()}. You're completely useless. OUT OF MY SCHOOL! Oh damn, I forgot you're already dead... Sorry.\"")
    print(f"You have been defeated by the dragon. PINPINPINPINNN PONNNN [Game Over Zelda version sound effect].")
    print()
    print("=== GAME OVER ===")
    print()
    input("Press enter to continue... ")
    print(".....................")
    print(f"{character['First Name']}: - \"Well, where am I? Did I die? Uhh... This looks like the Hogwarts infirmary...\"")
    input("Press enter to continue... ")
    print()
    print("A lady suddendly spawns from nowhere:")

    #Special dialogues for the 2nd tentative and more
    tentativeNumber += 1
    if tentativeNumber >=3:
        print("Madam Pomfrey: - \"Unbelievable! AGAIN??? Oh, I get it now, you're doing that just to take my littles candies... Okay, not anymore. Now OUT OF MY INFIRMARY!\"")
        print("Madam Pomfrey: - \"Go to hell! And try to not die because you cost me time...\"")
        input("Press enter to continue... ")

    else:
        if tentativeNumber == 2:
            print("Madam Pomfrey: - \"OKAY. You're really starting to piss me off now. This is the second time you die against that stupid dragon! Are you even trying to win this tournament??? Come on, get your act together!\"")
            input("Press enter to continue... ")
            print()
            print(f"{character['First Name']}: - \"Uhh... Sorry Madam Pomfrey. I'll try to do better next time... I guess...\"") 

            print()
        else:
            print("Madam Pomfrey: - \"Yes dear, you had a bad encounter with a dragon during the Triwizard Tournament. But don't worry, you're safe now.\"")
            input("Press enter to continue... ")
            print()
            print(f"{character['First Name']}: - \"Phew! That was close! I must have been really lucky to survive that. Thank you, I-dont-know-who-you-are.\"")
            print("Madam Pomfrey: - \"You're welcome dear.")
        
        print("Madam Pomfrey: - \"But no time to rest, let's try again!\"")
        input("Press enter to continue... ")
        print()
        print(f"{character['First Name']}: - \"Uhh... NOWW?\"")
        print("Madam Pomfrey: - \"Yes, NOWW! The dragon won't wait for you to be ready!\"")

        #The player learns Avada Kedavra if not already known
        if "Avada Kedavra" not in character["Spells"]:
            print(f"{character['First Name']}: - \"Well, to be honest Madam Pomfrey, I tried to use Avada Kedavra on the dragon but it backfired on me... I guess I should have learned it first...\"")
            input("Press enter to continue... ")
            print()
            print("Madame Pomfrey: - \"*sigh* Okay, I better understand... I'll teach you it.\"")
            print(f"{character['First Name']}: - \"You really know this dark spell??? I should ask questions but ok, thxx!\"")
            input("Press enter to continue... ")
            print()
            character["Spells"].append("Avada Kedavra")
            print(f"** You have learned the spell Avada Kedavra! **")
            print(f"{character['First Name']}: - \"Aaweuhdaaa...\"")
            print("Madam Pomfrey: - \"NO. Don't try it on me please.\"")

        input("Press enter to continue... ")
        print()
        print(f"{character['First Name']}: - \"Oh. I'm speechless. OK, let's try again!\"")
        print("Madam Pomfrey: - \"Before you go (ahh, young people, they're in such a hurry these days), here's something to cheer you up and that should help:\"")
        input("Press enter to continue... ")  
        print()
        addItem(character, "Inventory", "Chocolate Frog", True)
        addItem(character, "Inventory", "Bertie Bott's Every Flavour Beans", True)
        incrementAttribute(character, "Courage", 7, True)
        incrementAttribute(character, "Loyalty", 7, True)
        incrementAttribute(character, "Intelligence", 7, True)
        incrementAttribute(character, "Ambition", 7, True)
        print("You feel a sudden rush of adrenaline and confidence, and suddenly feel ready for battle again! You jump out of bed, ready to face the dragon once more.")
        input("Press enter to continue... ")

    print(".....................\n")
    print()
    fightResult = False #Ensures to restart the fight 

    return fightResult, tentativeNumber

def startChapter4(character):
    """
    Starts chapter 4 of the game: The Dragon Fight
 
    :param character: {dict} - The player's character dictionary 
    """

    fightResult = False
    tentativeNumber = 0

    print("=== Chapter 4: The Dragon Fight ===")
    print()
    introductionBeforeFight()

    #Restarts fight unless the player wins
    while not fightResult:
        fightResult = dragonFight(character, tentativeNumber) 
        if fightResult == True or fightResult == "Wow! You defeated the dragon in the first round! Incredible! Did you have a cheat code??? Tell me 👀...":
            fightResult=  fightWin(character, fightResult)
        else:
            fightResult, tentativeNumber = fightLose(character, fightResult, tentativeNumber) 

            
     
#%%###=== Program ===####
if __name__ == "__main__":
    pass