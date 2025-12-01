##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### INPUT UTILS #############################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################
"""
Utility functions for properly managing user input.
"""

#%%###=== Modules Import ===####
import json
#### Package modules import ####


#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


#%%###=== Module (functions) ===####
def askText(msg):
    """
    Asks the user to enter text
    Prompt again whenever the text entered is invalid

    :param msg: {str} - Input message display
    :return txt: {str} - Text entered
    """

    txt = input(msg).strip() #Removes spaces at the beginning and at the end of the text
    return txt

def askNumber(msg, minVal=None, maxVal=None):
    """
    Asks the user to enter an integer
    Prompt again whenever the text entered is invalid
    
    :param msg: {str} - Input message display
    :param minVal: {int} ? - Minimum value
    :param maxVal: {int} ? - Maximum value
    :return nb: {int} - Integer entered
    """

    valid = False
    while not valid:
        try:
            nb = int(input(msg))
            if minVal!=None and nb < minVal:
                print(f"Please enter an integer greater or equal to {minVal}!\n")
            elif maxVal!=None and nb > maxVal:
                print(f"Please enter an integer lower or equal to {maxVal}!\n")
            else:
                valid = True
        except ValueError:
            if minVal==None and maxVal == None:
                print("Please enter a valid integer!\n")
            elif minVal!=None and maxVal==None:
                print(f"Please enter an integer greater or equal to {minVal}!\n")
            elif minVal==None and maxVal!=None:
                print(f"Please enter an integer lower or equal to {maxVal}!\n")
            elif minVal!=None and maxVal !=None:
                print(f"Please enter an integer between {minVal} and {maxVal} (included)!\n")
        
    return nb

def askChoice(msg, options):
    """
    Displays a numbered list of options and prompts the user to make a selection by entering the corresponding number

    :param msg: {str} - Input message display
    :param options: {list[str]} - List of different options
    :return choice: {int} - Number corresponding to the selected option

    """
    print(f"{msg}")
    for i in range(len(options)):
        print(f"    {i+1}. {options[i]}")
    print()
    
    choice = askNumber("Choose you fate: ", 1, len(options))
    return choice

def loadFile(path):
    """
    Loads a JSON file contents. Raises an exception if an error occurs during the process.

    :param path: {str} - file path of the JSON file to load
    :return jsonList: {list} - JSON contents organized in lists
    """
    try: 
        with open(path, "r", encoding="utf-8") as f:
            jsonList = json.load(f)
            f.close()
            return jsonList
    except Exception as e:
        return f"An error occured while trying to read the file {path}. [Error: {e}]\nPlease try again later or contact us at the adress {contactSupportURL} for help."

#%%###=== Program ===####
if __name__ == "__main__":
    ###Functions tests:

    print("Loaded JSON: \n", loadFile("hogwarts/data/houses.json"))

    
    print(askChoice("What do u choose?", ["Die", "Live", "None."]))
    print(askText("Enter text: "))
    print(askNumber("Enter a number between 1 and 10: ", 1, 10))
    print(askNumber("Enter a number greater than 5: ", 5))
    print(askNumber("Enter a number lower than 20: ", None, 20))
    print(askNumber("Enter any number: "))
    