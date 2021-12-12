from game.actor import Actor
from game import constants


#The Player class, lets the "hero" chooses size in main
class Hero(Actor):
    def __init__(self):
        super().__init__()

        self._health = 0
        self._description = ""
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)

    def set_health(self, health):
        self._health = health + self._health

    def get_health(self):
        return self._health
