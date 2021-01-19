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