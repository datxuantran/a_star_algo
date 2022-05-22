import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Define Grid's Width and Height
WIDTH = 20
HEIGHT = 20
MARGIN = 1

# Define States Of Grid
START = 'START'
END = 'END'
BARRIER = 'BARRIER'
EXPLORED = 'EXPLORED'
CLEAR = 'CLEAR'
ONQUEUE = 'ONQUEUE'


# Grid
class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.color = WHITE
        self.state = CLEAR
        self.adj_plus = []

    def reset(self):
        self.parent = None
        self.color = WHITE
        self.state = CLEAR
        self.adj_plus = []

    def __lt__(self, other):
        return self.getXY() <= other.getXY()

    def getXY(self):
        return (self.x, self.y)

    def isOnQueue(self):
        return self.state == ONQUEUE

    def isExplored(self):
        return self.state == EXPLORED

    def isStart(self):
        return self.state == START

    def isEnd(self):
        return self.state == END

    def isBarrier(self):
        return self.state == BARRIER

    def markOnQueue(self):
        self.color = GREEN
        self.state = ONQUEUE

    def markExplored(self):
        self.color = YELLOW
        self.state = EXPLORED

    def markBarrier(self):
        self.color = BLACK
        self.state = BARRIER

    def markStart(self):
        self.color = GREEN
        self.state = START

    def markEnd(self):
        self.color = RED
        self.state = END

    def draw(self, screen):
        pygame.draw.rect(screen,
                         self.color,
                         [(MARGIN + WIDTH) * self.y + MARGIN,
                          (MARGIN + HEIGHT) * self.x + MARGIN,
                          WIDTH,
                          HEIGHT])

# MyRectangleFile
class MyRectangleField:
    def __init__(self, width):
        # construct grids fields
        self.LEN = width
        self.grid = []
        for y in range(width):
            self.grid.append([])
            for x in range(width):
                newGrid = Grid(x, y)
                self.grid[y].append(newGrid)

    def init_outGoing_Grids(self):
        for x in range(self.LEN):
            for y in range(self.LEN):
                if x + 1 < self.LEN:
                    if not self.grid[x+1][y].isBarrier():
                        self.grid[x][y].adj_plus.append(self.grid[x+1][y])
                if x - 1 >= 0:
                    if not self.grid[x-1][y].isBarrier():
                        self.grid[x][y].adj_plus.append(self.grid[x-1][y])
                if y + 1 < self.LEN:
                    if not self.grid[x][y+1].isBarrier():
                        self.grid[x][y].adj_plus.append(self.grid[x][y+1])
                if y - 1 >= 0:
                    if not self.grid[x][y-1].isBarrier():
                        self.grid[x][y].adj_plus.append(self.grid[x][y-1])

    def clear(self):
        for x in range(self.LEN):
            for y in range(self.LEN):
                self.grid[x][y].reset()