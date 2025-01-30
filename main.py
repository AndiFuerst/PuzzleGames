"""
Main File to start PuzzleGames.
"""

import sys
from MainMenu.main_menu_controller import MainMenuController

if __name__ == "__main__":
    mmc = MainMenuController()
    mmc.run()
    sys.exit(0)