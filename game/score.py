import math
from game.actor import Actor
from game import constants
from game.point import Point
from game.artifact import Artifact

#Manages the score on the top of the screen, and tallies points when recieved
class Score(Actor):
    def __init__(self):
        super().__init__()

        self._points = 0
        self.set_height(constants.SCORE_Y)
        self.set_width(constants.SCORE_X)
        self.set_position(Point(constants.SCORE_X,constants.SCORE_Y))
        

    def add_points(self, points):
        self._points += points
        self.set_text(f"Points: {self._points}")

    def set_points(self, points):
        self._points = points + self._points

    def get_points(self):
        return self._points

    

