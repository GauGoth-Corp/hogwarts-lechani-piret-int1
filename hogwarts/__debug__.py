from random import choice, randint


from universe.house import *
from universe.character import *
from utils.input_utils import *
from chapters.chapter_1 import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from utils import input_utils as IU

from chapters.chapter_4 import *



contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"


if __name__ == "__main__":
    print("=== DEBUG MODE ACTIVATED ===\n\n")
    

    igor_character = {
                        "Last Name": "clair", 
                        "First Name": "obscur", 
                        "Money": 531,
                        "Inventory": ["Magic Wand", "Bus full of children", "House elf", "Potions Book", "Wizard Robe"],
                        "Spells": ["Lumos", "Alohomora", "Expelliarmus", "Stupefy", "Rictusempra"], #Avada Kedavra
                        "Attributes": {"Courage": 13, "Intelligence": 11, "Loyalty": 10, "Ambition": 13},
                        "House": "Slytherin"
                        }
    
    """
    hungarian_horntail = createDragonBoss("Hungarian Horntail", 250, 80, 30)


    igor_character["PV"] = 80
    igor_character["PE"] = 50
    
    dragonFightFirstRound(igor_character, hungarian_horntail)
    """
    
    startChapter3(igor_character)
