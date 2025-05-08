import pygame as pg
import sys  # встроенный модуль, который предоставляет доступ к некоторым переменным и функциям,
# взаимодействующим с интерпретатором Python.
# Этот модуль полезен для управления работой программы, а также для получения информации о среде выполнения.
import random
import math
from pygame.locals import QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN

pg.init()
pg.mixer.init()
shot_sound = pg.mixer.Sound("shot.wav")
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
RELOAD_TIME = 2000  # время перезарядки в миллисекундах

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Тир")
clock = pg.time.Clock()

# спрайты
background_img = pg.image.load("background.png").convert_alpha()
player_img = pg.image.load("player.png").convert_alpha()
weapon_img = pg.image.load("weapon.png").convert_alpha()
bullet_img = pg.image.load("bullet.png").convert_alpha()
target_img = pg.image.load("target.png").convert_alpha()
target_hit_img = pg.image.load("target_hit.png").convert_alpha()
buy_button_img = pg.image.load("buy_button.png").convert_alpha()
barrier_img = pg.image.load("barrier.png").convert_alpha()
shop_img = pg.image.load("shop.png").convert_alpha()
rpg_img = pg.image.load("rpg.png").convert_alpha()
minigun_img = pg.image.load("minigun.png").convert_alpha()
sniper_img = pg.image.load("sniper.png").convert_alpha()
explosion_img = pg.image.load("explosion.png").convert_alpha()
# Состояния игры
MENU = 0
LEVEL1 = 1
LEVEL2 = 2
SHOP = 3
game_state = MENU


"""
Игрок может:
- Двигаться с помощью клавиш WASD
- Стрелять из оружия
- Перезаряжать оружие
- Покупать новые магазины патронов
"""


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = HEIGHT // 2  # это атрибут объекта в библиотеке pg,
        # который отвечает за вертикальное положение прямоугольника (rect) на экране.
        # координаты центра прямоугольника по горизонтали и вертикали соответственно.
        self.speed = 5
        self.weapon = Weapon(self)
        self.magazines = 5  # кол-во магазинов
        self.bullets_in_magazine = 10  # кол-во пуль в текущем магазине
        self.reloading = False  # состояние перезарядки
        self.reload_start_time = 0  # время начала перезарядки
        self.coins = 0  # кол-во монет
        self.barrier = None

    def update(self):
        # Проверяем нажатие клавиш для движения
        keys = pg.key.get_pressed()
        if keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        # Игрок не может пройти через барьер
        if keys[K_d] and self.rect.right < self.barrier.rect.left:
            self.rect.x += self.speed

        # Обновление оружия
        self.weapon.update()

        # Обработка перезарядки
        if self.reloading:
            current_time = pg.time.get_ticks()
            if current_time - self.reload_start_time >= RELOAD_TIME:
                self.reloading = False
                self.bullets_in_magazine = 10

    def shoot(self):
        # Стрельба только если есть патроны и не перезаряжаемся
        if self.bullets_in_magazine > 0 and not self.reloading:
            self.bullets_in_magazine -= 1
            # Создаем пулю в позиции конца оружия с углом поворота оружия
            shot_sound.play()
            bullet_pos = self.weapon.get_muzzle_position()
            return Bullet(bullet_pos[0], bullet_pos[1], self.weapon.angle)

        # Если кончились патроны в магазине, начинаем перезарядку
        elif self.bullets_in_magazine == 0 and not self.reloading and self.magazines > 0:
            self.reload()

        return None

    def reload(self):
        if self.magazines > 0 and not self.reloading:
            self.magazines -= 1
            self.reloading = True
            self.reload_start_time = pg.time.get_ticks()

    def buy_magazines(self):
        # Покупка магазинов за монеты
        if self.coins >= 100:
            self.magazines += 2
            self.coins -= 100
            return True
        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.weapon.draw(surface)


"""

Оружие:
- Следует за курсором мыши и вращается в его направлении
- Определяет позицию для создания пули при выстреле
"""


class Weapon(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = weapon_img
        self.original_image = weapon_img
        self.rect = self.image.get_rect()
        self.angle = 0

    def update(self):
        # позиция мыши
        mouse_pos = pg.mouse.get_pos()

        # Вычисляю угол между игроком и мышью
        # Использую математические функции для расчета угла:
        # atan2 возвращает угол в радианах(единица измерения плоских углов в си), затем преобразуем в градусы
        dx = mouse_pos[0] - self.player.rect.centerx
        dy = mouse_pos[1] - self.player.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx))

        # Оружте надо повернуть
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

        # Позиционирую оружие у правой стороны игрока
        # Юзаю смещение, чтобы оружие всегда было у плеча человечка
        offset_x = 20  # Смещение от центра чела по x
        offset_y = 0  # Смещение от центра чела по y

        # Тут что то надо использовать для корректного размещения оружия при любом угле
        self.rect.center = (
            self.player.rect.centerx + offset_x * math.cos(math.radians(self.angle)),
            self.player.rect.centery - offset_y * math.sin(math.radians(self.angle))
        )

    def get_muzzle_position(self):
        # Возвращает позицию конца оружия для создания пули
        angle_rad = math.radians(self.angle)
        muzzle_distance = 25  # Расстояние от центра до конца оружия

        # Тригонометрия(что это)(раздел математики, в котором изучаются тригонометрические функции и их использование в геометрии.)
        # для определения точки выстрела
        muzzle_x = self.rect.centerx + math.cos(angle_rad) * muzzle_distance
        muzzle_y = self.rect.centery - math.sin(angle_rad) * muzzle_distance
        return (muzzle_x, muzzle_y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ну тут рисовали пинятно картинку и рект

"""

Пуля:
- Создается в конце оружия и летит в направлении прицела
- Движется с постоянной скоростью
- Исчезает если вылетает за пределы экрана
"""


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, angle):  # ну тут инит и про пулю надо сделать
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.image = pg.transform.rotate(bullet_img, angle)
        self.speed = 10

        # Тут нужн что то по типу расчета векторов скорости по x и y на основе угла
        # Опять эта тригонометрия для определения направления движения
        angle_rad = math.radians(angle)
        self.speedx = math.cos(angle_rad) * self.speed  # Это скорость по горизонтали
        self.speedy = -math.sin(angle_rad) * self.speed  # А это скорость по вертикали

    def update(self):
        # Движение пули
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Удаление пули если она вышла за пределы экрана
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()


"""

Мишень:
- Автоматически двигается вверх-вниз в заданных пределах
- После первого попадания меняет внешний вид
- Уничтожается после двух попаданий
"""


class Target(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = target_img
        self.rect = self.image.get_rect()

        # Устанавливаем начальную позицию на правой стороне экрана
        self.rect.x = random.randint(int(WIDTH * 0.3), WIDTH - self.rect.width)
        self.rect.y = random.randint(50, HEIGHT - 50)

        # Параметры движения
        self.speed = random.uniform(1, 3)  # случайная скорость движения
        self.direction = random.choice([-1, 1])  # Направление: вверх или вниз

        # Определяем границы движения мишени (случайные значения для разнообразия)
        self.min_y = random.randint(50, HEIGHT // 2)
        self.max_y = random.randint(self.min_y + 100, HEIGHT - 50)
        self.hits = 0  # Количество попаданий

    def update(self):
        # Движение мишени вверх-вниз
        self.rect.y += self.speed * self.direction

        # Меняем направление, если достигли границы
        if self.rect.top < self.min_y:
            self.rect.top = self.min_y
            self.direction *= -1
        elif self.rect.bottom > self.max_y:
            self.rect.bottom = self.max_y
            self.direction *= -1

    def hit(self):
        # Обработка попадания в мишень
        self.hits += 1
        if self.hits == 1:
            self.image = target_hit_img  # Меняем спрайт после первого попадания
        return self.hits >= 2  # Возвращаем True, если мишень уничтожена


class Button:
    def __init__(self, image, pos):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = pos

    def is_clicked(self, pos):
        # Проверяем, попадает ли позиция клика в область кнопки
        return self.rect.collidepoint(pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


"""
Отрисовка интерфейса:
- Текущий счёт игрока
- Количество монет
- Количество магазиновц
- Количество патронов
- Прогресс перезарядки
"""


def draw_ui(surface, player, score):
    # Отображение счета
    font = pg.font.SysFont(None, 36)
    score_text = font.render(f"Счёт: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))

    # Отображение монет
    coins_text = font.render(f"Монеты: {player.coins}", True, WHITE)
    surface.blit(coins_text, (10, 50))

    # Отображение магазинов
    magazines_text = font.render(f"Магазины: {player.magazines}", True, WHITE)
    surface.blit(magazines_text, (10, 90))

    # Отображение текущих патронов в магазине
    bullets_text = font.render(f"Патроны: {player.bullets_in_magazine}/10", True, WHITE)
    surface.blit(bullets_text, (10, 130))

    # Отображение полоски перезарядки
    if player.reloading:
        current_time = pg.time.get_ticks()
        elapsed = current_time - player.reload_start_time

        # Вычисляем процент завершения перезарядки
        reload_percentage = min(elapsed / RELOAD_TIME, 1.0)

        # Фон полоски
        pg.draw.rect(surface, GRAY, (10, 170, 200, 20))
        # Заполнение
        pg.draw.rect(surface, GREEN, (10, 170, 200 * reload_percentage, 20))
        # Текст
        reload_font = pg.font.SysFont(None, 24)
        reload_text = reload_font.render("Перезарядка", True, WHITE)
        # Центрируем текст перезарядки в полоске загрузки
        reload_text_rect = reload_text.get_rect(center=(110, 180))
        surface.blit(reload_text, reload_text_rect)


"""
Барьер:
- Разделяет игровую зону на две части
- Ограничивает движение игрока
"""


class Barrier(pg.sprite.Sprite):
    def __init__(self):  # Будет легче
        super().__init__()
        self.image = barrier_img
        self.rect = self.image.get_rect()
        self.rect.x = int(WIDTH * 0.3)  # Барьер на трети экрана
        self.rect.y = 0
        self.rect.height = HEIGHT


"""
Кнопка магазина оружия:

- Открывает меню поверх игры
- Есть выбор оружия(в рамке находится фото оружия,снизу описание-характеристики)
"""


class Shop(pg.sprite.Sprite):
    def __init__(self):  # Будет легче
        super().__init__()
        self.image = shop_img
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 600


# game
def game():
    # Создание групп спрайтов вот тута сложно
    all_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()
    targets = pg.sprite.Group()

    # Создание пупса
    player = Player()
    all_sprites.add(player)
    all_sprites.add(player.weapon)

    # Создание барьера
    barrier = Barrier()
    player.barrier = barrier
    all_sprites.add(barrier)

    # Создание кнопки покупки и шопа
    buy_button = Button(buy_button_img, (WIDTH - 110, 10))
    shop_button = Button(shop_img, (600, 9))


    # Создание таргетов
    for _ in range(10):
        target = Target()
        all_sprites.add(target)
        targets.add(target)

    score = 0  # cюда а дальше по-старинке
    run = True
    while run:
        for event in pg.event.get():
            if event.type == QUIT:
                run = False

            # Нужна оказывается еще обработка выстрела
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # лкм
                    # Проверка не кликнули ли по кнопке покупки
                    if buy_button.is_clicked(event.pos):
                        if player.buy_magazines():
                            print("Куплено 2 магазина!")
                    else:
                        # пиу пиуу
                        bullet = player.shoot()
                        if bullet:
                            all_sprites.add(bullet)
                            bullets.add(bullet)

        # Обновление всех игровых объектов тоже надо
        all_sprites.update()

        # Проверка на попадания пуль в мишени (копиркнул)
        hits = pg.sprite.groupcollide(bullets, targets, True, False)
        for bullet, target_list in hits.items():
            for target in target_list:
                # Если мишень в ауте
                if target.hit():
                    score += 10
                    player.coins += 10
                    target.kill()

        # Если все мишени уничтожены нужны новые.. спавним
        if len(targets) == 0:
            for _ in range(10):
                target = Target()
                all_sprites.add(target)
                targets.add(target)

        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)
        buy_button.draw(screen)
        shop_button.draw(screen)
        draw_ui(screen, player, score)
        pg.display.flip()

        clock.tick(60)
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    game()
# сюда я доделал бож
