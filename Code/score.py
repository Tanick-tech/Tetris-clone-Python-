from settings import *
from os.path import join
import pygame as pg

class Score:
    def __init__(self):
        self.surface = pg.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        # The rectangle method: use to place an object at special coordinates (some adjusting if required)
        self.display_surface = pg.display.get_surface()

        # Fonts
        self.font = pg.font.Font(join('..','graphics','Russo_One.ttf'), 30)

        # Increment
        self.increment_height = self.surface.get_height() / 3

        # Data
        self.score = 0
        self.level = 1
        self.lines = 0

    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white') #render (text, enter alias text, color)
        text_rext = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rext)
    def run(self):
        self.surface.fill(GRAY)
        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height/ 2 + i*self.increment_height
            self.display_text((x, y), text)

        self.display_surface.blit(self.surface, self.rect)
        pg.draw.rect(self.display_surface, LINE_COLOUR, self.rect, 2, 2)