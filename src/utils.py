import pygame
import random
import time 

WINDOW_WIDTH = 800  # Width
WINDOW_HEIGHT = 600  # Height
LANE_WIDTH = 80  # Lane width
COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0)]
SAFE_DISTANCE = 6 #km Safe spacing of the vehicles
conversion_factor = 38
SAFE_DISTANCE = SAFE_DISTANCE*conversion_factor
all_sprites = pygame.sprite.Group()  # Store all the agents here

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
        self.velocity = velocity / 60  #For velocity, convert km/hr to pixels/frame
        self.direction = direction

    def update(self):
        self.rect.y += self.velocity * self.direction
        
        # Check if the vehicle is off the screen
        if self.direction == 1 and self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -40
            self.velocity = random.randint(110, 200) / 60  # Random velocity between 110 and 200 km/hr
        elif self.direction == -1 and self.rect.y < -40:
            self.rect.y = WINDOW_HEIGHT
            self.velocity = random.randint(110, 200) / 60  # Random velocity between 110 and 200 km/hr

        # Check for collision with other vehicles
        for vehicle in all_sprites:
            if vehicle != self:
                if pygame.sprite.collide_rect(self, vehicle):
                    # Calculate the distance between vehicles
                    distance = abs(self.rect.y - vehicle.rect.y)

                    # Calculate the safe distance based on the velocities
                    safe_distance = SAFE_DISTANCE * (self.velocity / vehicle.velocity)

                    # Adjust the velocity if the vehicles are too close
                    if distance < safe_distance:
                        if self.velocity > vehicle.velocity:
                            self.velocity = vehicle.velocity