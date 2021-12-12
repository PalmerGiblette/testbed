
import math
from game.actor import Actor
from game import constants
from game.point import Point
from game.artifact import Artifact


#Manages the health amount on the screen, and tallies up amount recieved, or reduced
class Health(Actor):
    def __init__(self):
        super().__init__()

        self._health = 0
        self.set_height(constants.SCORE_Y)
        self.set_width(constants.SCORE_X)
        self.set_position(Point(constants.SCORE_X,constants.SCORE_Y))
        

    def add_health(self, health):
        self._health += health
        self.set_text(f"Health: {self._health}")
    
    # def deduct_health(self, health):
    #     self._health -= health
    #     self.set_text(f"health: {self._health}")

    def set_health(self, health):
        self._health = health + self._health

    def get_health(self):
        return self._health
