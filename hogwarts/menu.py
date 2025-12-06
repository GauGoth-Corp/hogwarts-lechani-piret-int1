##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### MENU ####################################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Main menu module for Hogwarts Game

Allows players to:

    - Start a new game

    - Load a saved game

    - View credits 

    - Contact support

    - Quit the game
"""


#%%###=== Modules Import ===####
#### Package modules import ####
from utils.input_utils import *
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import startChapter2

#from chapters.chapter_3 import start_chapter_3
#from chapters.chapter_4 import start_chapter_4
#from chapters.chapter_5_extension import start_chapter_5

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

def theEnd():
    """
    Ends the game and displays some little messages & ads...
    """

    print("================================ THE END ======================================")
    print("Congratulations! You have completed the Hogwarts Game adventure!")
    print("We hope you enjoyed this little game set in the magical world of Harry Potter.")
    print()
    print("== We will be back after this short advertisement break... ==")
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

#%%###=== Module (functions) ===####
def startGame():
    """
    Starts a new game of Hogwarts Game! 
    """

    print("============================== LOADING... ====================================")

    #initialization of differents dict:
    hgg_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    #Executes each chapter
    my_character = start_chapter_1()
    startChapter2(my_character, hgg_houses)
    #start_chapter_3()
    #start_chapter_4()
    #start_chapter_5()

    theEnd()


def loadSavedGame():
    """
    Loads a saved game
    """

    #print("============================== LOADING... ====================================")
    print("Load Game feature is not available in the Bêta version. Starting a new game...\n")
    startGame()

def displayCredits():
    """
    Displays credits of the game
    """

    print("================================ CREDITS ======================================")
    print("#### Hogwarts Game - v. Bêta ####")
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
    """
    Displays contact information
    """

    print("================================ CONTACT US ====================================")
    print(f"For any support request, please contact us at: {contactSupportURL}\n")
    print()
    input("Press Enter to return to the main menu... ")
    print()

def quitGame():
    """
    Quits the game
    """

    print("Thank you for playing Hogwarts Game. See you soon!\n")
    input("Press Enter to exit... ") 
    return False

def displayMainMenu():
    """
    Displays the main menu of Hogwarts Game! 
    """

    #%%###=== Main menu choices display ===####
    print("==============================================================================")
    print("                           Hogwarts Game - v. Bêta                            ")
    print("                     -----------------------------------                      ")
    print("                  A game developed by Aomm-lgtm & GauGoth Corp.               ")
    print("==============================================================================")
    print(loadAsciiArt("hogwarts/data/Ascii/Hogwarts-Castle-ASCII.txt"))

    print("==============================================================================")
    print("Copyright (c) 2025 GauGoth Corp. All Rights reserved.\n")
    choice = askChoice("================================== MAIN MENU =================================", ["Start Game", "Load Game", "Credits", "Contact Us", "Quit Game"])
    print()
    return choice

def launchMenuChoice():
    """
    Launches the main menu and handles user choices
    """

    onLoop = True
    while onLoop:
        choice = displayMainMenu()
        #%%###=== Main menu choices handling ===####
        if choice == 1: #Start Game
            startGame()

        elif choice == 2: #Load Game
            loadSavedGame()
        elif choice == 3: #Credits
            displayCredits()

        elif choice == 4: #Contact Us
            displayContactInfo()
        
        elif choice == 5: #Quit Game
            onLoop = quitGame()


        
#%%###=== Program ===####
if __name__ == "__main__":
    #theEnd()

    launchMenuChoice()