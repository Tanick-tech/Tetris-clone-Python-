from settings import *
from random import choice

class Game:
    def __init__(self):
        # General - creating layer on top of the background
        self.surface = pg.Surface ((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pg.display.get_surface()
        self.rect = self.surface.get_rect(topleft =(PADDING, PADDING))
        self.sprites = pg.sprite.Group()


        # Line surface:
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0)) # Use green because in other sections, we don't use green --> easier to hide
        self.line_surface.set_colorkey((0,255,0)) # Hide the background colour
        self.line_surface.set_alpha(120) # Transparency: 0 --> 255 (no transparency)

        # Tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

    def run(self):
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)
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

class Block (pg.sprite.Sprite):
    def __init__(self, group, pos, colour):

        # General
        super().__init__(group) # Call out the bigger class's (super class) attributes so we can use it later
        self.image = pg.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(colour)

        # Position
        self.pos = pg.Vector2(pos) + BLOCK_OFFSET
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft = (x, y))

class Tetromino:
    def __init__(self, shape, group):
        # Setup
        self.block_positions = TETROMINOS[shape]['shape']
        ''' 
        The 1st shape is to define the type of shape
        The 2nd shape is to call out the coordinates of the shape
        '''
        self.colour = TETROMINOS[shape]['colour']

        # Create blocks comprehension (1 shape per class)
        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]