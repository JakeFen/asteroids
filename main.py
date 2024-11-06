import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


# 1. Check for player inputs
# 2. Update the game world
# 3. Draw the game to the screen


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0

    while True:

        # Check if user clicks close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()

        pygame.Surface.fill(screen, (0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


# Only called when this file is run directly.
# Wont run if imported as module
# Considered pythonic or best practice
if __name__ == "__main__":
    main()
