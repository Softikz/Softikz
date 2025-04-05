import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PLAYER_SIZE = 50
ENEMY_SIZE = 50
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blocks")

player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10
player_speed = 7

enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
enemy_y = -ENEMY_SIZE
enemy_speed = 5

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -ENEMY_SIZE
        enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)

    if (player_x < enemy_x + ENEMY_SIZE and
            player_x + PLAYER_SIZE > enemy_x and
            player_y < enemy_y + ENEMY_SIZE and
            player_y + PLAYER_SIZE > enemy_y):
        print("Game Over!")
        running = False

    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()