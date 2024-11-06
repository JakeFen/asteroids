import pygame
from constants import *
from player import *


# 1. Check for player inputs
# 2. Update the game world
# 3. Draw the game to the screen


def main():
    pygame.init()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:

        # Check if user clicks close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


# Only called when this file is run directly.
# Wont run if imported as module
# Considered pythonic or best practice
if __name__ == "__main__":
    main()
