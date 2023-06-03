import pygame
import random
import time 

WINDOW_WIDTH = 800  # Width
WINDOW_HEIGHT = 600  # Height
LANE_WIDTH = 80  # Lane width
COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0)]
SAFE_DISTANCE = 60  # Spacing of the vehicles

# Vehicle class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 40))
        self.color = random.choice(COLORS)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity / 60
        self.direction = direction

    def update(self):
        self.rect.y += self.velocity * self.direction

        # Check if the vehicle is off the screen
        if self.direction == 1 and self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -40
        elif self.direction == -1 and self.rect.y < -40:
            self.rect.y = WINDOW_HEIGHT