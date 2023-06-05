import pygame
import random

WINDOW_WIDTH = 800  # Width
WINDOW_HEIGHT = 600  # Height
LANE_WIDTH = 80  # Lane width
COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0)]
SAFE_DISTANCE = 6  # Safe spacing of the vehicles in km

MAX_ACCELERATION = 2 #Max acceleration in km/hr^2
MIN_VELOCITY = 100 # Minimum velocity in km/hr
MAX_VELOCITY = 200  # Maximum velocity in km/hr
all_sprites = pygame.sprite.Group()  # Store all the agents here
delta_t = 1 # hour

# Vehicle class

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, acceleration, time, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 40))
        self.color = random.choice(COLORS)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity / 60
        self.acceleration = acceleration / 60
        self.time = time
        self.direction = direction
        self.spawn_y = y  # Store the spawning y-coordinate

    def update(self):
        self.velocity += self.acceleration * delta_t
        self.velocity = min(self.velocity, MAX_VELOCITY)
        self.rect.y += self.velocity * self.direction * self.time

        if self.direction == 1 and self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -40
            self.velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY) / 60
            self.acceleration = random.randint(0, MAX_ACCELERATION) / 60
        elif self.direction == -1 and self.rect.y < -40:
            self.rect.y = WINDOW_HEIGHT
            self.velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY) / 60
            self.acceleration = random.randint(0, MAX_ACCELERATION) / 60