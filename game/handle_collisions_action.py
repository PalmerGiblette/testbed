import random
import time
from game import constants
from game.action import Action
from game.score import Score

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """      
        marquee = cast["marquee"][0] # there's only one
        Hero = cast["Hero"][0] # there's only one
        artifacts = cast["artifact"]
        score = cast["score"][0]
        marquee.set_text("")
        for artifact in artifacts:
            if self._physics_service.is_collision(Hero, artifact):
                description = artifact.get_description()
                marquee.set_text(description) 

                score.add_points(1)
                cast["artifact"].remove(artifact)


        Hero = cast["Hero"][0]
        guards = cast["guards"]
        health = cast["health"][0]
        
        for guard in guards:
            if self._physics_service.is_collision(Hero, guard):
                # description = guards.get_description()
                # marquee.set_text(description)

                health.add_health(-1)
                cast["guards"].remove(guard)
                
        Hero = cast["Hero"][0]
        supplies = cast["supplies"]
        health = cast["health"][0]
        
        for supply in supplies:
            if self._physics_service.is_collision(Hero, supply):
                # description = guards.get_description()
                # marquee.set_text(description)

                health.add_health(5)
                cast["supplies"].remove(supply)    

        


                
                
                