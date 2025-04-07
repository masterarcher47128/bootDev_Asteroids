from circleShape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        launchAngle = random.uniform(20,50)
        a = self.velocity.rotate(launchAngle)
        b = self.velocity.rotate(-launchAngle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = b * 1.2

