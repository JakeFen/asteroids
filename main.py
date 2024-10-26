import pygame
from constants import *


# 1. Check for player inputs
# 2. Update the game world
# 3. Draw the game to the screen


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        # Check if user clicks close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()


# Only called when this file is run directly.
# Wont run if imported as module
# Considered pythonic or best practice
if __name__ == "__main__":
    main()
