"""
This file holds the view for the Base Game
"""

from PyQt5.QtCore import pyqtSignal, QObject

class BaseGameView(QObject):
    """
    This class holds the view for the Base Game
    """
    options_selected_signal = pyqtSignal(str)
    return_to_game_menu_signal = pyqtSignal()
    game_input_signal = pyqtSignal()

    def __init__(self, game_name):
        super().__init__()
        self._game_name = game_name

    def show_welcome(self):
        """
        Displays a welcome message.
        """
        print(f"Let's Play {self._game_name}!!!")

    def show_menu_options(self, options):
        """
        Displays the menu options to the player and recieves input from the player.

        Args:
            options (list): the list of selections that user can choose from
        """
        print("Select an Option from the list below by typing it's number (or type 'q' at anytime to leave):")
        for index in options: 
            print(f"{index}: {options[index]}")
        self.options_selected_signal.emit(input())
    
    def show_scores_screen(self, scores):
        """
        Displays the high scores to the player and waits until the player wants to leave.

        Args:
            scores (dict): a dictionary representing the high scores for the given game.
                (key: player name (str), value: score (int))
        """
        print(f"Highscores for {self._game_name}!!!!")
        for player in scores: 
            print(f"{player}: {scores[player]}")
        print("Press <Enter> to return to the menu.")
        input()
        self.return_to_game_menu_signal.emit()

    def show_how_to_screen(self, how_to):
        """
        Displays the how-to message to the player and waits until they want to leave.

        Args:
            how_to (str): a string message detailing how to play the game.
        """
        print(f"How to Play {self._game_name}:")
        print(how_to)
        print("Press <Enter> to return to the menu.")
        input()
        self.return_to_game_menu_signal.emit()

    def show(self, game_board):
        """
        Displays the game board and waits for user input.

        Args:
            game_board (str): a string representing the game board
        """
        print(f"{self.game_name} (Press 'q' at any time to quit.)")
        print(game_board)
        self.game_input_signal.emit(input())

    def show_exit(self):
        """
        Displays a goodbye message
        """
        print(f"Thanks for Playing {self.game_name}!")

    def show_invalid_input(self, invalid_input, message=None, valid_options=None, pattern=None):
        """
        Displays a message to inform the user that they input an invalid input.

        Args:
            message (str): An additional message to give further context to the user on why their
                input was invalid.
            valid_options (dict): A dictionary representing the valid options a user can input. 
                (key: option (str), value: meaning (str))
            pattern (str): A string representing the way a user must enter their input. 
        """
        print(f'Sorry, "{invalid_input}" is not a valid option.')
        if message is not None:
            print(message)
        if valid_options is not None:
            print("The valid options are listed below:")
            for option in valid_options:
                print(f"{option}: {valid_options[option]}")
        if pattern is not None:
            print(f"The input should be specified in the following pattern: {pattern}")
