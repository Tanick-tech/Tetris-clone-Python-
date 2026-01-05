from settings import *

class Score:
    def __init__(self):
        self.surface = pg.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        # The rectangle method: use to place an object at special coordinates (some adjusting if required)
        self.display_surface = pg.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)