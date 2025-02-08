"""
This file holds the controller for the Main Menu
"""
import sys
from exceptions import ItemNotFoundError
from MainMenu.main_menu_model import MainMenuModel
from MainMenu.main_menu_view import MainMenuView

class MainMenuController:
    """
    This class contains the controller for the Main Menu
    """

    def __init__(self):
        self._model = MainMenuModel()
        self._view = MainMenuView(
            {key + 1: value for key, value in enumerate(self._model.get_games_list())}
        )
        self._view.user_input_signal.connect(self.on_user_input)

    def run(self):
        """
        Shows the Main Menu
        """
        self._view.show_welcome()
        self._view.show()

    def on_user_input(self, user_input):
        """
        Handles the user's input on which game to play.
        """
        if user_input.lower() == "q":
            self._view.show_exit()
            sys.exit()
        try:
            if user_input.isnumeric():
                controller = self._model.get_game_by_index(int(user_input) - 1)
            else:
                controller = self._model.get_game_by_name(user_input)
        except ItemNotFoundError as exception:
            print(exception)
        except ValueError as exception:
            # This shouldn't occur because of the isnumeric function
            print(exception)
        else:
            game = controller()
            game.run()
        finally:
            self._view.show()
