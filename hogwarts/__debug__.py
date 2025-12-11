##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### DEBUG FILE ##############################################
#### 27/11/2025 - 04/12/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

#%%###=== Modules Import ===####
from random import choice, randint
#### Package modules import ####

from universe.house import *
from universe.character import *
from utils.input_utils import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from utils import input_utils as IU

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

    def learnSpells(character, spells_list):
        """
        The player learns 5 new spells (utility, offensive, defensive)

        Args:
            character (dict): your character info 
            spells_list (list): all the spells available in the game
        """
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



    def magicQuiz(character, questions_list, answer_list, houses={"Gryffindor":0, "Hufflepuff":0, "Ravenclaw":0, "Slytherin":0}):
        """
        Asks 4 questions to your character from the magic_quiz.json file. The character's house earns 25 points per correct answer

        Args:
            character (dict): your character info
            questions_list (list): list of questions
            answer_list (list): list of answers
            houses (dict): all houses with their current points
        """
        input("Answer these 4 questions to earn points for your house! Press enter to continue... ")
        total_earned = 0
        for i in range(4):
            selected_index = randint(0, len(questions_list)-1)
            selected_qa = questions_list[selected_index]
            user_answer = input(f"Question {i+1}: {selected_qa} Your answer: ")
            correct_answer = answer_list[selected_index]

            if user_answer.lower() == correct_answer.lower():
                input("You're not as stupid as you look! Correct answer. Press enter to continue... ")
                total_earned += 25
                updateHousePoints(houses, "Gryffindor", 25)

            else:
                input(f"You actually are as stupid as you look! The correct answer was: {correct_answer}. Press enter to continue... ")

        input(f"You have earned a total of {total_earned} points for your house. Why couldn't you do better ? Press enter to continue... ")


    character = initCharacter("Hermione", "Granger", {"Courage": 8, "Intelligence": 10, "Loyalty": 9, "Ambition": 7})
    spell_dict = IU.loadFile("hogwarts/data/spells.json")
    quiz_dict = IU.loadFile("hogwarts/data/magic_quiz.json")
    spells_list = [[spell["name"], spell["type"]] for spell in spell_dict]
    questions_list = [q["question"] for q in quiz_dict]
    answer_list = [q["answer"] for q in quiz_dict]     
    learnSpells(character, spells_list)
    magicQuiz(character, questions_list, answer_list)