import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    my_asteroidfield = AsteroidField()


    Player.containers = (updatable, drawable)
    my_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT /2, radius = PLAYER_RADIUS)

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(my_player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

