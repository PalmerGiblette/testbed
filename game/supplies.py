from game.actor import Actor
from game import constants



#Handles the creation and save of the supplies, or the healing kit for the player
class Supplies(Actor):
    def __init__(self):
        super().__init__()

        self._description = ""
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)