from settings import *

class Game:
    def __init__(self):
        # General - creating layer on top of the background
        self.surface = pg.Surface ((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pg.display.get_surface()
        self.rect = self.surface.get_rect(topleft =(PADDING, PADDING))
        #line surface:
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120) # Transparency: 0 --> 255 (no transparency)

    def run(self):
        self.surface.fill(GRAY)
        # drawing
        self.draw_grid()

        self.display_surface.blit (self.surface, (PADDING, PADDING))
        """
        blit: block image transfer - fancy way of saying 1 surface on 1 surface
        blit (the object, position)
        """
        # pg.draw.rect(surface, color, rect, width, corner radius)
        pg.draw.rect(self.display_surface, LINE_COLOUR, self.rect, 2, 2)


    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            # pg.draw.line(surface, color, start_pos, end_pos, (width))
            pg.draw.line(self.line_surface, LINE_COLOUR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pg.draw.line(self.line_surface, LINE_COLOUR, (0, y), (self.surface.get_width(), y), 1)
        self.surface.blit(self.line_surface, (0, 0))