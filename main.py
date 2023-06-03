from src.utils import Vehicle

import pygame
import random
import numpy as np 
import matplotlib.pyplot as plt 
import csv

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
vehicle_trajectories = []  # Store vehicle trajectories

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
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    # Create vehicles
    num_lanes = 10
    lane_width = LANE_WIDTH
    x = lane_width // 2

    for lane in range(0, num_lanes // 2):
        y = random.randint(-WINDOW_HEIGHT, -60)
        velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY)
        acceleration = random.randint(0, MAX_ACCELERATION)
        direction = 1
        vehicle = Vehicle(x, y, velocity, acceleration, delta_t, direction)
        all_sprites.add(vehicle)
        x += lane_width

    x = WINDOW_WIDTH - lane_width // 2

    for lane in range(num_lanes // 2, num_lanes):
        y = random.randint(-60, WINDOW_HEIGHT)
        velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY)
        acceleration = random.randint(0, MAX_ACCELERATION)
        direction = -1
        vehicle = Vehicle(x, y, velocity, acceleration, delta_t, direction)
        all_sprites.add(vehicle)
        x -= lane_width

    # Create empty lists to store the trajectory data for each vehicle
    left_lane_trajectory = [[] for _ in range(num_lanes // 2)]
    right_lane_trajectory = [[] for _ in range(num_lanes // 2)]

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

        # Collect trajectory data for each vehicle
        for i, vehicle in enumerate(all_sprites):
            # Check if the vehicle is in the left or right lane
            if i < num_lanes // 2:
                trajectory = left_lane_trajectory[i]
            else:
                trajectory = right_lane_trajectory[i - num_lanes // 2]

            # Append the current position to the trajectory
            trajectory.append((pygame.time.get_ticks() / 3600000, vehicle.rect.y - vehicle.spawn_y))

            # Check if the vehicle is off the screen and start a new trajectory
            if vehicle.direction == 1 and vehicle.rect.y > WINDOW_HEIGHT:
                vehicle.rect.y = -40
                trajectory = []
            elif vehicle.direction == -1 and vehicle.rect.y < -40:
                vehicle.rect.y = WINDOW_HEIGHT
                trajectory = []

    pygame.quit()

    # Plot trajectory data after the simulation
    plot_trajectory(left_lane_trajectory, 'Left Lane Trajectory', 'left_trajectory.png')
    plot_trajectory(right_lane_trajectory, 'Right Lane Trajectory', 'right_trajectory.png')

    # Convert the files into csv respectively
    convert_to_csv(left_lane_trajectory, 'left_lane_trajectory.csv')
    convert_to_csv(right_lane_trajectory, 'right_lane_trajectory.csv')


def plot_trajectory(trajectory_data, title, filename):
    plt.figure()
    for trajectory in trajectory_data:
        times, positions = zip(*trajectory)
        positions = [p/10 for p in positions]
        plt.plot(times, positions, linestyle="None", marker='.', markersize=2)
    plt.xlabel('Time (hours)')
    plt.ylabel('Distance from Spawning Point (km)')
    plt.title(title)
    plt.savefig(filename)
    plt.show()


def convert_to_csv(trajectory_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time (hours)', 'Distance from Spawning Point (pixels)'])
        for trajectory in trajectory_data:
            writer.writerows(trajectory)


def main():
    simulate()  # Run the traffic simulator
    


if __name__ == '__main__':
    main()

