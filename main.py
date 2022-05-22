import pygame
from grid import *
from utils import *

pygame.init()   # initialize all the required modules of the pygame

# create the screen
field_size = 30
screen_size = ((WIDTH+MARGIN)*field_size, (HEIGHT+MARGIN)*field_size)
screen = pygame.display.set_mode(screen_size)

# caption and icon
pygame.display.set_caption("A* Path Finding Algorithm")

# init field of grid
field = MyRectangleField(field_size)
# init start and end grid
start = None
end = None
# inin signal to start algorithm
startAlgo = False

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              done = True

        # construct labyrinth depend on clicked position
        x, y = get_clicked_pos(pygame.mouse.get_pos())
        grid = field.grid[x][y]
        if pygame.mouse.get_pressed()[0]: # LEFT
            if not start and grid != end:
                start = grid
                grid.markStart()
            elif not end and grid != start:
                end = grid
                grid.markEnd()
            elif grid != start and grid != end:
                grid.markBarrier()
        elif pygame.mouse.get_pressed()[2]: # RIGHT
            grid.reset()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                AStarSearch(field, screen, start, end)  # START ALGORITHM
            elif event.key == pygame.K_RETURN:
                start = None
                end = None
                field.clear()


    screen.fill(BLACK)

    draw_update(field, screen)

    clock.tick(60)
pygame.quit()