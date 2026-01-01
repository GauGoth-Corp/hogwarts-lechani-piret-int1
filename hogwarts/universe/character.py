from universe.house import *
from utils import input_utils as IU
from universe.character import *


contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"



def initCharacter(lastName, firstName, attributes):

    character = {}

    character["Last Name"] = lastName
    character["First Name"] = firstName
    character["Money"] = 100 
    character["Inventory"] = [] 
    character["Spells"] = [] 
    character["Attributes"] = attributes

    return character

def displayCharacter(character):

    print(f"== {character['First Name']} {character['Last Name']} profile ==")
    for key, value in character.items():
        if type(value) == dict:
            print(f"{key}: ")
            for dictKey, dictValue in value.items():
                print(f"    - {dictKey}: {dictValue}")
        elif type(value) == list:
            print(f"{key}: ")
            if value:
                print(f"    - " + "\n    - ".join(value))
        else:
            print(f"{key}: {value}")

def modifyMoney(character, amount, displayMsg=False):

    character["Money"] += amount
    if displayMsg:
        if amount >= 0:
            print(f"** You have received {amount} Galleons! **")
        else: 
            print(f"** You have lost {-amount} Galleons... **") 
    return character

def addItem(character, key, item ,displayMsg=False):

    if key in character:
        if type(character[key]) != list:
            print(f"[Error:] The key '{key}' is not a list.")
            return character
        
        character[key].append(item)
        if displayMsg:
            print(f"** You have obtained the item: {item}! **")
        return character
    else:
        print(f"[Error:] The key '{key}' does not exist.")
        return character
    
def incrementAttribute(character, attributeName, amount=1, displayMsg=False):

    if attributeName in character["Attributes"]:
        character["Attributes"][attributeName] += amount

        if displayMsg:
            if amount >= 0:
                if amount >= 2:
                    suffix = "s"
                else:
                    suffix = ""
                print(f"** Your {attributeName} has increased by {amount} point{suffix}! **")
            else:
                if -amount >= 2:
                    suffix = "s"
                else:
                    suffix = ""
                print(f"** Oh no, your {attributeName} has decreased by {-amount} point{suffix}... **")
    else:
        print(f"[Error] The attribute '{attributeName}' does not exist.")
    
    return character

def newExit():

    raise SystemExit

def endAdventure(character, msg):

    print(msg)
    print("\nFinal character profile:")
    displayCharacter(character)
    print()
    cheat = input(f"This is the end of your adventure. Press enter to exit... ")

    try:
        key = IU.loadFile("data/sensitive_info.json")["easter_egg_pswd_key"]
    

        if IU.encryptText(cheat, key) == "Ig}H{}s%L{~x0":
            print("\n** Congratulations! You've discovered the secret cheat code easter egg! Here is a little reward: you win 1,000,000 Galleons! **")
            character = modifyMoney(character, 1000000, True)
            print()
            print("Everyone thought you were done, but suddendly you take a great breath and get back on your feet. How mysterious is magic, isn't it?")
            print(f"Welcome back, {character['First Name']} {character['Last Name']}!")
            print()

        else:
            newExit()
    except TypeError:
        print(f"An error occured while trying to read the file 'data/sensitive_info.json'.\nPlease try again later or contact us at the adress {contactSupportURL} for help.")
        newExit()


        

if __name__ == "__main__":

    Harry_the_goat = initCharacter("Potter", "Harry", {"Courage": 1000, "Intelligence": 0, "Loyalty": 9, "Ambition": 7})
    displayCharacter(Harry_the_goat)

    print("\nModifying money...")
    Harry_the_goat = modifyMoney(Harry_the_goat, -1000)
    displayCharacter(Harry_the_goat)

    print("\n\nTesting the addItem() function...")
    Harry_the_goat = addItem(Harry_the_goat, "Inventory", "Blaster Blastech E-11")
    list_items = ["Green Light Saber", "Comlink", "Thermal Detonator", "Datapad", "Vibroblade", "Medpac", "Poodoo", "64x Dirt", "64x Cobblestone", "64x Cobblestone", "A beautiful young Twi'lek slave", "64x Cobblestone", "38x Cobblestone", "47x Dark Oak Planks"]
    for item in list_items:
        Harry_the_goat = addItem(Harry_the_goat, "Inventory", item) 
    Harry_the_goat = addItem(Harry_the_goat, "Spells", "Abracadabite")
    Harry_the_goat = addItem(Harry_the_goat, "Spells", "Expelliarmus")
    displayCharacter(Harry_the_goat)