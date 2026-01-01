# Hogwarts Game - v. 0.1
<i>Version 0.1<br/>
**Testing file**<br/>
01/01/2026</i>

*********************************************************************

Thank you for downloading Hogwarts Game (v. 0.1).

-----------------------------
Hogwarts Game is a text-based adventure game set in the Harry Potter universe.
To learn more about the game and how to play it, please refer to the [[README.md](README.md)] file.

## Control, Testing & Validation Summary

### Input & Error Management
- All inputs the player is asked to provide are managed in the `input_utils.py` module. This allows to avoid every crashes due to invalid inputs.
- Input types are handled using try/except blocks to avoid crashes ('invalid type!')
- Invalid integer inputs are used to re-prompt the player until a valid input is provided ('more', 'less')
- Empty strings are not accepted

### Known Bugs
- No known bugs at the moment. If you find one, please [contact us](http://gaugoth.corp.free.fr/en/credits/contact/?subject=Hogwarts%20Game%20v.%200.1%20bug%20report).
- In some rare cases, if the game have been missed installed, some `.json` files containing important data may not be found. In this case, an error message is displayed using a try/except block. Please then re-install properly the game following the instructions in the [[README.md](README.md#installation)] file.

### Testing Strategies
- Each module was tested separately during game development (section `if __name__ == "__main__":` at the end of each module and file `__debug__.py`). 
- Numerous games were played, each time making different choices to test the various paths and identify any bugs.

### Screenshots
Here are some screenshots of the game during testing:


![menu.png](screenshots/menu.png)
_Game Menu screen_

![character-creation-1.png](screenshots/character-creation-1.png)
_Character Creation screen - the attributes are well stored_

![character-creation-2.png](screenshots/character-creation-2.png)
_Character Creation screen - other choices lead to different outcomes_

![shops-choices-1.png](screenshots/shops-choices-1.png)
_Shop screen - supplies are well bought and stored in the inventory_

![shops-choices-2.png](screenshots/shops-choices-2.png)
_Shop screen - other choices lead to different outcomes! :)_

![houses-test.png](screenshots/houses-test.png)
_House selection screen - the sorting hat works well_

![dragon-fight-round-1.png](screenshots/dragon-fight-round-1.png)
_Dragon fight - round 1: the spells you have already learned influence the fight!_

![the-end.png](screenshots/the-end.png)
_The End screen - the adventure is completed successfully_

![restart-game.png](screenshots/restart-game.png)
_Restart Game screen - the player can choose to restart the game. The previous game data is successfully cleared_