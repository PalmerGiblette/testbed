

from game.actor import Actor
from game import constants
import random
class Background(Actor):
    """
    Defines a background. Inherits from Actor, and adds a description.
    """
    def __init__(self):
        super().__init__()

        self._description = ""
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)
        # self.set_image(constants.MAP_IMAGE)
    
    # def set_tile(self):
    #     tile_select = 5
    #     self.random.randint(tile_select)

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def has_description(self):
        """
        Returns true if the description is not "".
        """
        return self._description != ""