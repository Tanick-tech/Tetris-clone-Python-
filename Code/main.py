from settings import *
from sys import exit
# Components
from game import Game
from score import Score
from preview import Preview


class Main:
    # Declaring attribute of a class.
    def __init__(self):

        # General
        pg.init()
        self.display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Tetris')

        # Components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    # Exit everything
                    """
                    This line is to exit everything without error message.
                    Without it, Python can't initialize the pg.display.update().
                    """
                    exit()


            # Display
            self.display_surface.fill(GRAY)

            # Components
            self.game.run()
            self.score.run()
            self.preview.run()

            # Updating the game - decorations
            pg.display.update()
            self.clock.tick()
if __name__ == '__main__':
    main = Main()
    main.run()