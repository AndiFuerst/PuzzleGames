"""
This file holds the Model for the Main Menu
"""

from GameA.game_a_controller import GameAController

class MainMenuModel:
    """
    This class holds the Model for the Main Menu
    """
    def __init__(self):
        self._games = [GameAController]

    def get_games_list(self):
        """
        Returns a list of all the games within the application
        
        Returns:
            list: A list of strings representing the games' names
        """
        return list(map(lambda controller: controller.get_name(), self._games))