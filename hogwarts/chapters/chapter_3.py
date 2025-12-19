##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### CHAPTER 3 ###############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################


#%%###=== Modules Import ===####
#### Package modules import ####
#WARNING: these imports do not work if we try to run this file directly 
#They only work if we run the program from the main directory (hogwarts/) using main.py, menu.py or __debug__.py 
from universe.house import *
from universe.character import *
from random import choice

from utils import input_utils as IU


#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####

    #USE ASK CHOICE OR ELSE YOU WILL REGRET IT


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



def magicQuiz(character, question_answer_couple, houses={"Gryffindor":0, "Hufflepuff":0, "Ravenclaw":0, "Slytherin":0}):
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
        selected_qa = choice(question_answer_couple)
        question = selected_qa[0]
        user_answer = input(f"Question {i+1}: {question} Your answer: ")
        correct_answer = selected_qa[1]
        if user_answer.lower() == correct_answer.lower():
            input("You're not as stupid as you look! Correct answer. Press enter to continue... ")
            total_earned += 25
            updateHousePoints(houses, assignedHouse, 25)

        else:
            input(f"You actually are as stupid as you look! The correct answer was: {correct_answer}. Press enter to continue... ")

    input(f"You have earned a total of {total_earned} points for your house. Why couldn't you do better ? Press enter to continue... ")


def startChapter3(character):
    spell_list_dict = IU.loadFile("data/spells.json")
    quiz_dict = IU.loadFile("data/magic_quiz.json")
    spells_list = [[spell["name"], spell["type"]] for spell in spell_list_dict]
    #questions_list = [[q["question"], i] for q in quiz_dict for i in range(len(quiz_dict))]
    #answer_list = [[q["answer"], i] for q in quiz_dict for i in range(len(quiz_dict))]  
    question_answer_couple = [[q["question"], q["answer"]] for q in quiz_dict]
    learnSpells(character, spells_list)
    magicQuiz(character, question_answer_couple)
    return character


#%%###=== Program ===####
if __name__ == "__main__":
    spell_dict = IU.loadFile("data/inventory.json")
    print([type(spell) for spell in spell_dict])