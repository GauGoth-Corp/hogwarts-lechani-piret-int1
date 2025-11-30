##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### HOUSE ###################################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Functions for managing Hogwarts houses, including player distribution, updating points, and displaying the winning house.
"""

#%%###=== Modules Import ===####
#### Package modules import ####


#%%###=== Global variables ===###
from hogwarts.utils.input_utils import askChoice


contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####
def updateHousePoints(houses, houseName, points):
    """
    Updates the score of the specified house.

    :param houses: {dict} - Houses associated with their current points. Structure used: houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0} 
    :param houseName: {str} - The name of the house to update.
    :param points: {int} - The number of points to add (or subtract if negative) to the house.
    """
    if houseName not in houses:
        print(f"The house '{houseName}' does not exist.")
    else:
        houses[houseName] += points

def displayHouses(houses):
    """
    Displays the current points of the houses 

    :param houses: {dict} - Houses associated with their current points. Structure used: houses ={"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0} 
    """
    print("== Current House Points: ==") 
    for house, points in houses.items() :
        print(f"{house}: {points} points")

def displayWinningHouse(houses):
    """
    Displays the house with the highest points.

    :param houses: {dict} - Houses associated with their current points. Structure used: houses ={"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0} 
    """
    winningHouseScore = houses["Gryffindor"]
    #Gets the highest score
    for key, value in houses.items():
        if value > winningHouseScore:
            winningHouseScore = value

    #Now determines all the houses with the same score (if there is draw)
    WinningHousesList = []
    for key, value in houses.items():
        if value == winningHouseScore:
            WinningHousesList.append([key, value])

    if len(WinningHousesList) == 1:
        print(f"The current winning house is {WinningHousesList[0][0]} with a total of {WinningHousesList[0][1]} points.")
    else:
        print("The current winning houses are ", end="")

        begin, endee = "", ", "
        for i in range(len(WinningHousesList)):
            #Adds to the last house a "and " at the beginning and a " " instead of a ", " at the end.
            if len(WinningHousesList) - i == 1:
                begin, endee ="and ", " "
            print(f"{begin}{WinningHousesList[i][0]}{endee}", end="")
        print(f"all with a total of {WinningHousesList[i][1]} points.")

def assignHouse(character, questions):
    """
    Determines a player's house by combining the character's personal attributes with their answers to the Sorting Hat's personality test during the sorting ceremony.

    The function calculates a score for each house: ﬁrst by taking into account the player's character attributes (each trait inﬂuences a speciﬁc house), then by adding points based on the answers to the test.  

    :param character: {dict} - The character dictionary
    :param questions: {list[tuple]} -  A list of tuples, each containing: (1) the question text, (2) a list of possible choices, and (3) the corresponding houses for each answer.
    :return house: {str} - The assigned house
   """
    #Initial house points with 0 each
    housePoints = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    #Attributes influence (add to each the attribute multiplied by 2)
    attributes = character["Attributes"]
    housePoints["Gryffindor"] += attributes["Courage"]* 2
    housePoints["Slytherin"] += attributes["Ambition"]*2
    housePoints["Hufflepuff"] += attributes["Loyalty"]*2
    housePoints["Ravenclaw"] += attributes["Intelligence"]*2 

    #Questions influence
    for question, choices, houses in questions :
        choice = askChoice(question, choices)
        selectedHouse = houses[choice - 1] 
        housePoints[selectedHouse] += 10  #Each answer gives 10 points to the corresponding house
     
    #Determine the house with the highest points
    assignedHouse = max(housePoints, key=housePoints.get)
    return assignedHouse
    

#%%###=== Program ===####
if __name__ == "__main__":
    hgg_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 25}
    updateHousePoints(hgg_houses, "Gryffindor", 25)
    updateHousePoints(hgg_houses, "Slytherin", 15)
    updateHousePoints(hgg_houses, "Huuuuupplllelelepuff", -250)
    updateHousePoints(hgg_houses, "Hufflepuff", -5)
    displayHouses(hgg_houses)
    print()

    displayWinningHouse(hgg_houses)

    #Example of assignHouse function
    from hogwarts.universe.character import initCharacter
    Harry_the_goat = initCharacter("Potter", "Harry", {"Courage": 1000, "Intelligence": 0, "Loyalty": 9, "Ambition": 7})

    questions = [ 
    ( 
        "You see a friend in danger. What do you do?", 
        ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ), 
    ( 
        "Which trait describes you best?", 
        ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ), 
    ( 
        "When faced with a difficult challenge, you...", 
        ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", 
         "Analyze the problem"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ) 
]

    assignedHouse = assignHouse(Harry_the_goat, questions)
    print(f"Harry the goat has been assigned to {assignedHouse}.")