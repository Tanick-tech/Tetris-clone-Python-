import pygame as pg

# Game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE
""" 
CELL_SIZE: In pixels
10, 20: the number of COLUMNS & ROWS
"""

# Sidebar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7 # The percentage of the sidebar area
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# Window - the screen covers the whole thing
PADDING = 20 # The margin between the window and the gaming elements is 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# Colours
YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204B9B'
GREEN = '#65B32E'
PURPLE = '#7B217F'
CYAN = '#6CC6D9'
ORANGE = '#F07E13'
GRAY = '#1C1C1C'
LINE_COLOUR = '#FFFFFF'

# Shapes
TETROMINOS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'colour': PURPLE},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'colour': YELLOW},
    'J': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'colour': BLUE},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'colour': ORANGE},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'colour': CYAN},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'colour': GREEN},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'colour': RED},
}
# Every shape starts with (0; 0) is always the pivot point to rotate.

# Game behaviour
UPDATE_START_SPEED = 200 # Increase the game difficulty
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pg.Vector2(COLUMNS // 2, -1)

SCORE_DATA = {0: 0,1: 40, 2: 100, 3: 300, 4: 1200}