from game import constants
from game.action import Action
from game.output_service import OutputService
from game.actor import Actor

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        self._output_service.draw_image(0, 0, constants.MAP_IMAGE)
        for group in cast.values():

            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()
