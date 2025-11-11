# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        print(dt)
if __name__ == "__main__":
    main()
