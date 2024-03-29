import pygame
import menu
import front_menu
import os
import sys

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


map_massiv = open('map.txt').read().split('\n')
final = []
for i in map_massiv:
    print(i)
    final.append(list(map(int, list(i))))
bg = pygame.image.load("images/map1 (1).png")
car = pygame.image.load("car and map testing/car(right).png")
BACKGROUND_MUSIC = 'assets and music/fon.mp3'

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)
front_menu.front_menu()

x_car = 348
y_car = 356
clock = pygame.time.Clock()
start_game = True

pygame.mixer.music.load(BACKGROUND_MUSIC)
pygame.mixer.music.play(-1)

while start_game:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_car += 1
    elif keys[pygame.K_a]:
        x_car -= 1
    elif keys[pygame.K_w]:
        y_car -= 1
    elif keys[pygame.K_s]:
        y_car += 1
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            start_game = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                menu.Menu_screeen()
                print(x_car, y_car)
                window = pygame.display.set_mode(SIZE)
    screen.fill(000000)
    screen.blit(bg, (280, 0))
    screen.blit(car, (x_car, y_car))
    window.blit(screen, (0, 0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
