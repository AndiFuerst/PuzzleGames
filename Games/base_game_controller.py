"""
This file holds the controller for a Parent class of games
"""

from Games.base_game_view import BaseGameView

class BaseGameController:
    """
    This class contains the controller a Parent class of games
    """

    name = "BaseGame"
    
    def __init__(self):
        self._view = BaseGameView(self.name)

    def run(self):
        """
        This method will handle running the game.
        """
        print("Running")

    @staticmethod
    def get_name():
        """
        Returns the Name for the Game

        Returns:
            str: The Name of the Game
        """
        return BaseGameController.name
