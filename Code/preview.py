# Similar to score.py
from settings import *

class Preview:
    def __init__(self):
        self.surface = pg.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surface.get_rect(topright =(WINDOW_WIDTH - PADDING,PADDING ))
        self.display_surface = pg.display.get_surface()

    def run(self):
        self.display_surface.blit (self.surface, self.rect)