"""
This file holds the view for the Main Menu
"""

from PyQt5.QtCore import pyqtSignal, QObject

class MainMenuView(QObject):
    """
    This class holds the view for the Main Menu
    """

    user_input_signal = pyqtSignal(str)

    def __init__(self, game_dict):
        super().__init__()
        self._game_dict = game_dict

    def show(self):
        """
        Displays the main menu for a user to select a game.
        """
        print("Welcome to Puzzle Games!!!")
        print("Select a Game from the list below by typing it's number (or type 'q' at anytime to leave):")
        for index in self._game_dict: 
            print(f"{index}: {self._game_dict[index]}")
        self.user_input_signal.emit(input())