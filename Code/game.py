from settings import *

class Game:
    def __init__(self):
        # General - creating layer on top of the background
        self.surface = pg.Surface ((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pg.display.get_surface()

    def run(self):
        self.display_surface.blit (self.surface, (PADDING, PADDING))
        """
        blit: block image transfer - fancy way of saying 1 surface on 1 surface
        blit (the object, position)
        """
