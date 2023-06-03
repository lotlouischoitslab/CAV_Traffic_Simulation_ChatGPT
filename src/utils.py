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
    def __init__(self, x, y, velocity, acceleration,time,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 40))
        self.color = random.choice(COLORS)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity / 60  # Convert km/hr to pixels/frame
        self.acceleration = acceleration /60 
        self.time = time
        self.direction = direction

    def update(self):
        self.velocity += self.acceleration*delta_t
        self.velocity = min(self.velocity, MAX_VELOCITY)
        self.rect.y += self.velocity * self.direction*self.time

        # Check if the vehicle is off the screen
        if self.direction == 1 and self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -40
            self.velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY) / 60  # Random velocity 
            self.acceleration = random.randint(0, MAX_ACCELERATION) /60   # Random acceleration 
        elif self.direction == -1 and self.rect.y < -40:
            self.rect.y = WINDOW_HEIGHT
            self.velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY) / 60  # Random velocity 
            self.acceleration = random.randint(0, MAX_ACCELERATION) /60   # Random acceleration 

        # Check for collision with other vehicles
        for vehicle in all_sprites:
            if vehicle != self:
                if pygame.sprite.collide_rect(self, vehicle):
                    # Calculate the distance between vehicles
                    distance = abs(self.rect.y - vehicle.rect.y)

                    # Calculate the safe distance based on the velocities
                    safe_distance = SAFE_DISTANCE * (self.velocity / vehicle.velocity)

                    # Adjust the acceleration if the vehicles are too close
                    if distance < safe_distance:
                        if self.velocity > vehicle.velocity:
                            self.acceleration = -MAX_ACCELERATION /60 
                        else:
                            self.acceleration = MAX_ACCELERATION /60 
                    else:
                        self.acceleration = 0