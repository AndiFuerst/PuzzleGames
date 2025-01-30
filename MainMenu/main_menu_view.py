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

    def show_welcome(self):
        """
        Displays a welcome message.
        """
        print("Welcome to Puzzle Games!!!")

    def show(self):
        """
        Displays the main menu for a user to select a game.
        """
        print("Select a Game from the list below by typing it's number (or type 'q' at anytime to leave):")
        for index in self._game_dict: 
            print(f"{index}: {self._game_dict[index]}")
        self.user_input_signal.emit(input())

    def show_exit(self):
        """
        Displays a goodbye message
        """
        print("Have a Good Day! Bye!")

    def show_invalid_input(self, invalid_input):
        """
        Displays a message to inform the user that they input an invalid input.
        """
        print(f'Sorry, "{invalid_input}" is not a valid option.')
