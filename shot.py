import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.position = position

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)