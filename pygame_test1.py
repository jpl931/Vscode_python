# import the pygame module
import pygame

# import pygame.locals for easier access
# updated for flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initialize pygame
pygame.init()

# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create screen object
# the size by constant screen_width, screen_height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# variable to keep the main loop runnning
running = True

# main loop
while running:
    # look at every event in the queue
    for event in pygame.event.get():
        # did the user hit a key?
        if event.type == KEYDOWN:
            # was it the escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # did the user click the close button? Then stop the loop.
        elif event.type == QUIT:
            running = False

# fill the screen with white
screen.fill((255, 255, 255))

# create a surface and pass in a tuple containing length and width
surf = pygame.Surface((50, 50))

# give the surface color separate from background
surf.fill((0, 0, 0))
rect = surf.get_rect()

# draw surf onto the scrren at the cneter
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()
            
