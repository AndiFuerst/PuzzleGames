"""
This file holds the controller for the Main Menu
"""
from MainMenu.main_menu_model import MainMenuModel
from MainMenu.main_menu_view import MainMenuView

class MainMenuController:
    """
    This class contains the controller for the Main Menu
    """
    def __init__(self):
        self._model = MainMenuModel()
        self._view = MainMenuView({key + 1: value for key, value in enumerate(self._model.get_games_list())})
        self._view.user_input_signal.connect(self.on_user_input)

    def run(self):
        """
        Shows the Main Menu
        """
        self._view.show()
    
    def on_user_input(self, user_input):
        print(user_input)