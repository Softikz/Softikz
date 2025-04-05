import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 20

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")


# Классы
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - PADDLE_WIDTH) / 2
        self.rect.y = HEIGHT - PADDLE_HEIGHT - 10

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 10


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от стен
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(random.choice([RED, GREEN, BLUE, YELLOW]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# Создание платформы и мяча
paddle = Paddle()
ball = Ball()
all_sprites.add(paddle)
all_sprites.add(ball)

# Создание кирпичей
for row in range(5):
    for col in range(10):
        brick = Brick(col * (BRICK_WIDTH + 5) + 35, row * (BRICK_HEIGHT + 5) + 35)
        all_sprites.add(brick)
        bricks.add(brick)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление paddle с передачей keys
    paddle.update(keys)

    # Обновление других спрайтов (в данном случае только ball)
    ball.update()

    # Проверка на столкновения
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y = -ball.speed_y  # Отскок от платформы

    # Проверка столкновений с кирпичами
    hits = pygame.sprite.spritecollide(ball, bricks, True)
    for hit in hits:
        ball.speed_y = -ball.speed_y  # Отскок от кирпичей

    # Проверка, пропустил ли игрок мяч
    if ball.rect.bottom >= HEIGHT:
        running = False  # Завершение игры, если мяч упал

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры
pygame.quit()
print("Game Over!")