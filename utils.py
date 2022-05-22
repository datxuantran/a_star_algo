import heapq as hq
import math
from grid import *

# PRIORITY QUEUE
class PriorityQueue:
    def __init__(self):
        self.DONE = -1000000
        self.frontier = []
        self.priorities = {} # Map from grid to cost

    def update(self, grid, newCost):
        oldCost = self.priorities.get(grid)
        if (oldCost is None or newCost < oldCost):
            self.priorities[grid] = newCost
            hq.heappush(self.frontier, (newCost, grid))
            return True
        return False

    def removeMin(self):
        while (len(self.frontier) > 0) :
            cost, grid = hq.heappop(self.frontier)
            if self.priorities[grid] == self.DONE:
                continue
            self.priorities[grid] = self.DONE
            return (grid, cost)
        return (None, None)

# Screen Visualization
def draw_update(field, screen):
    for x in range(field.LEN):
        for y in range(field.LEN):
            grid = field.grid[x][y]
            grid.draw(screen)
    pygame.display.update()

def get_clicked_pos(cordinate):
    x, y = cordinate
    x = x // (WIDTH + MARGIN)
    y = y // (HEIGHT + MARGIN)
    return (x, y)

# Algorithm
def shortest_path_trace(startGrid, endGrid):
    startGrid.parent = None
    grid_ptr = endGrid
    while grid_ptr is not None:
        grid_ptr.color = RED
        grid_ptr = grid_ptr.parent

def heuristicDistance(pointA, pointB):
    xA, yA = pointA.getXY()
    xB, yB = pointB.getXY()
    return math.sqrt((xA-xB)**2 + (yA-yB)**2)

def AStarSearch(field, screen ,startGrid, endGrid):
    field.init_outGoing_Grids()

    frontier = PriorityQueue()
    frontier.update(startGrid, 0)
    while True:
        # Explore grid with lowest pastCost, use frontier(PriorityQueue)
        grid, pastCost = frontier.removeMin()

        if not grid or grid.isBarrier(): continue

        # Exploring this grid
        grid.markExplored()

        if grid and grid.getXY() == endGrid.getXY():
            return shortest_path_trace(startGrid, endGrid)

        # push all outgoing_grids on the frontier
        for outGoing_Grid in grid.adj_plus:
            newCost = pastCost + heuristicDistance(grid, endGrid)
            if frontier.update(outGoing_Grid, newCost):
                # if outGoing_Node is updated,
                # set new path from node to outGoing_Node,
                outGoing_Grid.parent = grid
                # mark grid on queue
                outGoing_Grid.markOnQueue()


        draw_update(field, screen)


