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
        self._view.show_welcome()
        self._view.show()
    
    def on_user_input(self, user_input):
        """
        Handles the user's input on which game to play.
        """
        test = self._model.get_game_by_name(user_input)
        print(type(test))
        # if user_input.lower() == "q":
        #     self._view.show_exit()
        #     return # Exit
        # try:
        #     if int(user_input) > 0 and int(user_input) <= self._model.get_game_count():
        #         game = self._model.get_game(int(user_input))
        #         game.run()
        #     else:
        #         self._view.show_invalid_input(user_input)
        #         self._view.show()
        # except:
        #     self._view.show_invalid_input(user_input)
        #     self._view.show()
