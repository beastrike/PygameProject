import pygame
import menu
import front_menu
import os
import sys
import random
import time

pygame.init()
pygame.font.init()


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


bezdelnik = True
punkty = [
    (1, 1), (1, 3), (3, 8), (4, 1), (4, 3),
    (7, 1), (7, 3), (8, 10), (8, 12), (8, 14),
    (11, 6), (11, 9), (11, 12), (11, 15), (13, 16),
    (13, 17), (13, 18), (15, 4), (17, 2), (17, 4),
    (17, 5), (19, 2), (19, 4)
]
spis = []
nezaversheny = 3
sobrano = 0
map_massiv = open('map.txt').read().split('\n')
final_list = []
for i in map_massiv:
    final_list.append(list(map(int, list(i))))
bg = pygame.image.load("car and map testing/map_first_level.png")
car = pygame.image.load("car and map testing/car(right).png")
BACKGROUND_MUSIC = 'assets and music/fon.mp3'
punkt_1 = pygame.image.load("car and map testing/coin.png")
punkt_2 = pygame.image.load("car and map testing/coin.png")
punkt_3 = pygame.image.load("car and map testing/coin.png")
y_punkt_1, x_punkt_1 = -32, 0
y_punkt_2, x_punkt_2 = -32, 0
y_punkt_3, x_punkt_3 = -32, 0
f1 = pygame.font.Font("FSEX300.ttf", 60)
f2 = pygame.font.Font("FSEX300.ttf", 60)
text_counter = f1.render(str(sobrano), True, (254, 254, 254))

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)
front_menu.front_menu()

x_car = 344
y_car = 352
clock = pygame.time.Clock()
start_game = True

# pygame.mixer.music.load(BACKGROUND_MUSIC)
# pygame.mixer.music.play(-1)


time_limit = 120
start_time = time.time()
elapsed_time = 0
text_timer = f2.render(str(time_limit - int(elapsed_time)), True, (254, 254, 254))
while start_game:
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("GAME OVER")
        menu.game_over(sobrano)
    text_counter = f1.render(str(sobrano), True, (254, 254, 254))
    text_timer = f2.render(
        f'{str((time_limit - int(elapsed_time)) // 60)}:{(time_limit - int(elapsed_time)) % 60:02}', True,
        (254, 254, 254))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        car = pygame.image.load("car and map testing/car(right).png")
        check = final_list[(y_car + 16) // 32][(x_car + 32 - 280 + 1) // 32]
        if check == 1:
            x_car += 2
        if check == 3:
            if ((y_car + 16) // 32, (x_car - 280 + 32 + 1) // 32) in spis:
                if spis.index(((y_car + 16) // 32, (x_car - 280 + 32 + 1) // 32)) == 0:
                    y_punkt_1, x_punkt_1 = -32, 0
                    nezaversheny -= 1
                    spis[0] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 16) // 32, (x_car - 280 + 32 + 1) // 32)) == 1:
                    y_punkt_2, x_punkt_2 = -32, 0
                    nezaversheny -= 1
                    spis[1] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 16) // 32, (x_car - 280 + 32 + 1) // 32)) == 2:
                    y_punkt_3, x_punkt_3 = -32, 0
                    nezaversheny -= 1
                    spis[2] = (-32, 0)
                    sobrano += 1
            if nezaversheny == 0:
                bezdelnik = True
                spis.clear()
            x_car += 2
        if check == 0:
            pass
    elif keys[pygame.K_a]:
        car = pygame.image.load("car and map testing/car(left).png")
        check = final_list[(y_car + 16) // 32][(x_car - 280 - 1) // 32]
        if check == 1:
            x_car -= 2
        if check == 3:
            if ((y_car + 16) // 32, (x_car - 280 - 1) // 32) in spis:
                if spis.index(((y_car + 16) // 32, (x_car - 280 - 1) // 32)) == 0:
                    y_punkt_1, x_punkt_1 = -32, 0
                    nezaversheny -= 1
                    spis[0] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 16) // 32, (x_car - 280 - 1) // 32)) == 1:
                    y_punkt_2, x_punkt_2 = -32, 0
                    nezaversheny -= 1
                    spis[1] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 16) // 32, (x_car - 280 - 1) // 32)) == 2:
                    y_punkt_3, x_punkt_3 = -32, 0
                    nezaversheny -= 1
                    spis[2] = (-32, 0)
                    sobrano += 1
            if nezaversheny == 0:
                bezdelnik = True
                spis.clear()
            x_car -= 2
        if check == 0:
            pass  # >-)
    elif keys[pygame.K_w]:
        car = pygame.image.load("car and map testing/car(up).png")
        check = final_list[(y_car - 1) // 32][(x_car + 16 - 280) // 32]
        if check == 1:
            y_car -= 2
        if check == 3:
            if ((y_car - 1) // 32, (x_car - 280 + 16) // 32) in spis:
                if spis.index(((y_car - 1) // 32, (x_car - 280 + 16) // 32)) == 0:
                    y_punkt_1, x_punkt_1 = -32, 0
                    nezaversheny -= 1
                    spis[0] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car - 1) // 32, (x_car - 280 + 16) // 32)) == 1:
                    y_punkt_2, x_punkt_2 = -32, 0
                    nezaversheny -= 1
                    spis[1] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car - 1) // 32, (x_car - 280 + 16) // 32)) == 2:
                    y_punkt_3, x_punkt_3 = -32, 0
                    nezaversheny -= 1
                    spis[2] = (-32, 0)
                    sobrano += 1
            if nezaversheny == 0:
                bezdelnik = True
                spis.clear()
            y_car -= 2
        if check == 2:
            if bezdelnik:
                spis = random.sample(punkty, 3)
                y_punkt_1, x_punkt_1 = spis[0][0] * 32, spis[0][1] * 32 + 280
                y_punkt_2, x_punkt_2 = spis[1][0] * 32, spis[1][1] * 32 + 280
                y_punkt_3, x_punkt_3 = spis[2][0] * 32, spis[2][1] * 32 + 280
                bezdelnik = False
                nezaversheny = 3
        if check == 0:
            pass
    elif keys[pygame.K_s]:
        car = pygame.image.load("car and map testing/car(down).png")
        check = final_list[(y_car + 1 + 32) // 32][(x_car + 16 - 280 - 1) // 32]
        if check == 1:
            y_car += 2
        if check == 3:
            if ((y_car + 1 + 32) // 32, (x_car - 280 + 16 - 1) // 32) in spis:
                if spis.index(((y_car + 1 + 32) // 32, (x_car - 280 + 16 - 1) // 32)) == 0:
                    y_punkt_1, x_punkt_1 = -32, 0
                    nezaversheny -= 1
                    spis[0] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 1 + 32) // 32, (x_car - 280 + 16 - 1) // 32)) == 1:
                    y_punkt_2, x_punkt_2 = -32, 0
                    nezaversheny -= 1
                    spis[1] = (-32, 0)
                    sobrano += 1
                elif spis.index(((y_car + 1 + 32) // 32, (x_car - 280 + 16 - 1) // 32)) == 2:
                    y_punkt_3, x_punkt_3 = -32, 0
                    nezaversheny -= 1
                    spis[2] = (-32, 0)
                    sobrano += 1
            if nezaversheny == 0:
                bezdelnik = True
                spis.clear()
            y_car += 2
        if check == 0:
            pass
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            start_game = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                menu.Menu_screeen()
                window = pygame.display.set_mode(SIZE)
                start_time = time.time() - elapsed_time
    screen.fill(000000)
    screen.blit(bg, (280, 0))
    screen.blit(car, (x_car, y_car))
    screen.blit(text_counter, (925, 5))
    screen.blit(text_timer, (850, 160))
    screen.blit(punkt_1, (x_punkt_1, y_punkt_1))
    screen.blit(punkt_2, (x_punkt_2, y_punkt_2))
    screen.blit(punkt_3, (x_punkt_3, y_punkt_3))
    window.blit(screen, (0, 0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
