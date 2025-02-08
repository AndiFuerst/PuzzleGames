"""
This file holds the controller for a Parent class of games
"""

class BaseGame:

    name = "BaseGame"
    """
    This class contains the controller a Parent class of games
    """
    def __init__(self):
        pass

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
        return BaseGame.name
