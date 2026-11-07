"""Make an AI navigate through a maze."""
import pygame as pg
import numpy as np

class Game:
    """This class manages the game loop and pygame setup."""
    def __init__(self) -> None:
        """Initializes the pygame window."""
        pg.init()
        self.width = 800
        self.height = 600
        self.screen = pg.display.set_mode([self.width, self.height])
        self.maze = Maze(self)

    def play(self) -> None:
        """Manages the main game loop."""
        while True:
            self.maze.draw(self.screen)
            pg.display.update()

class Maze:
    """Generates the maze for the AI to navigate through."""
    def __init__(self, game: Game) -> None:
        """Initialize maze matrix."""
        self.game = game
        self.mazeWidth = self.game.width
        self.mazeHeight = self.game.height
        self.gridWidth = self.game.width//self.mazeWidth
        self.gridHeight = self.game.height//self.mazeHeight
        self.maze = np.zeros([self.game.width, self.game.height])
    def draw(self, screen: pg.Surface) -> None:
        """Draw the maze onto the screen one grid piece at a time."""
        for column in range(0, self.game.width, self.gridWidth):
            for row in range(0, self.game.height, self.gridHeight):
                rect = pg.Rect(column, row, self.gridWidth, self.gridHeight)
                print(self.maze.shape)
                if self.maze[row, column] == 1:
                    color = "black"
                else:
                    color = "white"
                pg.draw.rect(screen, color, rect)
    def makeWalls(self) ->None:
        """Make walls by adding 1's to the matrix."""
        self.maze[10, 0:100] = 1



if __name__ == "__main__":
    game = Game()
    game.play()