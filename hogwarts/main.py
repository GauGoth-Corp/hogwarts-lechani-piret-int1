##############################################################
#### Authors: Lisa Lechani & Gautier Piret ###################
#### Hogwarts Game - v. Bêta #################################
#### MAIN ####################################################
#### 27/11/2025 - 28/11/2025 #################################
#### Copyright (c) 2025 GauGoth Corp. All Rights reserved ####
##############################################################

### CONVERT THIS PROJECT TO EXE WITH PYINSTALLER USING THE FOLLOWING COMMAND:
# python -m pyinstaller --onefile --noconsole --icon=hgg-icon.ico hogwarts/main.py

### WARNING: ###
# PyCharm runs the program from the file directory, not from the main directory. 
# Then, we have to set this parameter in VSCode to emulate the Pycharm behaviour:
# "python.terminal.executeInFileDir": true

"""
Hogwarts Game is a text-based adventure game set in the Harry Potter universe. This project is developed as part of a Python programming project at our school Efrei Paris.

Developed by Aomm-lgtm & GauGoth Corp.

For more information, check our GitHub repository: 

https://github.com/GauGoth-Corp/hogwarts-lechani-piret-int1
"""
#test

#%%###=== Modules Import ===####
#### Package modules import ####
from menu import launchMenuChoice

#%%###=== Global variables ===###
contactSupportURL = "http://gaugoth.corp.free.fr/credits/contact/?subject=Hogwarts%20Game%20Support%20Request"

#%%###=== Module (functions) ===####

        
#%%###=== Program ===####
if __name__ == "__main__":
    launchMenuChoice()