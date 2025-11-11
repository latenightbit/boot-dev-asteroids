from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_new_asteroid_vector = self.velocity.rotate(random_angle)
        second_new_asteroid_vector = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        first_new_asteroid.velocity = first_new_asteroid_vector * 1.2
        second_new_asteroid.velocity = second_new_asteroid_vector * 1.2
