import sys
import pygame
from pendulum import *

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    # Constants for the screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    ITERATION = 1000
    iteration = 0
    WHITE = (255, 255, 255) 
    BLACK = 0
    MASS1 = 10
    MASS2 = 20
    LENGTH1 = 100
    LENGTH2 = 150
    XPOS = SCREEN_WIDTH/2
    YPOS = SCREEN_HEIGHT/5
    ANGLE1 = 45
    ANGLE2 = 30
    WIDTH = 5

    # Create the screen surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pendulum = Pendulum(MASS1, MASS2, LENGTH1, LENGTH2, XPOS, YPOS, ANGLE1, ANGLE2, WIDTH)
    clock = pygame.time.Clock()

    while True:

        color = WHITE
        # Clear the screen with a white background
        screen.fill(BLACK)
        
        pendulum.draw(screen, WHITE)
        pendulum.move()

        # Update the display
        pygame.time.delay(1)
        pygame.display.update()
        # iteration += 1
    
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
