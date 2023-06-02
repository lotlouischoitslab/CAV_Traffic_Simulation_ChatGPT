from src.utils import Vehicle

import pygame
import random
import time

WINDOW_WIDTH = 800  # Width
WINDOW_HEIGHT = 600  # Height
LANE_WIDTH = 80  # Lane width
COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0)]
SAFE_DISTANCE = 60  # Spacing of the vehicles

# Generate road function
def generate_road(surface):
    # Draw the road
    surface.fill((128, 128, 128))

    # Draw the yellow lines
    line_width = 5
    line_height = 600
    line_spacing = 100

    # Calculate the position of the center lines
    center_line_left_x = WINDOW_WIDTH // 2 - line_width // 2 - 10
    center_line_right_x = WINDOW_WIDTH // 2 + line_width // 2 - 5

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
    stripe_spacing = 100

    for lane in range(-4, 5):
        delta = 0
        for x in range(WINDOW_WIDTH // 2 - LANE_WIDTH // 2 - (LANE_WIDTH + 190),
                       WINDOW_WIDTH // 2 + LANE_WIDTH // 2 + (LANE_WIDTH + 200), (LANE_WIDTH + 20)):
            if delta != 3 * (LANE_WIDTH + 20):
                for y in range(stripe_spacing // 2, WINDOW_HEIGHT, stripe_spacing):
                    pygame.draw.rect(surface, (255, 255, 255),
                                     pygame.Rect(x - stripe_width // 2, y - stripe_height // 2, stripe_width,
                                                 stripe_height))
            delta += (LANE_WIDTH + 20)


# Simulate function
def simulate():
    pygame.init() #initialize the pygame 
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #create a window for pygame
    clock = pygame.time.Clock() #set a timer
    all_sprites = pygame.sprite.Group() #we are going to store all the agents here 

    # Create vehicles
    num_lanes = 8 
    lane_width = LANE_WIDTH
    spacing = lane_width // 4

    for lane in range(num_lanes):
        x = (lane + 1) * lane_width - LANE_WIDTH // 2
        y = random.choice([-40, WINDOW_HEIGHT])
        speed = -1 if y > 0 else 1
        vehicle = Vehicle(x, y, speed)
        all_sprites.add(vehicle)
        x += spacing
        vehicle = Vehicle(x, y, speed)
        all_sprites.add(vehicle)

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
