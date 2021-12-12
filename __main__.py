import random
import math
import sys

from pyray import close_window

from game import constants
from game import trees
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.artifact import Artifact
from game.hero import Hero
from game.guard import Guard
from game.score import Score
from game.background import Background
from game.audio_service import AudioService
from game.walls import Walls
from game.trees import Trees
from game.door import Door
from game.health import Health
from game.supplies import Supplies

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    marquee = Actor()
    marquee.set_text("")
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]



    # Creates, and displays health amount on the screen
    health = Health()
    health.add_health(5)
    health.set_position(Point(500,0))
    cast["health"] = [health]

    # Creates, and places on screen, a health kit to heal if picked up the player
    supply = []
    supplies = Supplies()
    X = random.randint(5,400)
    Y = random.randint(480,495)
    supplies.set_position(Point(X,Y))
    supplies.set_height(15)
    supplies.set_width(15)
    supplies.set_image(constants.SUPPLY_AID)
    supply.append(supplies)
    cast["supplies"] = supply

        

    #Places and creates the player on the screen in the middle of the screen.
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    hero = Hero()
    hero.set_height(20)
    hero.set_width(20)
    
    hero.set_image(constants.HERO_RETRO)
    hero.set_position(position)
    cast["Hero"] = [hero]


    #Displays the current score on the screen
    score = Score()
    score.add_points(0)
    
    score.set_position(Point(400,0))
    cast["score"] = [score]

    #Creates a vertical wall on the screen.
    wall_1 = Walls()
    wall_1.set_height(150)
    wall_1.set_width(20)
    wall_1.set_position(Point(220,0))
    wall_1.set_image(constants.WALL_STONE_V)

    #Creates a horizontal wall on the screen
    wall_2 = Walls()
    wall_2.set_height(20)
    wall_2.set_width(220)
    wall_2.set_position(Point(0,200))
    wall_2.set_image(constants.WALL_STONE_H)
    cast["Walls"] = [wall_1,wall_2]

    #Creates a door on the screen, not currently in use. Going to be a door to load new area
    door = Door()
    door.set_height(30)
    door.set_width(25)
    door.set_position(Point(400,150))
    door.set_image(constants.NORTH_DOOR)
    cast["Door"] = [door]

    # Generates a forest
    trees = []
    for t in range(constants.TREES):

        # description = constants.TREE_TEXT[t]

        x = random.randint(5, 550)
        y = random.randint(450, 800)
        position = Point(x,y)

        tree = Trees()
        # tree.set_description(description)
        tree.set_height(60)
        tree.set_width(15)
        
        tree.set_image(constants.TREE_1)
        tree.set_position(position)
        trees.append(tree)
        cast["tree"] = trees

    #Generates chests for the player to collect
    artifacts = []
    for n in range(constants.CHESTS):
       
        description = constants.CHEST_TEXT[n]
        
        x = random.randint(50, 150)
        y = random.randint(50, 150)
        position = Point(x, y)

        artifact = Artifact()
        artifact.set_description(description)
        artifact.set_height(35)
        artifact.set_width(50)

        artifact.set_image(constants.CHEST_IMAGE)
        artifact.set_position(position)
        artifacts.append(artifact)
        cast["artifact"] = artifacts
    
    #Creates enemies, guards that protect the chest, hurts or lowers health if touched
    guard = []
    for i in range(constants.GUARDS):
        
        
        
        x = random.randint(200, 400)
        y = random.randint(200, 400)
        position = Point(x, y)

        guards = Guard()
        
        guards.set_description(description)
        guards.set_height(30)
        guards.set_width(20)
        guards.set_image(constants.GUARD_BAD)
        
        # artifact.set_text(text)
        guards.set_position(position)
        guard.append(guards)
        cast["guards"] = guard
    

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    output_service.open_window("Dungeon Crawl");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
