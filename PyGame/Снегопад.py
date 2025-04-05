import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Снегопад")

class Snowflake:
    def __init__(self):  # Исправлено: name __init__
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(2, 6)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)

    def fall(self):
        self.y += self.speed
        self.x += self.wind

        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

snowflakes = [Snowflake() for _ in range(200)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()