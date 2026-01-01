import json

contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


def askText(msg):

    txt = input(msg).strip()
    return txt

def askNumber(msg, minVal=None, maxVal=None):

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

    print(f"{msg}")
    for i in range(len(options)):
        print(f"    {i+1}. {options[i]}")
    print()
    
    choice = askNumber("Make your choice: ", 1, len(options))
    return choice

def loadFile(path):
    
    try: 
        with open(path, "r", encoding="utf-8") as f:
            jsonList = json.load(f)
            f.close()
            return jsonList
    except Exception as e:
        return f"An error occured while trying to read the file {path}. [Error: {e}]\nPlease try again later or contact us at the adress {contactSupportURL} for help."

def loadAsciiArt(path):

    try: 
        with open(path, "r", encoding="utf-8") as f:
            asciiArt = f.read()
            f.close()
            return asciiArt
    except Exception as e:
        return f"An error occured while trying to read the file {path}. [Error: {e}]\nPlease try again later or contact us at the adress {contactSupportURL} for help."

def encryptText(text, key):


    text = text
    key = key
    Crypted=""
    for i in range(len(text)):
        asciiPos = ord(text[i])
        Crypted+= chr(asciiPos+key[i])


    return Crypted

def decryptText(encryptedText, key):

    text = encryptedText
    key = key
    Decrypted=""
    for i in range(len(text)):
        asciiPos = ord(text[i])
        Decrypted+= chr(asciiPos - key[i])


    return Decrypted


if __name__ == "__main__":


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
    