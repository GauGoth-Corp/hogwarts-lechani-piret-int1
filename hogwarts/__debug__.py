##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### DEBUG FILE ##############################################
#### 27/11/2025 - 04/12/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
import random
#### Package modules import ####

from universe.house import *
from universe.character import *
from utils.input_utils import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####


#%%###=== Program ===####
if __name__ == "__main__":
    """
    text = input("Enter text to encrypt: ")
    key = [random.randint(1,15) for i in range(len(text))]

    crypt = encryptText(text, key)
    print(f"Encrypted text: '{crypt}', using auto generated key: '{key}'")
    decrypt = decryptText(crypt, key)
    print(f"Decrypted text: '{decrypt}'\n\n")


    Harry_the_goat = initCharacter("Moustafa Al Ben Wallouh Ben Muhammad Abdel Kader Al Psartek", "Abdelaziz Al Saoudima", {"Courage": 10, "Intelligence": 10, "Loyalty": 10, "Ambition": 10})
    Harry_the_goat["House"] = "Ravenclaw"
    enterCommonRoom(Harry_the_goat)
    """
    #remaining spells
    #while if remaining is 0 you don't add
    #remove spell from list when added
    def learnSpells(character, spells_list):

        input("You begin your magic lessons at Hogwarts. Press enter to continue... ")

        remaining = {
            "Utility": 3,
            "Offensive": 1,
            "Defensive": 1
        }
        while remaining["Utility"] > 0 or remaining["Offensive"] > 0 or remaining["Defensive"] > 0:
            learned_spell = choice(spells_list)

            if learned_spell[1] == "Utility" and remaining["Utility"] > 0:
                remaining["Utility"] -= 1
                addItem(character, "Spells", learned_spell)
                spells_list.remove(learned_spell)
                input(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). How exciting... Press enter to continue... ")

            elif learned_spell[1] == "Offensive" and remaining["Offensive"] > 0:
                remaining["Offensive"] -= 1
                addItem(character, "Spells", learned_spell)
                spells_list.remove(learned_spell)
                input(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). Do you even read these anymore ? Press enter to continue... ")
                
            elif learned_spell[1] == "Defensive" and remaining["Defensive"] > 0:
                remaining["Defensive"] -= 1
                addItem(character, "Spells", learned_spell)
                spells_list.remove(learned_spell)
                input(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). Did you know that the Alicia leitmotiv was used in 20 tracks of Clair Obscur ? Press enter to continue... ")

    def magicQuiz(character, questions_list, answer_list):
        return "fuck you"

    
    spell_dict = IU.loadFile("hogwarts/data/spells.json")
    quiz_dict = IU.loadFile("hogwarts/data/magic_quiz.json")
    spells_list = [[spell["name"], spell["type"]] for spell in spell_dict]
    character = initCharacter("Doe", "John", {"Courage": 5, "Intelligence": 5, "Loyalty": 5, "Ambition": 5})
    learnSpells(character, spells_list)