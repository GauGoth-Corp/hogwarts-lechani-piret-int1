from universe.house import *
from utils import input_utils as IU
from universe.character import *

contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


def updateHousePoints(houses, houseName, points, msg=True):

    if houseName not in houses:
        print(f"The House '{houseName}' does not exist.")
    else:
        houses[houseName] += points
        if msg:
            if points >= 0:
                print(f"** {houseName} has been awarded +{points} points! **")
            else:
                print(f"** {houseName} has been deducted {-points} points! **")

def displayHouses(houses):

    print("== Current House Points: ==") 
    for house, points in houses.items() :
        print(f"{house}: {points} points")

def displayWinningHouse(houses):

    winningHouseScore = houses["Gryffindor"]

    for key, value in houses.items():
        if value > winningHouseScore:
            winningHouseScore = value


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

            if len(WinningHousesList) - i == 1:
                begin, endee ="and ", " "
            print(f"{begin}{WinningHousesList[i][0]}{endee}", end="")
        print(f"all with a total of {WinningHousesList[i][1]} points.")


def assignHouse(character, questions):

    housePoints = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}


    attributes = character["Attributes"]
    housePoints["Gryffindor"] += attributes["Courage"]* 2
    housePoints["Slytherin"] += attributes["Ambition"]*2
    housePoints["Hufflepuff"] += attributes["Loyalty"]*2
    housePoints["Ravenclaw"] += attributes["Intelligence"]*2 


    counter = 1
    for q in questions:
        print(f"Q{counter}- ", end="")
        choice = IU.askChoice(q["question"], q["choices"]) 
        print()
        selectedHouse = q["houses"][choice - 1] 
        housePoints[selectedHouse] += 10 
        counter += 1
    

    assignedHouse = "Gryffindor"
    maxScore = 0
    for house, score in housePoints.items():
        if score > maxScore:
            assignedHouse = house
            maxScore = score


    print("== Summary of scores ==")
    for house, score in housePoints.items():
        print(f"{house}: {score} points") 
    return assignedHouse
    


if __name__ == "__main__":
    hgg_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 25}
    updateHousePoints(hgg_houses, "Gryffindor", 25)
    updateHousePoints(hgg_houses, "Slytherin", 15)
    updateHousePoints(hgg_houses, "Huuuuupplllelelepuff", -250)
    updateHousePoints(hgg_houses, "Hufflepuff", -5)
    displayHouses(hgg_houses)
    print()

    displayWinningHouse(hgg_houses)


    from universe import character as carac
    Harry_the_goat = carac.initCharacter("Potter", "Harry", {"Courage": 5, "Intelligence": 5, "Loyalty": 5, "Ambition": 5})


    questions = IU.loadFile("data/sorting_ceremony_questions.json")

    print(f"\n=== Here's the time to being assigned to your Hogwarts' House! Here is a quizz. Answer the questions and discover your House! ===\n")
    assignedHouse = assignHouse(Harry_the_goat, questions)
    print(f"{Harry_the_goat['First Name']} {Harry_the_goat['Last Name']} has been assigned to {assignedHouse}!")