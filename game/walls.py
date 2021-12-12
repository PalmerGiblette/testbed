

from game.actor import Actor
from game import constants


#Creates walls that appear on the screen
class Walls(Actor):
    def __init__(self):
        super().__init__()

        self._description = ""
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)