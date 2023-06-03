from src.utils import Vehicle

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

# Generate road function
def generate_road(surface):
    # Draw the road
    surface.fill((128, 128, 128))

    # Draw the yellow lines
    line_width = 5
    line_height = 600
    line_spacing = 100

    # Calculate the position of the center lines
    center_line_left_x = WINDOW_WIDTH // 2 - line_width // 2
    center_line_right_x = WINDOW_WIDTH // 2 + line_width // 2 + 5

    # Draw the left yellow line
    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(center_line_left_x, 0, line_width, line_height))
    for y in range(line_spacing, WINDOW_HEIGHT - line_height, line_spacing):
        pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(center_line_left_x, y, line_width, line_height))

    # Draw the right yellow line
    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(center_line_right_x, 0, line_width, line_height))
    for y in range(line_spacing, WINDOW_HEIGHT - line_height, line_spacing):
        pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(center_line_right_x, y, line_width, line_height))

    # Draw the white stripes for each lane
    stripe_width = 10
    stripe_height = 40
    stripe_spacing = LANE_WIDTH

    for lane in range(-4, 6):
        delta = 0
        for x in range(WINDOW_WIDTH // 2 - LANE_WIDTH // 2 - (LANE_WIDTH + 190),
                       WINDOW_WIDTH // 2 + LANE_WIDTH // 2 + (LANE_WIDTH + 400), (LANE_WIDTH)):
            if delta != 4 * (LANE_WIDTH):
                for y in range(stripe_spacing // 2, WINDOW_HEIGHT, stripe_spacing):
                    pygame.draw.rect(surface, (255, 255, 255),
                                     pygame.Rect(x - stripe_width // 2, y - stripe_height // 2, stripe_width,
                                                 stripe_height))
            delta += LANE_WIDTH

def simulate():
    pygame.init()  # Initialize pygame
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create a window for pygame
    clock = pygame.time.Clock()  # Set a timer
    all_sprites = pygame.sprite.Group()  # Store all the agents here

    # Create vehicles
    num_lanes = 10
    lane_width = LANE_WIDTH
    x = lane_width // 2

    for lane in range(0, num_lanes // 2):
        y = random.randint(-WINDOW_HEIGHT, -60)  # Random y-axis position above the window
        velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY)  # Random velocity 
        acceleration = random.randint(0,MAX_ACCELERATION)
        direction = 1  # Move down
        vehicle = Vehicle(x, y, velocity, acceleration,delta_t,direction)
        all_sprites.add(vehicle)
        x += lane_width

    x = WINDOW_WIDTH - lane_width // 2

    for lane in range(num_lanes // 2, num_lanes):
        y = random.randint(-60, WINDOW_HEIGHT)  # Random y-axis position below the window
        velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY)  # Random velocity 
        acceleration = random.randint(0,MAX_ACCELERATION)
        direction = -1  # Move up
        vehicle = Vehicle(x, y, velocity, acceleration,delta_t,direction)
        all_sprites.add(vehicle)
        x -= lane_width

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        generate_road(window)
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def main():
    simulate()  # Run the traffic simulator


if __name__ == '__main__':
    main()
