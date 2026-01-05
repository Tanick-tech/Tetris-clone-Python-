from settings import *
from random import choice
from timer import Timer
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

        # Timer
        self.timers = {
            'vertical move': Timer(UPDATE_START_SPEED, True, self.move_down), #Timer(duration, repeated, func)
            'horizontal move': Timer(MOVE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()

    def run(self):
        # Update
        self.timer_update()
        self.sprites.update()
        self.input()
        # Drawing sprites
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)
        # Drawing grid
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

    def move_down(self):
        self.tetromino.move_down()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def input(self):
        keys = pg.key.get_pressed()
        if not self.timers['horizontal move'].active:
            if keys [pg.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys [pg.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

class Block (pg.sprite.Sprite):
    def __init__(self, group, pos, colour):
        # General
        super().__init__(group) # Call out the bigger class's (super class) attributes so we can use it later
        self.image = pg.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(colour)

        # Position
        self.pos = pg.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

    def horizontal_collide(self, x):
        if not 0 <= x < COLUMNS:
            return True
    def vertical_collide (self, y):
        if y >= ROWS:
            return True
    def update(self):
        # self.pos -> rect (because the rect is fixed, so we change the position of it)
        # self.pos changes because of move_down self in Tetromino class
        self.rect.topleft = self.pos * CELL_SIZE


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

    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1

    # Collision
    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount)) for block in self.blocks]
        return True if any(collision_list) else False
    # Movement
    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount)) for block in self.blocks]
        return True if any(collision_list) else False