"""Make an AI navigate through a maze."""
import pygame as pg
import numpy as np
import sys
import matplotlib.pyplot as plt

class Game:
    """This class manages the game loop and pygame setup."""
    def __init__(self) -> None:
        """Initializes the pygame window."""
        pg.init()
        self.width = 800
        self.height = 600
        self.screen = pg.display.set_mode([self.width, self.height])
        self.maze = Maze(self)
        self.rngManager = RngManager(629748367498629487378962)

        self.maze.makeWalls()
        print(np.sum(self.maze.maze))

    def play(self) -> None:
        """Manages the main game loop."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
            self.maze.draw(self.screen)
            pg.display.update()

class Maze:
    """Generates the maze for the AI to navigate through."""
    def __init__(self, game: Game) -> None:
        """Initialize maze matrix."""
        self.game = game
        self.mazeWidth = self.game.width
        self.mazeHeight = self.game.height
        self.gridWidth = 30
        self.gridHeight = 20
        self.wallPieceWidth = 5
        self.wallPieceHeight = 5
        self.maze = np.zeros([self.game.height, self.game.width])
    def draw(self, screen: pg.Surface) -> None:
        """Draw the maze onto the screen one grid piece at a time."""
        for column in range(0, self.game.width, self.gridWidth):
            for row in range(0, self.game.height, self.gridHeight):
                rect = pg.Rect(column, row, self.gridWidth, self.gridHeight)
                # print(self.maze.shape)
                if self.maze[row, column] == 1:
                    color = "black"
                else:
                    color = "white"
                pg.draw.rect(screen, color, rect)
    def makeWalls(self) ->None:
        """Make walls by adding 1's to the matrix."""
        # Using Wilson's algorithm
        # https://en.wikipedia.org/wiki/Maze_generation_algorithm
        # self.maze[10:50, 10:100] = 1
        startPoint = [self.wallPieceHeight + self.gridHeight//2, self.wallPieceWidth + self.gridWidth//2]
        endPoint = [590, 790]
        currentPoint = [0, 0]
        self.maze[startPoint[0] - self.gridWidth//2:startPoint[0] + self.gridWidth//2, startPoint[1] - self.gridHeight//2:startPoint[1] + self.gridHeight//2] = 1
        while(currentPoint != endPoint):
            direction = self.game.rngManager.integer(1, 4)
            distance = self.game.rngManager.integer(1, 2)
            nextRow = currentPoint[0]
            nextColumn = currentPoint[1]
            for i in range(distance):
                if direction == 1:
                    nextRow -= self.gridHeight + self.wallPieceHeight
                if direction == 2:
                    nextRow += self.gridHeight + self.wallPieceHeight
                if direction == 3:
                    nextColumn -= self.gridWidth + self.wallPieceWidth
                if direction == 4:
                    nextColumn += self.gridWidth + self.wallPieceWidth
                if(nextRow < 0 or nextColumn < 0 or nextRow > self.game.height or nextColumn > self.game.width):
                    return
                currentPoint = [nextRow, nextColumn]
                self.maze[currentPoint[0] - self.gridWidth//2:currentPoint[0] + self.gridWidth//2, currentPoint[1] - self.gridHeight//2:currentPoint[1] + self.gridHeight//2] =  1

class RngManager:
    """This class manages the randomization in the maze generation."""
    def __init__(self, seed: int) -> None:
        """Initializes rng management with seed."""
        self.rng = np.random.default_rng(seed)

    def integer(self, low: int, high: int) -> int:
        """Return random integer."""
        return(self.rng.integers(low, high))


if __name__ == "__main__":
    game = Game()
    # game.play()
    maze = Maze(game)
    maze.makeWalls()
    plt.imshow(maze.maze)
    plt.show()