import pygame
import random
import time

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
LANE_WIDTH = 80
COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0)]
SAFE_DISTANCE = 60

# Vehicle class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 40))
        self.color = random.choice(COLORS)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, vehicles):
        self.rect.y += self.speed
        if self.rect.y > WINDOW_HEIGHT or self.rect.y < -40:
            self.rect.y = random.choice([-40, WINDOW_HEIGHT])

        # Check for collisions/overlaps with other vehicles
        for vehicle in vehicles:
            if vehicle != self and pygame.sprite.collide_rect(self, vehicle):
                if self.rect.y < vehicle.rect.y:
                    self.rect.y = vehicle.rect.y - SAFE_DISTANCE
                else:
                    self.rect.y = vehicle.rect.y + SAFE_DISTANCE

# Simulate function
def simulate():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    vehicles = pygame.sprite.Group()

    # Create vehicles with different colors and adjust headway
    # num_vehicles = 8
    # lane_width = WINDOW_WIDTH // (num_vehicles + 1)
    # for i in range(num_vehicles):
    #     x = (i + 1) * lane_width - LANE_WIDTH // 2
    #     y = random.choice([-40, WINDOW_HEIGHT])
    #     speed = -1 if y > 0 else 1
    #     vehicle = Vehicle(x, y, speed)
    #     all_sprites.add(vehicle)
    #     vehicles.add(vehicle)


    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(vehicles)

        # Draw the road
        window.fill((128, 128, 128))

        # Draw the yellow lines
        line_width = 5
        line_height = 600
        line_spacing = 100

        # Calculate the position of the center lines
        center_line_left_x = WINDOW_WIDTH // 2 - line_width // 2 - 5
        center_line_right_x = WINDOW_WIDTH // 2 + line_width // 2

        # Draw the left yellow line
        pygame.draw.rect(window, (255, 255, 0), pygame.Rect(center_line_left_x, 0, line_width, line_height))
        for y in range(line_spacing, WINDOW_HEIGHT - line_height, line_spacing):
            pygame.draw.rect(window, (255, 255, 0), pygame.Rect(center_line_left_x, y, line_width, line_height))

        # Draw the right yellow line
        pygame.draw.rect(window, (255, 255, 0), pygame.Rect(center_line_right_x, 0, line_width, line_height))
        for y in range(line_spacing, WINDOW_HEIGHT - line_height, line_spacing):
            pygame.draw.rect(window, (255, 255, 0), pygame.Rect(center_line_right_x, y, line_width, line_height))

        # Draw the white stripes for each lane
        stripe_width = 10
        stripe_height = 40
        stripe_spacing = 100

        for lane in range(-4, 5):
            delta = 0
            for x in range(WINDOW_WIDTH // 2 - LANE_WIDTH // 2 - (LANE_WIDTH + 190), WINDOW_WIDTH // 2 + LANE_WIDTH // 2 + (LANE_WIDTH + 200), (LANE_WIDTH + 20)):
                if delta != 3*(LANE_WIDTH + 20):
                    for y in range(stripe_spacing // 2, WINDOW_HEIGHT, stripe_spacing):
                        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(x - stripe_width // 2, y - stripe_height // 2, stripe_width, stripe_height))
                delta += (LANE_WIDTH + 20)

        all_sprites.draw(window)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def main():
    simulate() #Run the simulation

if __name__ == '__main__':
    main()
