"""
This file holds the Model for the Main Menu
"""

from Games.base_game import BaseGame
from exceptions import ItemNotFoundError

class MainMenuModel:
    """
    This class holds the Model for the Main Menu
    """
    def __init__(self):
        self._games = [BaseGame]

    def get_games_list(self):
        """
        Returns a list of all the games within the application
        
        Returns:
            list: A list of strings representing the games' names
        """
        return list(map(lambda controller: controller.get_name(), self._games))

    def get_game_count(self):
        """
        Returns the quantity of all the games within the application
        
        Returns:
            int: the quantity of all games within the application
        """
        return len(self._games)

    def get_game_by_index(self, index):
        """
        Returns the GameController type of the game at the index given
        Raises an error if not found.

        Args:
            index (int): The index of the GameController being looked for.
        
        Returns:
            GameController: GameController type of the game at the index given
        """
        if index >= len(self._games):
            raise ItemNotFoundError(index, "MainMenuModel")
        return self._games[index]

    def get_game_by_name(self, name):
        """
        Returns the GameController type of the game with the name given
        Raises an error if not found

        Args:
            name (str): The name of the GameController being looked for.
        
        Returns:
            GameController: GameController type of the game with the name given
        """
        for game in self._games:
            if game.get_name().lower() == name.lower():
                return game
        raise ItemNotFoundError(name, "MainMenuModel")
