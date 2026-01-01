from universe.house import *
from universe.character import *
from random import choice

from utils import input_utils as IU


contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


def learnSpells(character, spells_list):
    """
    The player learns 5 new spells (utility, offensive, defensive)

    Args:
        character (dict): your character info 
        spells_list (list): all the spells available in the game
    """
    print("You begin your magic lessons at Hogwarts. Time to learn some spells!")
    input("Press enter to continue... ")
    print()
    print("During those very hard but exciting lessons, you will learn five new spells! Let's go, what are we waiting for??")
    input("Press enter to continue... ")
    print()

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
            print(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). How exciting...")
            input("Press enter to continue... ")

        elif learned_spell[1] == "Offensive" and remaining["Offensive"] > 0:
            remaining["Offensive"] -= 1
            addItem(character, "Spells", learned_spell)
            spells_list.remove(learned_spell)
            print(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). Do you even read these anymore ?")
            input("Press enter to continue... ")

        elif learned_spell[1] == "Defensive" and remaining["Defensive"] > 0:
            remaining["Defensive"] -= 1
            addItem(character, "Spells", learned_spell)
            spells_list.remove(learned_spell)
            print(f"You just learned the spell {learned_spell[0]} ({learned_spell[1]}). Did you know that the Alicia leitmotiv was used in 20 tracks of Clair Obscur ?")
            input("Press enter to continue... ")

    print() 



def magicQuiz(character, question_answer_couple, houses={"Gryffindor":0, "Hufflepuff":0, "Ravenclaw":0, "Slytherin":0}):

    print("It's time for a magic quizz... Are you ready to obtain you B.U.S.E?? Let's see!")
    print("Answer these 4 questions to earn points for your house!")
    input("Press enter to continue... ")
    print()

    total_earned = 0
    for i in range(4):
        selected_qa = choice(question_answer_couple)
        question_answer_couple.remove(selected_qa)
        question = selected_qa[0]
        user_answer = input(f"Question {i+1}: {question} Your answer: ")
        correct_answer = selected_qa[1]
        if user_answer.lower() == correct_answer.lower():
            print("You're not as stupid as you look! Correct answer.")
            total_earned += 25
            updateHousePoints(houses, character["House"], 25)
            input("Press enter to continue... ")

        else:
            print(f"You actually are as stupid as you look! The correct answer was: {correct_answer}.")
            input("Press enter to continue... ")
        print()
    print(f"You have earned a total of {total_earned} points for your house. Why couldn't you do better ?")
    input("Press enter to continue... ")
    print()

def startChapter3(character):
    print("=== Chapter 3:  Classes and discovering Hogwarts ===\n")

    spell_list_dict = IU.loadFile("data/spells.json")
    quiz_dict = IU.loadFile("data/magic_quiz.json")
    spells_list = [[spell["name"], spell["type"]] for spell in spell_list_dict]


    question_answer_couple = [[q["question"], q["answer"]] for q in quiz_dict]
    learnSpells(character, spells_list)
    magicQuiz(character, question_answer_couple)
    return character


if __name__ == "__main__":
    spell_dict = IU.loadFile("data/inventory.json")
    print([type(spell) for spell in spell_dict])