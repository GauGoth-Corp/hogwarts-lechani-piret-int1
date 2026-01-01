from utils.input_utils import *
from chapters.chapter_1 import startChapter1
from chapters.chapter_2 import startChapter2
from chapters.chapter_3 import startChapter3
from chapters.chapter_4 import startChapter4


contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

def theEnd():

    input("Press Enter to continue... ")
    print("\n\n\n")
    print("================================ THE END ======================================")
    print("Congratulations! You have completed the Hogwarts Game adventure!")
    print("We hope you enjoyed this little game set in the magical world of Harry Potter.")
    print()
    print("== We will be back after this short advertisement break... ==")
    input("Press Enter to continue... ")
    print()
    print("Is it finished? Not yet! Aomm-lgtm and GauGoth Corp. have developed several other projects:")
    print("     - Mini Golf 3D: The Pirate flag: a mini golf pirate adventure available on PC and mobile devices:")
    print("     PLAY NOW: http://gaugoth.corp.free.fr/games/\n")
    print("     - Password Manager CLI, A command line application password manager simulation:")
    print("     CHECK IT OUT: https://github.com/Aomm-lgtm/password_manager-CLI-\n")
    print("     - Galaxie Lointaine, a Star Wars website made by fans, for fans:")
    print("     VISIT: https://galaxielointaine.alwaysdata.net/\n")
    print("     - Auto Medias Downloader, a powerful medias downloading tool:")
    print("     CHECK IT OUT: https://github.com/GauGoth-Corp/Auto-Medias-Downloader\n")
    print("     - And other things: look for them on our website or our GitHub profiles!")
    print("     http://gaugoth.corp.free.fr/ | https://github.com/Aomm-lgtm | https://github.com/GauGoth-Corp")
    print()
    input("Press Enter to return to the main menu... ")
    print()


def startGame():

    print("============================== LOADING... ====================================")


    hgg_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}


    my_character = startChapter1()
    startChapter2(my_character, hgg_houses)
    startChapter3(my_character)
    startChapter4(my_character)


    theEnd()


def loadSavedGame():

    print("Load Game feature is not available in the 0.1 version. Starting a new game...\n")
    startGame()

def displayCredits():
    """
    Displays credits of the game
    """

    print("================================ CREDITS ======================================")
    print("#### Hogwarts Game - v. 0.1 ####")
    print("Hogwarts Game is a text-based adventure game set in the Harry Potter universe.")
    print("")
    print("Developed by Aomm-lgtm & GauGoth Corp.")
    print("")
    print("### HOW TO PLAY ###")
    print("Please refer to the REAMDE file available here: \nhttps://github.com/GauGoth-Corp/hogwarts-lechani-piret-int1")
    print()
    print("### LICENSE & CREDITS ###")
    print("Please refer to the LICENSE file available here: \nhttps://github.com/GauGoth-Corp/hogwarts-lechani-piret-int1?tab=License-1-ov-file")
    print()
    input("Press Enter to return to the main menu... ")
    print()

def displayContactInfo():

    print("================================ CONTACT US ====================================")
    print(f"For any support request, please contact us at: {contactSupportURL}\n")
    print()
    input("Press Enter to return to the main menu... ")
    print()

def quitGame():

    print("Thank you for playing Hogwarts Game. See you soon!\n")
    input("Press Enter to exit... ") 
    return False

def displayMainMenu():

    print("==============================================================================")
    print("                           Hogwarts Game - v. 0.1                            ")
    print("                     -----------------------------------                      ")
    print("                  A game developed by Aomm-lgtm & GauGoth Corp.               ")
    print("==============================================================================")
    print(loadAsciiArt("data/Ascii/Hogwarts-Castle-ASCII.txt"))

    print("==============================================================================")
    print("Copyright (c) 2025 GauGoth Corp. All Rights reserved.\n")
    choice = askChoice("================================== MAIN MENU =================================", ["Start Game", "Load Game", "Credits", "Contact Us", "Quit Game"])
    print()
    return choice

def launchMenuChoice():

    onLoop = True
    while onLoop:
        choice = displayMainMenu()

        if choice == 1:
            startGame()

        elif choice == 2:
            loadSavedGame()
        elif choice == 3:
            displayCredits()

        elif choice == 4:
            displayContactInfo()
        
        elif choice == 5:
            onLoop = quitGame()


        

if __name__ == "__main__":


    launchMenuChoice()