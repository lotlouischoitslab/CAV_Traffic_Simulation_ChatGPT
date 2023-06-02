import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define window dimensions
WIDTH = 800
HEIGHT = 600

# Define vehicle dimensions
VEHICLE_WIDTH = 20
VEHICLE_HEIGHT = 40

# Define road dimensions
ROAD_WIDTH = 120
ROAD_HEIGHT = HEIGHT

# Define traffic light dimensions
TRAFFIC_LIGHT_SIZE = 20

# Define vehicle speed
VEHICLE_SPEED = 5


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((VEHICLE_WIDTH, VEHICLE_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = VEHICLE_SPEED

    def update(self):
        self.rect.y += self.speed

        # Reset vehicle position if it goes off the screen
        if self.rect.y > HEIGHT:
            self.rect.y = -VEHICLE_HEIGHT


class TrafficLight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TRAFFIC_LIGHT_SIZE, TRAFFIC_LIGHT_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = random.choice(["red", "green"])
        self.timer = random.randint(100, 300)

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            if self.state == "red":
                self.state = "green"
            else:
                self.state = "red"
            self.timer = random.randint(100, 300)

        if self.state == "red":
            self.image.fill(RED)
        else:
            self.image.fill(GREEN)


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Traffic Simulator")

    all_sprites = pygame.sprite.Group()

    # Create vehicles
    for i in range(10):
        x = random.randint(0, WIDTH - VEHICLE_WIDTH)
        y = random.randint(0, HEIGHT - VEHICLE_HEIGHT)
        vehicle = Vehicle(x, y)
        all_sprites.add(vehicle)

    # Create traffic lights
    traffic_light = TrafficLight(WIDTH // 2 - TRAFFIC_LIGHT_SIZE // 2, HEIGHT // 2 - TRAFFIC_LIGHT_SIZE // 2)
    all_sprites.add(traffic_light)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        window.fill(WHITE)

        # Draw road
        pygame.draw.rect(window, BLACK, (WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, ROAD_HEIGHT))

        all_sprites.draw(window)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
