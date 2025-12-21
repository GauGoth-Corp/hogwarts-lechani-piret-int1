##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. 0.1 #################################
#### INPUT UTILS #############################################
#### 27/11/2025 - 21/12/2025 #################################
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
    
    choice = askNumber("Make your choice: ", 1, len(options))
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

def loadAsciiArt(path):
    """
    Loads an ASCII art from a text file. Raises an exception if an error occurs during the process. 

    :param path: {str} - file path of the text file to load
    :return asciiArt: {str} - ASCII art content
    """

    try: 
        with open(path, "r", encoding="utf-8") as f:
            asciiArt = f.read()
            f.close()
            return asciiArt
    except Exception as e:
        return f"An error occured while trying to read the file {path}. [Error: {e}]\nPlease try again later or contact us at the adress {contactSupportURL} for help."

def encryptText(text, key):
    """
    This function is used to encrypt text in order to store sensitive game information (like pswds, secret spells, etc.)
    Based on the Caesar & Vigenère cipher methods.
    
    :param text: {str} - Text to encrypt
    :param key: {list[int]} - Encryption key - WARNING: len(key) = len(text); 1 <= key[i] <= 9

    :return: {str} - Encrypted text
    """

    #PROCESS
    text = text
    key = key
    Crypted=""
    for i in range(len(text)):
        asciiPos = ord(text[i])
        Crypted+= chr(asciiPos+key[i])

    #OUTPUT
    return Crypted

def decryptText(encryptedText, key):
    """
    This function is used to decrypt text in order to retrieve sensitive game information 
    Based on the Caesar & Vigenère cipher methods.
    
    :param encryptedText: {str} - Text to decrypt
    :param key: {list[int]} - Decryption key - WARNING: len(key) = len(encryptedText); 1 <= key[i] <= 9

    :return: {str} - Decrypted text
    """

    #Different from encryptText only in the processing part (subtraction instead of addition)

    #PROCESS
    text = encryptedText
    key = key
    Decrypted=""
    for i in range(len(text)):
        asciiPos = ord(text[i])
        Decrypted+= chr(asciiPos - key[i])

    #OUTPUT
    return Decrypted

#%%###=== Program ===####
if __name__ == "__main__":
    ###Functions tests:

    print("Loaded JSON: \n", loadFile("data/houses.json"))

    encrypted = encryptText("Hello World!", [1,2,3,4,5,6,7,8,9,10,11,12])
    print("Encrypted:", encrypted)
    decrypted = decryptText(encrypted, [1,2,3,4,5,6,7,8,9,10,11,12])
    print("Decrypted:", decrypted)
    
    print(askChoice("What do u choose?", ["Die", "Live", "None."]))
    print(askText("Enter text: "))
    print(askNumber("Enter a number between 1 and 10: ", 1, 10))
    print(askNumber("Enter a number greater than 5: ", 5))
    print(askNumber("Enter a number lower than 20: ", None, 20))
    print(askNumber("Enter any number: "))
    